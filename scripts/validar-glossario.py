#!/usr/bin/env python3
"""Confere Glossário 3D ampliado, estrutura, duplicações e links internos."""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = 293
SECTIONS = 15

def normalize(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.split(" (")[0].strip()

def main():
    errors = []
    files = sorted((ROOT / "GLOSSARIO").glob("[0-9]*.md"))
    index = (ROOT / "GLOSSARIO/README.md").read_text(encoding="utf-8")
    seen = {}
    total = 0
    if len(files) != SECTIONS:
        errors.append(f"Seções: {len(files)} em vez de {SECTIONS}")
    for p in files:
        data = p.read_text(encoding="utf-8")
        terms = re.findall(r"^### \d+\. (.+)$", data, re.M)
        total += len(terms)
        if not terms or f"]({p.name})" not in index:
            errors.append(f"Módulo ausente do índice ou sem termos: {p.name}")
        for term in terms:
            key = normalize(term)
            if key in seen:
                errors.append(f"Conceito duplicado: {term} ({seen[key]} e {p.name})")
            seen[key] = p.name
        for token in ("O que é:", "Por que importa:", "Como praticar:", "Onde aprender:"):
            if data.count(token) != len(terms):
                errors.append(f"Dados didáticos incompletos: {p.name}/{token}")
        if not p.name.startswith(("0", "1")):
            errors.append(f"Nome do módulo não sequencial: {p.name}")
    if total != BASELINE or f"**{BASELINE} termos" not in index:
        errors.append(f"Contagem divergente: {total} em vez de {BASELINE}")
    print(f"Glossário: {total} conceitos únicos, {len(files)} módulos, erros={len(errors)}")
    for e in errors:
        print("FALHA:", e)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
