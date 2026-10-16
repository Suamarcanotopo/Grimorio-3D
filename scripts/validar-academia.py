#!/usr/bin/env python3
"""Valida a academia didatica 3D sem dependencias externas ou internet."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MIN_TERMS = 293
MIN_FAQ = 184
MIN_TUTORIALS = 19
MIN_PIPELINES = 10
MIN_SOURCES = 208


def check():
    errors = []
    docs = sorted(ROOT.rglob("*.md"))
    blob_files = {p.resolve() for p in ROOT.rglob("*") if p.is_file()}
    for path in docs:
        text = path.read_text(encoding="utf-8")
        # Ignora blocos de codigo para que exemplos literais nao sejam tratados como links.
        without_code = re.sub(r"```.*?```", "", text, flags=re.S)
        for match in re.finditer(r"!?(?:\[[^\]]*\])\(([^)]+)\)", without_code):
            dest = match.group(1).strip().split(" ", 1)[0].strip("<>")
            dest = unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if not dest or "://" in dest or dest.startswith(("mailto:", "data:", "#")):
                continue
            if dest.startswith("/"):
                errors.append(f"Link absoluto interno nao portavel: {path.relative_to(ROOT)} -> {dest}")
                continue
            target = (path.parent / dest).resolve()
            if target not in blob_files:
                errors.append(f"Link quebrado: {path.relative_to(ROOT)} -> {dest}")
    def load_text(path):
        p = ROOT / path
        if not p.exists():
            errors.append(f"Arquivo ausente: {path}")
            return ""
        return p.read_text(encoding="utf-8")
    glossary = load_text("GLOSSARIO/README.md")
    faq = load_text("FAQ/README.md")
    tutorials = load_text("TUTORIAIS/README.md")
    deps = load_text("DEPENDENCIAS/README.md")
    if not glossary or not faq or not tutorials or not deps:
        return errors
    g_files = sorted((ROOT / "GLOSSARIO").glob("[0-9]*.md"))
    f_files = sorted((ROOT / "FAQ").glob("[0-9]*.md"))
    t_files = sorted((ROOT / "TUTORIAIS").glob("[0-9]*.md"))
    g_count = sum(len(re.findall(r"^### \d+\.", x.read_text(encoding="utf-8"), re.M)) for x in g_files)
    f_count = sum(len(re.findall(r"^## \d+\.", x.read_text(encoding="utf-8"), re.M)) for x in f_files)
    if g_count < MIN_TERMS or g_count != 293:
        errors.append(f"Glossario incompleto: {g_count}")
    if f_count < MIN_FAQ or f_count != 184:
        errors.append(f"FAQ incompleto: {f_count}")
    if len(t_files) != MIN_TUTORIALS:
        errors.append(f"Tutoriais incompletos: {len(t_files)}")
    if len(g_files) != 15 or len(f_files) != 18:
        errors.append("Seções didaticas removidas")
    for path in t_files:
        body = path.read_text(encoding="utf-8")
        for expected in ("Antes de começar", "Entregável verificável", "Como fazer", "Como saber se deu certo", "Onde aprender"):
            if expected not in body:
                errors.append(f"Tutorial sem campo {expected}: {path}")
        if len(re.findall(r"^\d+\. \*\*Etapa", body, re.M)) < 7:
            errors.append(f"Tutorial sem passos suficientes: {path}")
    dep = json.loads(load_text("DEPENDENCIAS/matriz.json") or "{}")
    p = dep.get("pipelines", [])
    if len(p) != MIN_PIPELINES:
        errors.append(f"Pipelines incompletos: {len(p)}")
    seen = set()
    for item in p:
        if item.get("id") in seen:
            errors.append("Pipeline duplicado")
        seen.add(item.get("id"))
        for key in ("title", "from", "via", "to", "urls", "obrigatorios", "status"):
            if not item.get(key):
                errors.append(f"Pipeline sem {key}: {item.get('id')}")
        for u in item.get("urls", []):
            if not u.startswith("https://"):
                errors.append(f"Fonte de dependencias nao HTTPS: {u}")
    catalog = json.loads(load_text("FONTES/catalogo.json") or "[]")
    if len(catalog) < MIN_SOURCES:
        errors.append(f"Catalogo encolheu: {len(catalog)}")
    for field,need in [(glossary,str(MIN_TERMS)),(faq,str(MIN_FAQ)),(tutorials,str(MIN_TUTORIALS))]:
        if need not in field:
            errors.append(f"Indice sem contagem de {need}")
    readme=load_text("README.md")
    for href in ("GLOSSARIO/README.md","FAQ/README.md","TUTORIAIS/README.md","DEPENDENCIAS/README.md","ACADEMIA/MAPA-DE-COMPETENCIAS.md"):
        if href not in readme:
            errors.append(f"README nao tem link {href}")
    print(f"Arquivos MD: {len(docs)} | Glossario: {g_count} | FAQ: {f_count} | Tutoriais: {len(t_files)} | Pipelines: {len(p)} | Fontes: {len(catalog)} | Erros: {len(errors)}")
    for e in errors:
        print("FALHA:", e)
    return not errors

if __name__ == "__main__":
    sys.exit(0 if check() else 1)
