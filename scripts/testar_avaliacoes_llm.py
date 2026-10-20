#!/usr/bin/env python3
"""Testes offline/mocks, nunca resultados reais de modelos."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

source=Path(__file__).resolve().parent/"executar-avaliacoes-llm.py"
spec=importlib.util.spec_from_file_location("llmrunner",source)
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class Response:
    status=200
    def __init__(self,value): self.raw=json.dumps(value).encode()
    def __enter__(self): return self
    def __exit__(self,*args): return False
    def read(self,size=None): return self.raw

class Tests(unittest.TestCase):
    def test_payloads(self):
        for p in runner.PROVIDERS:
            url,body,headers=runner.payload(p,"model-test","same system","same question","TEST-KEY")
            self.assertTrue(url.startswith("https://"))
            self.assertIn("TEST-KEY"," ".join(headers.values()))
            text=json.dumps(body)
            self.assertIn("same system",text)
            self.assertIn("same question",text)

    def test_response_parsers(self):
        body={
            "openai":{"id":"r1","model":"m","output":[{"content":[{"type":"output_text","text":"ok"}]}]},
            "anthropic":{"id":"m1","model":"m","content":[{"type":"text","text":"ok"}]},
            "gemini":{"responseId":"g1","modelVersion":"m","candidates":[{"content":{"parts":[{"text":"ok"}]}}]},
            "xai":{"id":"x1","model":"m","choices":[{"message":{"content":"ok"}}]},
        }
        for p,value in body.items():
            answer,rid,model=runner.unpack(p,value)
            self.assertEqual(answer,"ok")
            self.assertTrue(rid)
            self.assertEqual(model,"m")

    def test_mocked_network_only_tests_parser(self):
        prompt={"id":"PA01","system":"same","user":"test","input_sha256":"abc"}
        fake={"id":"fake","model":"fake","choices":[{"message":{"content":"synthetic"}}]}
        with patch.object(runner,"urlopen",return_value=Response(fake)):
            row=runner.invoke("xai","test-model",prompt,"TEST-KEY",5)
        self.assertEqual(row["status"],runner.STATUS_REAL)
        self.assertEqual(row["semantic_review"],"PENDING_HUMAN_REVIEW")

    def test_dryrun_never_sends_requests(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(runner,"urlopen",side_effect=AssertionError("network forbidden")):
                exitcode=runner.main(["--max-cases","2","--out",tmp])
            result=json.loads((Path(tmp)/"resultados.json").read_text())
        self.assertEqual(exitcode,0)
        self.assertEqual(len(result["results"]),8)
        self.assertTrue(all(x["status"]=="NOT_EXECUTED" for x in result["results"]))

    def test_missing_credentials_blocks_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.dict(os.environ,{"OPENAI_API_KEY":"","MODEL_OPENAI":"test-model"},clear=True):
                with patch.object(runner,"urlopen",side_effect=AssertionError("network forbidden")):
                    code=runner.main(["--execute","--approve-spend","--providers","openai","--max-cases","1","--out",tmp])
            result=json.loads((Path(tmp)/"resultados.json").read_text())
        self.assertEqual(code,2)
        self.assertEqual(result["results"][0]["status"],"BLOCKED_NO_CREDENTIALS")

    def test_execute_requires_paid_api_confirmation(self):
        with self.assertRaises(SystemExit):
            runner.main(["--execute","--max-cases","1"])

if __name__=="__main__": unittest.main()
