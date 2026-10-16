#!/usr/bin/env python3
"""Verifica 10 demonstrações HTML offline, navegação e ausência de SDKs executáveis."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = False
        self.title = False
        self.viewport = False
        self.footer = False
        self.external = False
        self.script_count = 0
        self.aria = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "html" and data.get("lang", "").lower() == "pt-br":
            self.lang = True
        if tag == "title":
            self.title = True
        if tag == "meta" and data.get("name") == "viewport":
            self.viewport = True
        if tag == "footer":
            self.footer = True
        if any(k.startswith("aria-") for k in data):
            self.aria = True
        if tag == "script":
            self.script_count += 1
            if "src" in data:
                self.external = True

def main():
    errors = []
    paths = sorted((ROOT / "EXEMPLOS").glob("[0-9]*.html"))
    index = (ROOT / "EXEMPLOS/README.md").read_text(encoding="utf-8")
    if len(paths) != 10:
        errors.append("Esperadas 10 demonstrações offline")
    for order, path in enumerate(paths, 1):
        html = path.read_text(encoding="utf-8")
        parsed = Inspector()
        parsed.feed(html)
        if int(path.name[:2]) != order:
            errors.append("Numeração incorreta: " + path.name)
        if not all((parsed.lang, parsed.title, parsed.viewport, parsed.footer, parsed.aria)):
            errors.append("HTML sem estrutura, idioma, viewport, rodapé ou acessibilidade: " + path.name)
        if parsed.external or parsed.script_count != 1:
            errors.append("Scripts externos ou múltiplos em " + path.name)
        if "prefers-reduced-motion" not in html:
            errors.append("Sem preferência de movimento reduzido: " + path.name)
        if "sistemaimersivonarrativo.com.br" not in html:
            errors.append("Sem convite ao SIN: " + path.name)
        if "](" + path.name + ")" not in index:
            errors.append("Sem navegação no índice: " + path.name)
        if "fetch(" in html or "XMLHttpRequest" in html:
            errors.append("Possível solicitação de rede: " + path.name)
    print(f"Exemplos HTML: {len(paths)} | Erros de estrutura: {len(errors)}")
    for problem in errors:
        print("FALHA:", problem)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
