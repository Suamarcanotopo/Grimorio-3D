#!/usr/bin/env python3
"""Gera e valida o índice completo de URLs do README. Python stdlib somente.

Comandos:
    python3 scripts/gerar-indice-readme.py --check
    python3 scripts/gerar-indice-readme.py --write

Fonte única: FONTES/catalogo.json.
Referências adicionais: FONTES/links-complementares.json.
Rótulos de navegação: FONTES/rotulos-de-nichos.json.
Não realiza consultas à internet, instalações ou inferências de licença.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- INICIO_INDICE_URLS_GRIMORIO_3D -->"
END = "<!-- FIM_INDICE_URLS_GRIMORIO_3D -->"


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def render(catalog, extras, labels):
    grouped = {}
    for row in catalog:
        grouped.setdefault(row["nicho"], []).append(row)
    lines = [
        START,
        f"## 🔗 INDEX GERAL — {len(catalog)} fontes e URLs completas",
        "",
        "Este é o índice **integral das fontes cadastradas**, organizado por finalidade. Abra somente o nicho que você procura. Cada ficha mostra **o que é, para que serve, URL completa e se existe acesso gratuito/freemium**.",
        "",
        "**Como escolher:** comece por um objetivo na [Academia](ACADEMIA/MAPA-DE-COMPETENCIAS.md), confira o [Glossário](GLOSSARIO/README.md), siga os [Tutoriais](TUTORIAIS/README.md) e consulte aqui a ferramenta. Leia sempre a licença do item antes de uso comercial.",
        "",
        f"**Catálogo canônico:** [CSV](FONTES/catalogo.csv) · [JSON](FONTES/catalogo.json) · [Ficha de licenças](GOVERNANCA/REGISTRO-DE-LICENCA.md). **Total:** {len(catalog)} fontes em {len(grouped)} nichos.",
        "",
        "### Escolha uma categoria",
        "",
        "| Nicho de conhecimento | Fontes | Acesso |",
        "|---|---:|---|",
    ]
    for key in sorted(grouped):
        lines.append(f"| {labels.get(key, key)} | {len(grouped[key])} | [Abrir índice](#fontes-{key}) |")
    lines.extend(["", "### Todas as URLs, por nicho", ""])
    for key in sorted(grouped):
        lines.extend([
            f'<a id="fontes-{key}"></a>',
            "<details>",
            f"<summary><strong>{labels.get(key, key)}</strong> · {len(grouped[key])} fontes</summary>",
            "",
        ])
        for row in grouped[key]:
            desc = re.sub(r"[\r\n]+", " ", str(row["descricao"])).strip()
            usage = re.sub(r"[\r\n]+", " ", str(row["para_que_serve"])).strip()
            lines.extend([
                f'- **{row["titulo"]}** (\{row["id"]}\`) — {desc} **Serve para:** {usage}.',
                f'  **URL completa:** <{row["url"]}> · **Acesso:** {row["acesso"]} · **Freemium:** {row["freemium"]}.',
            ])
            terms = row.get("fonte_termos", "")
            if terms and terms != row["url"] and terms.startswith("https://"):
                lines.append(f"  **Termos/licença e detalhes:** <{terms}>.")
        lines.extend(["", "</details>", ""])
    lines.extend([
        "### Portais e documentação complementares",
        "",
        f"Além das {len(catalog)} fontes cadastradas, os guias técnicos citam {len(extras)} URLs auxiliares e portais do próprio ecossistema. Elas ficam listadas aqui para ninguém depender de procurar o endereço em dezenas de arquivos.",
        "",
    ])
    mapped = {}
    for row in extras:
        mapped.setdefault(row["area"], []).append(row)
    for area in sorted(mapped):
        lines.extend([f"#### {area}", ""])
        for row in mapped[area]:
            lines.append(f'- **{row["titulo"]}:** {row["descricao"]} **URL completa:** <{row["url"]}>.')
        lines.append("")
    lines.extend([
        "**Condições:** a presença de uma URL neste índice não comprova que esteja disponível agora, que o conteúdo seja gratuito ou que permita uso comercial. A autoria e as licenças específicas dos assets permanecem com os titulares.",
        "",
        END,
    ])
    return "\n".join(lines) + "\n"


def main():
    arg = argparse.ArgumentParser(description=__doc__)
    mode = arg.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Falha se README estiver desatualizado")
    mode.add_argument("--write", action="store_true", help="Regenera somente o bloco indexado")
    args = arg.parse_args()
    catalog = read_json("FONTES/catalogo.json")
    extra = read_json("FONTES/links-complementares.json")
    labels = read_json("FONTES/rotulos-de-nichos.json")
    content_path = ROOT / "README.md"
    content = content_path.read_text(encoding="utf-8")
    if content.count(START) != 1 or content.count(END) != 1:
        print("FALHA: marcadores do índice estão ausentes ou duplicados")
        return 1
    start, end = content.index(START), content.index(END) + len(END)
    expected = render(catalog, extra, labels).rstrip("\n")
    existing = content[start:end]
    if args.check:
        if existing != expected:
            print("FALHA: índice do README não corresponde ao catálogo JSON; execute --write")
            return 1
        print(f"PASS: README sincronizado com {len(catalog)} fontes, {len(labels)} nichos e {len(extra)} URLs adicionais.")
        return 0
    content_path.write_text(content[:start] + expected + content[end:], encoding="utf-8")
    print("README atualizado preservando demais seções e rodapé.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
