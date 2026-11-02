#!/usr/bin/env python3
"""SIN-TRACE-01: PR change coverage; stdlib-only. Docs contract in grimorio-skills/GOVERNANCA."""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEDGER=Path("GOVERNANCA/RASTREABILIDADE/changes")
REPOS={"Suamarcanotopo/grimorio-skills","Suamarcanotopo/Grimorio-SIN",
       "Suamarcanotopo/ListOFprompts","Suamarcanotopo/Grimorio-3D"}
RELS={"TEACHES","VISUALIZES","IMPLEMENTS","TESTS","REFERENCES","CONSUMES","AFFECTS"}
STATES={"DRAFT","NOT_RUN","NOT_VERIFIED","VERIFIED_STATIC","RETEST"}
HEXSHA=re.compile(r"^[0-9a-f]{40}$")
def git(*args):
    return subprocess.check_output(["git",*args],cwd=ROOT,stderr=subprocess.STDOUT,text=True).strip()
def changed_paths(base):
    merge_base=git("merge-base","HEAD",base)
    changed=set(filter(None,git("diff","--no-renames","--name-only",merge_base,"HEAD").splitlines()))
    return merge_base,changed
def check_manifest(m,repo):
    errors=[]
    for k in ("mission_id","repository","base_sha","owner","summary","risk","state",
              "changed_paths","tests","rollback","handoff","bridges"):
        if k not in m: errors.append("MISSING_FIELD:"+k)
    if errors: return errors
    if m["repository"]!=repo: errors.append("WRONG_REPO")
    if not isinstance(m["mission_id"],str) or not re.fullmatch(r"[A-Za-z0-9_.-]{6,100}",m["mission_id"]):
        errors.append("BAD_MISSION_ID")
    if not isinstance(m["base_sha"],str) or not HEXSHA.fullmatch(m["base_sha"]):errors.append("BAD_BASE_SHA")
    if m["risk"] not in ("R0","R1","R2","R3"): errors.append("BAD_RISK")
    if m["state"] not in ("DRAFT","CANDIDATE","RETEST"):errors.append("BAD_STATE")
    if not isinstance(m["owner"],str) or not m["owner"].strip():errors.append("OWNER_MISSING")
    for k in ("summary","rollback","handoff"):
        if not isinstance(m[k],str) or len(m[k].strip())<12: errors.append("EMPTY_"+k)
    paths=m["changed_paths"]
    if not isinstance(paths,list) or not paths or len(set(paths))!=len(paths):errors.append("INVALID_PATH_LIST")
    else:
        for p in paths:
            if not isinstance(p,str) or p.startswith("/") or ".." in Path(p).parts or "\\" in p:
                errors.append("UNSAFE_PATH")
    if not isinstance(m["tests"],list) or not m["tests"]:errors.append("NO_TEST_RECEIPTS")
    else:
        for x in m["tests"]:
            if not isinstance(x,dict) or x.get("state") not in STATES or not x.get("command"):
                errors.append("INVALID_TEST_ENTRY")
            if isinstance(x,dict) and x.get("state")=="VERIFIED_STATIC" and not x.get("receipt"):
                errors.append("FAKE_PASS_NO_RECEIPT")
    if not isinstance(m["bridges"],list): errors.append("INVALID_BRIDGES")
    else:
        for b in m["bridges"]:
            if not isinstance(b,dict) or b.get("target_repo") not in REPOS or b.get("target_repo")==repo:
                errors.append("INVALID_BRIDGE_REPO");continue
            if b.get("relationship") not in RELS or b.get("state") not in ("PROPOSED","PENDING_REVIEW","APPROVED_WITH_REFERENCE"):
                errors.append("INVALID_BRIDGE_CONTRACT")
            if not isinstance(b.get("target_path"),str) or not b["target_path"].strip():
                errors.append("MISSING_BRIDGE_TARGET")
    return errors
def audit(repo,base):
    if repo not in REPOS:raise ValueError("UNKNOWN_REPOSITORY")
    mb,changed=changed_paths(base)
    records=[]
    for path in sorted((ROOT/LEDGER).glob("*.json")):
        data=json.loads(path.read_text(encoding="utf-8"))
        errors=check_manifest(data,repo)
        if errors:raise ValueError(f"{path.relative_to(ROOT)}:"+",".join(errors))
        records.append((path.relative_to(ROOT).as_posix(),data))
    if not records: raise ValueError("MISSING_CHANGE_MANIFEST")
    relevant=[(p,m) for p,m in records if p in changed]
    if not relevant:raise ValueError("NO_MANIFEST_CHANGED_IN_THIS_PR")
    covered=set()
    for p,m in relevant:
        if m["base_sha"] != mb:raise ValueError(f"BASELINE_DRIFT:{p}:{mb}")
        if p not in m["changed_paths"]:raise ValueError("MANIFEST_MUST_COVER_ITSELF:"+p)
        covered.update(m["changed_paths"])
    missing=sorted(changed-covered)
    invented=sorted(covered-changed)
    if missing:raise ValueError("UNCOVERED_CHANGES:"+",".join(missing))
    if invented:raise ValueError("CLAIMED_BUT_UNCHANGED:"+",".join(invented))
    return {"result":"PASS_STATIC_CHANGE_COVERAGE","repository":repo,"base_sha":mb,
            "changed_paths":len(changed),"manifests":len(relevant),"bridges":sum(len(m["bridges"]) for _,m in relevant),
            "runtime":"NOT_VERIFIED","note":"CI is not a branch rule or downstream delivery."}
def main():
    a=argparse.ArgumentParser();a.add_argument("--repo",required=True);a.add_argument("--base",default=None)
    ns=a.parse_args()
    base=ns.base or f"origin/{os.environ.get('GITHUB_BASE_REF','main')}"
    try: res=audit(ns.repo,base);print(json.dumps(res,ensure_ascii=False,indent=2))
    except (ValueError,subprocess.CalledProcessError,json.JSONDecodeError) as exc:
        print("SIN-TRACE-01 BLOCK:",exc,file=sys.stderr);return 1
    return 0
if __name__=="__main__":sys.exit(main())
