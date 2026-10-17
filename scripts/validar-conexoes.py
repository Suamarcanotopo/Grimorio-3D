#!/usr/bin/env python3
"""ECP+Coliseu: auditoria das relações didáticas entre fontes, termos, FAQ e prática.

Somente biblioteca padrão. NÃO executa Blender, SDKs ou HTML; não confirma licenças.
"""
from collections import Counter, defaultdict
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def load(path):
    return json.loads(read(path))

def main():
    errors = []
    graph = load("APRENDER/mapa.json")["competencias"]
    routes = load("APRENDER/rotas.json")["trilhas"]
    glossary = load("APRENDER/indice-glossario.json")["entries"]
    questions = load("APRENDER/indice-faq-01-10.json")["entries"] + load("APRENDER/indice-faq-11-mercado.json")["entries"]
    catalog = load("FONTES/catalogo.json")
    names = {r["id"]: r for r in catalog}
    cats = {r["nicho"] for r in catalog}
    nodes = {n["id"]: n for n in graph}
    qfiles = {f"FAQ/{p.name}" for p in (ROOT / "FAQ").glob("[0-9]*.md")}
    gfiles = {f"GLOSSARIO/{p.name}" for p in (ROOT / "GLOSSARIO").glob("[0-9]*.md")}
    tpaths = {p.name[:2]: f"TUTORIAIS/{p.name}" for p in (ROOT / "TUTORIAIS").glob("[0-9]*.md")}
    dpaths = {p.name[:2]: f"EXEMPLOS/{p.name}" for p in (ROOT / "EXEMPLOS").glob("[0-9]*.html")}

    if len(graph) != 18 or list(nodes) != [f"E{i:02d}" for i in range(1, 19)]:
        errors.append("Esperadas 18 etapas ordenadas E01...E18")
    if len(catalog) != 368 or len(cats) != 38:
        errors.append("Baseline original de 368 fontes e 38 nichos foi alterado")
    if len(gfiles) != 15 or len(qfiles) != 18 or len(tpaths) != 37 or len(dpaths) != 10:
        errors.append("Módulos originais removidos ou renomeados")
    used = {"nicho": set(), "glossario": set(), "faq": set(), "tutoriais": set(), "demonstracoes": set()}
    for i, stage in enumerate(graph):
        ident = stage["id"]
        for field in ("titulo", "entregavel", "como_fazer", "convencao", "truque", "erro", "criterio"):
            if len(str(stage.get(field, "")).strip()) < 35:
                errors.append(f"{ident}: didática insuficiente em {field}")
        for pre in stage["pre_requisitos"]:
            if pre not in nodes or int(pre[1:]) >= i+1:
                errors.append(f"{ident}: pré-requisito inexistente/futuro {pre}")
        for key, valid in [("glossario", gfiles), ("faq", qfiles)]:
            for link in stage[key]:
                used[key].add(link)
                if link not in valid:
                    errors.append(f"{ident}: {key} inexistente: {link}")
        for kind, existing in [("tutoriais", tpaths), ("demonstracoes", dpaths)]:
            for identifier in stage[kind]:
                used[kind].add(identifier)
                if identifier not in existing:
                    errors.append(f"{ident}: {kind} inexistente: {identifier}")
        for category in stage["nicho_fontes"]:
            used["nicho"].add(category)
            if category not in cats:
                errors.append(f"{ident}: nicho de fonte inexistente: {category}")
            elif not (ROOT / "FONTES/nichos" / (category+".md")).exists():
                errors.append(f"{ident}: ficha de nicho ausente: {category}")
        for source_id in stage["fontes"]:
            if source_id not in names:
                errors.append(f"{ident}: fonte ID inexistente {source_id}")
            elif not names[source_id]["url"].startswith("https://"):
                errors.append(f"{ident}: fonte não HTTPS {source_id}")
        if not stage["glossario"] or not stage["faq"] or not stage["fontes"] or not stage["tutoriais"]:
            errors.append(f"{ident}: faltam ligações de aprendizado essenciais")
    for name, all_ids in [
        ("nicho", cats), ("glossario", gfiles), ("faq", qfiles),
        ("tutoriais", set(tpaths)), ("demonstracoes", set(dpaths)),
    ]:
        missing = all_ids-used[name]
        if missing:
            errors.append(f"{name}: sem rota a partir de competência: {sorted(missing)}")
    # Cada uma das 368 fontes precisa aparecer por meio do seu nicho canônico,
    # sem criar cópias de URL, IDs ou dados de licença no grafo.
    unassigned_sources = [x["id"] for x in catalog if x["nicho"] not in used["nicho"]]
    if unassigned_sources:
        errors.append(f"Fontes órfãs: {unassigned_sources}")
    if len(glossary) != 293 or len(questions) != 210:
        errors.append(f"Índice individual difere do baseline: {len(glossary)} + {len(questions)}")
    original_cache = {}
    seen = set()
    for letter, rows in [("G", glossary), ("Q", questions)]:
        for number, row in enumerate(rows, 1):
            label = f"{letter}{number:03d}"
            if row.get("id") != label or label in seen:
                errors.append(f"ID de roteamento repetido/desordenado: {row.get('id')} / {label}")
            seen.add(label)
            cap = row.get("capitulo", "")
            if not (ROOT / cap).exists():
                errors.append(f"Capítulo original inexistente: {cap}")
                continue
            data = original_cache.setdefault(cap, read(cap))
            level = "###" if letter == "G" else "##"
            expression = rf"^{level} {row['numero']}\. {re.escape(row['titulo'])}$"
            if not re.search(expression, data, re.M):
                errors.append(f"Índice aponta título que não existe: {label} / {cap}")
            route = nodes.get(row.get("etapa"))
            if not route:
                errors.append(f"{label}: etapa primária inválida")
            elif cap.startswith("GLOSSARIO") and cap not in route["glossario"]:
                errors.append(f"{label}: etapa não referencia capítulo do glossário")
            elif cap.startswith("FAQ/") and cap != "FAQ/PERGUNTAS-POR-MERCADO.md" and cap not in route["faq"]:
                errors.append(f"{label}: etapa não referencia capítulo do FAQ")
    markdown_index = read("APRENDER/INDICE-INDIVIDUAL.md")
    for row in glossary+questions:
        if f"**{row['id']}**" not in markdown_index:
            errors.append(f"Entrada ausente do índice de navegação: {row['id']}")
    if len(routes) != 10 or {r["nicho"] for r in routes} != {
        p.stem for p in (ROOT / "NICHOS").glob("*.md") if p.name != "README.md"
    }:
        errors.append("Dez trilhas profissionais não correspondem às páginas NICHOS")
    for r in routes:
        if r.get("etapas", [None])[0] != "E01" or "E18" not in r.get("etapas", []):
            errors.append(f"{r['nicho']}: falta briefing ou conclusão")
        for id_ in r["etapas"]:
            if id_ not in nodes:
                errors.append(f"{r['nicho']}: etapa inexistente {id_}")
        for id_ in r["tutoriais"]:
            if id_ not in tpaths:
                errors.append(f"{r['nicho']}: tutorial inexistente {id_}")
            elif not any(id_ in nodes[s]["tutoriais"] for s in r["etapas"]):
                errors.append(f"{r['nicho']}: tutorial fora das competências da rota {id_}")
        for id_ in r["demos"]:
            if id_ not in dpaths:
                errors.append(f"{r['nicho']}: demo inexistente {id_}")
        for field in ("objetivo", "projeto_final", "truque", "erro"):
            if len(r[field]) < 30:
                errors.append(f"{r['nicho']}: {field} pouco detalhado")
    for name in [
        "README.md", "ETAPAS-CONECTADAS.md", "ROTAS-POR-MERCADO.md",
        "INDICE-INDIVIDUAL.md", "CONVENCOES-E-TRUQUES.md", "CADERNO-DE-PROVAS.md",
    ]:
        if not (ROOT / "APRENDER" / name).exists():
            errors.append("Índice didático inexistente: "+name)
    root = read("README.md")
    if "[APRENDER]" not in root or "APRENDER/README.md" not in root:
        errors.append("README não apresenta o novo ponto de entrada")
    if "sistemaimersivonarrativo.com.br" not in root or "FcyMOdQqyW8Ci104P8i3Gg" not in root:
        errors.append("Rodapé SIN original alterado")
    print(f"ECP/Coliseu: {len(graph)} competências, {len(cats)} nichos/"
          f"{len(catalog)} fontes, {len(glossary)} termos, {len(questions)} FAQ, "
          f"{len(tpaths)} tutoriais, {len(dpaths)} demos, {len(routes)} rotas, falhas={len(errors)}")
    for error in errors[:50]:
        print("FALHA:", error)
    if len(errors) > 50:
        print(f"... {len(errors)-50} outros erros")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
