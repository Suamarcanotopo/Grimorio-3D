"""Negative and positive contract tests; not proof of GitHub branch protection."""
import importlib.util
import unittest
from pathlib import Path
F=Path(__file__).resolve().parents[1]/"scripts"/"validar-rastreabilidade-sin.py"
spec=importlib.util.spec_from_file_location("trace",F)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def valid():
 return {"mission_id":"SIN-TRACE-20261102","repository":"Suamarcanotopo/grimorio-skills",
 "base_sha":"a"*40,"owner":"repository:grimorio-skills","summary":"Add a versioned source of change truth",
 "risk":"R1","state":"DRAFT","changed_paths":["GOVERNANCA/RASTREABILIDADE/changes/TEST.json"],
 "file_changes":{"GOVERNANCA/RASTREABILIDADE/changes/TEST.json":{"action":"A","description":"Create the mission change manifest and record accountability","owner":"repository:grimorio-skills"}},
 "affected_skill_roles":{"controller":"engineering-control-plane","reviewer":"coliseum"},
 "tests":[{"command":"python3 -m unittest","state":"NOT_RUN"}],
 "rollback":"Revert candidate PR, never delete canonical files",
 "handoff":"Review this change and rerun the required tests","bridges":[]}
class ContractTest(unittest.TestCase):
 def test_valid(self): self.assertEqual(mod.check_manifest(valid(),"Suamarcanotopo/grimorio-skills"),[])
 def test_missing_owner(self):
  d=valid();d["owner"]="";self.assertIn("OWNER_MISSING",mod.check_manifest(d,d["repository"]))
 def test_missing_file_description(self):
  d=valid();d["file_changes"]={}
  self.assertIn("FILE_CHANGE_DETAILS_MISMATCH",mod.check_manifest(d,d["repository"]))
 def test_wrong_change_action(self):
  d=valid();next(iter(d["file_changes"].values()))["action"]="MAGIC"
  self.assertTrue(any("INVALID_FILE_CHANGE_NOTE" in x for x in mod.check_manifest(d,d["repository"])))
 def test_missing_skill_roles(self):
  d=valid();d["affected_skill_roles"]={}
  self.assertIn("SKILL_COMMUNICATION_ROLES_MISSING",mod.check_manifest(d,d["repository"]))
 def test_missing_tests(self):
  d=valid();d["tests"]=[];self.assertIn("NO_TEST_RECEIPTS",mod.check_manifest(d,d["repository"]))
 def test_fictitious_pass(self):
  d=valid();d["tests"][0]["state"]="VERIFIED_STATIC"
  self.assertIn("FAKE_PASS_NO_RECEIPT",mod.check_manifest(d,d["repository"]))
 def test_wrong_repo(self):
  d=valid();self.assertIn("WRONG_REPO",mod.check_manifest(d,"Suamarcanotopo/ListOFprompts"))
 def test_bad_bridge(self):
  d=valid();d["bridges"]=[{"target_repo":"third-party/foo","relationship":"AFFECTS","target_path":"abc","state":"PROPOSED"}]
  self.assertIn("INVALID_BRIDGE_REPO",mod.check_manifest(d,d["repository"]))
 def test_duplicate_paths(self):
  d=valid();d["changed_paths"].append(d["changed_paths"][0])
  self.assertIn("INVALID_PATH_LIST",mod.check_manifest(d,d["repository"]))
 def test_path_traversal(self):
  d=valid();d["changed_paths"]=["../secrets"]
  self.assertIn("UNSAFE_PATH",mod.check_manifest(d,d["repository"]))
 def test_no_approval_by_text(self):
  self.assertNotIn("PRODUCTION_VERIFIED",mod.audit.__doc__ or "")
if __name__=="__main__":unittest.main()
