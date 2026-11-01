#!/usr/bin/env python3
"""Teste estrutural do indice dos caminhos Git; nao valida URLs externas."""
from pathlib import Path
import subprocess
R=Path(__file__).resolve().parents[1]
paths=set(p.decode() for p in subprocess.check_output(["git","ls-files","-z"],cwd=R).split(b"\0") if p)
lines=(R/"CATALOGO-TOTAL-ARQUIVOS.md").read_text().splitlines()
named=[s.split("`")[1] for s in lines if s.startswith("- [`") and "`](" in s]
m=paths-set(named);x=set(named)-paths;duplicates=len(named)-len(set(named))
print("git",len(paths),"inventario",len(named),"ausentes",len(m),"excedentes",len(x),"duplicados",duplicates)
if m or x or duplicates:
 print("missing",sorted(m)[:30],"extras",sorted(x)[:30]);raise SystemExit(1)
print("PASS - 100% caminhos Git no indice")
