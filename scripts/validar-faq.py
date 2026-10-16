#!/usr/bin/env python3
"""FAQ SIN 3D: 184 perguntas modulares, 26 por mercado, sem repetição."""
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
def normalize(v):
    s=unicodedata.normalize("NFD", v.lower())
    return "".join(c for c in s if unicodedata.category(c)!="Mn").strip().rstrip("?!.")

def main():
    errors=[]
    files=sorted((ROOT/"FAQ").glob("[0-9]*.md"))
    index=(ROOT/"FAQ/README.md").read_text(encoding="utf-8")
    count=0
    seen=set()
    if len(files)!=18:
        errors.append(f"Seções: {len(files)} em vez de 18")
    for path in files:
        data=path.read_text(encoding="utf-8")
        qs=re.findall(r"^## \d+\. (.+)$", data, re.M)
        count+=len(qs)
        if f"]({path.name})" not in index:
            errors.append(f"Índice sem {path.name}")
        for q in qs:
            norm=normalize(q)
            if norm in seen:
                errors.append(f"Questão repetida: {q}")
            seen.add(norm)
        for key in ("**Resposta:**", "**Por que isso importa?**", "**Como fazer:**", "**Onde aprender / boas práticas:**"):
            if data.count(key)!=len(qs):
                errors.append(f"Campo incompleto {path.name}: {key}")
    market=(ROOT/"FAQ/PERGUNTAS-POR-MERCADO.md").read_text(encoding="utf-8")
    mcount=len(re.findall(r"^## \d+\. ",market,re.M))
    if count!=184 or mcount!=26 or count+mcount!=210:
        errors.append(f"Esperados 184+26=210, obtidos {count}+{mcount}")
    if "210 respostas" not in index or "26 perguntas profissionais" not in index:
        errors.append("Navegação e contagem de FAQ desatualizadas")
    print(f"FAQ: {count} perguntas modulares, {mcount} perguntas por mercado; erros={len(errors)}")
    for e in errors: print("FALHA:",e)
    return 1 if errors else 0

if __name__=="__main__":
    sys.exit(main())
