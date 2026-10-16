#!/usr/bin/env python3
"""Auditoria documental de 37 tutoriais preservando baselines e conteúdo."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    errors=[]
    docs=sorted((ROOT/"TUTORIAIS").glob("[0-9]*.md"))
    index=(ROOT/"TUTORIAIS/README.md").read_text(encoding="utf-8")
    seen=set()
    totalsteps=0
    if len(docs)!=37:
        errors.append(f"Há {len(docs)} projetos, esperado 37")
    for i,p in enumerate(docs,1):
        data=p.read_text(encoding="utf-8")
        digits=p.name.split("-",1)[0]
        if int(digits)!=i:
            errors.append(f"Numeração inesperada: {p.name}")
        if p.name in seen:
            errors.append(f"Nome duplicado: {p.name}")
        seen.add(p.name)
        if f"]({p.name})" not in index:
            errors.append(f"Ausente do índice: {p.name}")
        steps=re.findall(r"^\d+\. \*\*Etapa \d+:\*\*",data,re.M)
        totalsteps+=len(steps)
        if len(steps)<7:
            errors.append(f"Menos de 7 etapas: {p.name}")
        for key in ("Antes de começar", "Entregável verificável", "Como fazer", "Como saber se deu certo", "Armadilha a evitar", "Onde aprender", "Fonte primária"):
            if key not in data:
                errors.append(f"Sem {key}: {p.name}")
        if i>=20 and "Comunidade SIN:" not in data:
            errors.append(f"Novo tutorial sem rodapé SIN: {p.name}")
    if "37 projetos guiados" not in index:
        errors.append("Índice sem contagem 37")
    print(f"Tutoriais: {len(docs)} | Etapas documentadas: {totalsteps} | Erros: {len(errors)}")
    for err in errors: print("FALHA:",err)
    return 1 if errors else 0
if __name__=="__main__":
    sys.exit(main())
