#!/usr/bin/env python3
"""Confere cobertura integral de URLs, navegação e rodapé SIN no README."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CAT = json.loads((ROOT / "FONTES/catalogo.json").read_text(encoding="utf-8"))
MORE = json.loads((ROOT / "FONTES/links-complementares.json").read_text(encoding="utf-8"))
LABELS = json.loads((ROOT / "FONTES/rotulos-de-nichos.json").read_text(encoding="utf-8"))
START = "<!-- INICIO_INDICE_URLS_GRIMORIO_3D -->"
END = "<!-- FIM_INDICE_URLS_GRIMORIO_3D -->"
CTA = (
    "https://sistemaimersivonarrativo.com.br/",
    "https://github.com/Suamarcanotopo/grimorio-skills",
    "https://www.instagram.com/suamarcanotopo/",
    "https://www.youtube.com/@suamarcanotopo?sub_confirmation=1",
    "https://chat.whatsapp.com/F11omHqfI4KKCC0Sgbc4Vm?s=cl&p=i&mlu=4&ilr=4",
    "https://chat.whatsapp.com/FcyMOdQqyW8Ci104P8i3Gg?s=cl&p=i&mlu=4&ilr=4",
    "https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5",
)

def main():
    errors = []
    try:
        segment = README.split(START, 1)[1].split(END, 1)[0]
    except IndexError:
        print("FALHA: Bloco do índice integral ausente")
        return 1
    if README.count(START) != 1 or README.count(END) != 1:
        errors.append("Marcadores repetidos")
    known = set()
    for entry in CAT:
        url = entry["url"]
        if not url.startswith("https://"):
            errors.append("URL do catálogo sem HTTPS: " + url)
        if f"<{url}>" not in segment:
            errors.append("URL faltante no README: " + url)
        if entry["id"] not in segment:
            errors.append("ID faltante: " + entry["id"])
        known.add(url.rstrip("/").lower())
        terms = entry.get("fonte_termos", "")
        if terms.startswith("https://") and terms != url and f"<{terms}>" not in segment:
            errors.append("URL dos termos ausente: " + terms)
    for entry in MORE:
        url = entry["url"]
        if f"<{url}>" not in segment:
            errors.append("URL complementar ausente: " + url)
        if url.rstrip("/").lower() in known:
            errors.append("URL extra duplicada do catálogo: " + url)
    if set(LABELS) != {x["nicho"] for x in CAT}:
        errors.append("Rótulos não correspondem às categorias do catálogo")
    for category in LABELS:
        if f'id="fontes-{category}"' not in segment:
            errors.append("Âncora ausente: " + category)
    if segment.count("<details>") != len(LABELS) or segment.count("</details>") != len(LABELS):
        errors.append("Categorias recolhíveis incompletas")
    if "## ⭐ Comunidade SIN" not in README:
        errors.append("Rodapé não existe")
        footer = ""
    else:
        footer = README.rsplit("## ⭐ Comunidade SIN", 1)[-1]
    for link in CTA:
        if f"<{link}>" not in footer:
            errors.append("CTA do SIN ausente do rodapé: " + link)
    if not (README.index(END) < README.rfind("## ⭐ Comunidade SIN")):
        errors.append("Rodapé não é a última seção do índice")
    mdlinks = re.findall(r"\]\(([^)]+)\)", README)
    for dest in mdlinks:
        if "://" in dest or dest.startswith(("#", "mailto:")):
            continue
        path = unquote(dest.split("#", 1)[0].split("?", 1)[0])
        if path and not (ROOT / path).exists():
            errors.append("Navegação interna do README quebrada: " + path)
    print(f"Índice: {len(CAT)} fontes, {len(MORE)} extras, {len(LABELS)} categorias, {len(CTA)} CTAs; erros={len(errors)}")
    for e in errors:
        print("FALHA:", e)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
