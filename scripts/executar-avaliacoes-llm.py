#!/usr/bin/env python3
"""Execucao opt-in de APIs LLM; dry-run e mocks nao constituem execucao real."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
from time import monotonic
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ("openai", "anthropic", "gemini", "xai")
KEYS = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY",
        "gemini": "GEMINI_API_KEY", "xai": "XAI_API_KEY"}
MODELS = {"openai": "MODEL_OPENAI", "anthropic": "MODEL_ANTHROPIC",
          "gemini": "MODEL_GEMINI", "xai": "MODEL_XAI"}
STATUS_REAL = "API_RESPONSE_RECEIVED"
STATUS_DRY = "NOT_EXECUTED"
STATUS_BLOCKED = "BLOCKED_NO_CREDENTIALS"
STATUS_MODEL = "BLOCKED_NO_MODEL"
STATUS_ERROR = "API_ERROR"
STATUS_INVALID = "INVALID_API_RESPONSE"

def jsonfile(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def prepare(cases, catalog, contract):
    sources = {x["id"]: x for x in catalog}
    system = contract + "\nNunca presuma execucao real, licenca ou homologacao sem evidencia."
    result = []
    for c in cases:
        s = sources[c["source_id"]]
        user = (
            "AVALIACAO 3D CONTROLADA. Responda em PT-BR, com conceito, procedimento, "
            "convencao, truque, erro comum, como testar, status verdadeiro e proximo passo. "
            "Nao acione ferramentas nem invente evidencias.\n"
            + "ETAPA: " + c["stage"] + "\n"
            + "FONTE DO CATALOGO: " + s["id"] + " | " + s["titulo"] + " | " + s["url"] + "\n"
            + "PEDIDO: " + c["input"]
        )
        result.append({"id": c["id"], "system": system, "user": user,
                       "input_sha256": digest(system + "\n---\n" + user)})
    return result

def payload(provider, model, system, user, key):
    if provider == "openai":
        return ("https://api.openai.com/v1/responses",
                {"model": model, "instructions": system, "input": user,
                 "max_output_tokens": 1100, "store": False},
                {"Authorization": "Bearer " + key})
    if provider == "anthropic":
        return ("https://api.anthropic.com/v1/messages",
                {"model": model, "max_tokens": 1100, "system": system,
                 "messages": [{"role": "user", "content": user}]},
                {"x-api-key": key, "anthropic-version": "2023-06-01"})
    if provider == "gemini":
        if not model.replace("-", "").replace(".", "").replace("_", "").isalnum():
            raise ValueError("invalid Gemini model identifier")
        return ("https://generativelanguage.googleapis.com/v1beta/models/"
                + model + ":generateContent",
                {"systemInstruction": {"parts": [{"text": system}]},
                 "contents": [{"role": "user", "parts": [{"text": user}]}],
                 "generationConfig": {"maxOutputTokens": 1100}},
                {"x-goog-api-key": key})
    if provider == "xai":
        return ("https://api.x.ai/v1/chat/completions",
                {"model": model, "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}],
                 "max_tokens": 1100}, {"Authorization": "Bearer " + key})
    raise ValueError("provider not supported")

def unpack(provider, body):
    rid = str(body.get("id") or body.get("responseId") or "")
    model = str(body.get("model") or body.get("modelVersion") or "")
    if provider == "openai":
        text = body.get("output_text") or "\n".join(
            part.get("text", "") for item in body.get("output", [])
            for part in item.get("content", []) if part.get("type") == "output_text")
    elif provider == "anthropic":
        text = "\n".join(x.get("text", "") for x in body.get("content", [])
                         if x.get("type") == "text")
    elif provider == "gemini":
        text = "\n".join(part.get("text", "")
                         for c in body.get("candidates", [])[:1]
                         for part in c.get("content", {}).get("parts", [])
                         if isinstance(part.get("text"), str))
    else:
        text = body.get("choices", [{}])[0].get("message", {}).get("content", "")
        if isinstance(text, list):
            text = "\n".join(v.get("text", "") for v in text if isinstance(v, dict))
    return str(text or "").strip(), rid, model

def invoke(provider, model, prompt, key, timeout):
    result = {"provider": provider, "case_id": prompt["id"], "model_requested": model,
              "input_sha256": prompt["input_sha256"], "status": STATUS_ERROR,
              "semantic_review": "NOT_REVIEWED"}
    started = monotonic()
    try:
        url, body, auth = payload(provider, model, prompt["system"], prompt["user"], key)
        request = Request(url, data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
                          headers={"Content-Type": "application/json", **auth},
                          method="POST")
        with urlopen(request, timeout=timeout) as response:
            if not 200 <= response.status < 300:
                raise ValueError("http failed")
            data = json.loads(response.read(1000000).decode("utf-8"))
        answer, rid, returned_model = unpack(provider, data)
        if not answer or not rid:
            result.update(status=STATUS_INVALID, reason="missing text or response id")
        else:
            result.update(status=STATUS_REAL, provider_response_id=rid,
                          model_returned=returned_model or model,
                          response_sha256=digest(answer), output_chars=len(answer),
                          output_excerpt=answer[:12000],
                          semantic_review="PENDING_HUMAN_REVIEW")
    except HTTPError as e:
        result["reason"] = "HTTP " + str(e.code) + " (body omitted)"
    except (URLError, OSError, TimeoutError) as e:
        result["reason"] = "NETWORK_" + type(e).__name__
    except (TypeError, ValueError, KeyError, IndexError) as e:
        result["reason"] = "INVALID_" + type(e).__name__
    result["elapsed_ms"] = round((monotonic() - started) * 1000)
    return result

def report(data, args, providers, prompts, contract, out):
    out.mkdir(parents=True, exist_ok=True)
    result = {
        "schema": "sin3d-api-evidence-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "API_EXECUTION" if args.execute else "DRY_RUN_NO_API",
        "git_sha": os.environ.get("GITHUB_SHA", "LOCAL_UNPINNED"),
        "contract_sha256": digest(contract),
        "case_ids": [p["id"] for p in prompts],
        "summary": {},
        "human_review": "NOT_PERFORMED",
        "results": data,
    }
    for provider in providers:
        mine = [x for x in data if x["provider"] == provider]
        result["summary"][provider] = {
            "verified_api_responses": sum(x["status"] == STATUS_REAL for x in mine),
            "blocked_or_not_run": sum(x["status"] in
                (STATUS_DRY, STATUS_BLOCKED, STATUS_MODEL) for x in mine),
            "errors": sum(x["status"] in (STATUS_ERROR, STATUS_INVALID) for x in mine),
            "semantic_approved": 0,
        }
    file = out / "resultados.json"
    file.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    md = ["# Evidencias de execucao 4 provedores", "",
          "MODO: " + result["mode"] + " | COMMIT: " + result["git_sha"], "",
          "| Provedor | Respostas reais | Bloqueados ou nao executados | Erros | Aprovacao semantica |",
          "|---|---:|---:|---:|---:|"]
    for p, s in result["summary"].items():
        md.append("| " + p + " | " + str(s["verified_api_responses"])
                  + " | " + str(s["blocked_or_not_run"]) + " | "
                  + str(s["errors"]) + " | 0 |")
    md += ["", "Somente API_RESPONSE_RECEIVED com ID e texto comprova invocacao real.",
           "PENDING_HUMAN_REVIEW NAO equivale a aprovacao do Mission Lock.", "",
           "Nenhuma chave API foi gravada neste relatorio."]
    outmd = out / "RESUMO.md"
    outmd.write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "SHA256SUMS.txt").write_text(
        hashlib.sha256(file.read_bytes()).hexdigest() + "  resultados.json\n"
        + hashlib.sha256(outmd.read_bytes()).hexdigest() + "  RESUMO.md\n",
        encoding="utf-8")
    return result

def main(argv=None):
    arg = argparse.ArgumentParser()
    arg.add_argument("--providers", default="openai,anthropic,gemini,xai")
    arg.add_argument("--max-cases", type=int, default=4)
    arg.add_argument("--execute", action="store_true")
    arg.add_argument("--approve-spend", action="store_true")
    arg.add_argument("--timeout", type=int, default=50)
    arg.add_argument("--out", default="resultados-llm")
    args = arg.parse_args(argv)
    providers = [x.strip() for x in args.providers.split(",") if x.strip()]
    if not providers or len(set(providers)) != len(providers) or any(
            p not in PROVIDERS for p in providers):
        arg.error("invalid providers")
    if not 1 <= args.max_cases <= 20 or not 5 <= args.timeout <= 120:
        arg.error("invalid case count or timeout")
    if args.execute and not args.approve_spend:
        arg.error("--execute requires --approve-spend")
    cases = jsonfile("INTEROPERABILIDADE/EVALS/agnostico-casos.json")["cases"]
    catalog = jsonfile("FONTES/catalogo.json")
    contract = (ROOT / "INTEROPERABILIDADE/CONTRATO-CANONICO.md").read_text(encoding="utf-8")
    prompts = prepare(cases[:args.max_cases], catalog, contract)
    results = []
    for provider in providers:
        model = os.getenv(MODELS[provider], "").strip()
        key = os.getenv(KEYS[provider], "").strip()
        for prompt in prompts:
            base = {"provider": provider, "case_id": prompt["id"],
                    "model_requested": model or "NOT_CONFIGURED",
                    "input_sha256": prompt["input_sha256"],
                    "semantic_review": "NOT_REVIEWED"}
            if not args.execute:
                base["status"] = STATUS_DRY
            elif not key:
                base["status"] = STATUS_BLOCKED
            elif not model:
                base["status"] = STATUS_MODEL
            else:
                base = invoke(provider, model, prompt, key, args.timeout)
            print(provider + "/" + prompt["id"] + ": " + base["status"], flush=True)
            results.append(base)
    report(results, args, providers, prompts, contract, Path(args.out))
    statuses = {r["status"] for r in results}
    if not args.execute:
        return 0
    if statuses == {STATUS_REAL}:
        return 0
    if STATUS_BLOCKED in statuses or STATUS_MODEL in statuses:
        return 2
    return 3

if __name__ == "__main__":
    sys.exit(main())
