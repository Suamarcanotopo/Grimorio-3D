#!/usr/bin/env python3
"""Gates adicionais de conhecimento ECP/Coliseu; não testa licenças nem hardware."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCS = [
    "CURRICULO/README.md",
    "CURRICULO/ETAPAS-DA-PRODUCAO.md",
    "CURRICULO/CONTRATOS-DE-ENTREGA.md",
    "NICHOS/README.md",
    "ECOSSISTEMA/README.md",
    "ATUALIDADES/README.md",
    "ATUALIDADES/BOLETIM-2026-10-16.md",
    "SKILLS/README.md",
    "SKILLS/CONTRATO-DE-SKILL-3D.md",
    "GOVERNANCA/ECP-COLISEU-2026-10-16.md",
    "GOVERNANCA/FONTES-ATEMPORAIS-E-ATUAIS.md",
    "DEPENDENCIAS/REGISTRO-TRANSVERSAL-3D.md",
    "FAQ/PERGUNTAS-POR-MERCADO.md",
]
NICHES = [
    "publicidade-marketing", "cinema-vfx", "animacao-storytelling",
    "games-level-design", "ar-xr", "web3d-commerce",
    "arquitetura-industria", "educacao-pesquisa",
    "ambientes-procedurais", "ia-captura",
]
FIELDS = ("id", "titulo", "descricao", "url", "nicho", "para_que_serve",
          "como_usar", "dica_pratica", "acesso", "uso_comercial", "status_verificacao")


def load(rel):
    path = ROOT / rel
    if not path.exists():
        raise ValueError(f"Arquivo obrigatório ausente: {rel}")
    return path.read_text(encoding="utf-8")


def main():
    errs = []
    for doc in REQUIRED_DOCS:
        try:
            load(doc)
        except ValueError as e:
            errs.append(str(e))
    catalog = json.loads(load("FONTES/catalogo.json"))
    stats = json.loads(load("FONTES/ESTATISTICAS.json"))
    if len(catalog) != stats.get("total") or len(catalog) < 238:
        errs.append("Quantidade do catálogo ou baseline de 238 incorreto")
    keys = set()
    urls = set()
    seen_niches = {}
    for row in catalog:
        for k in FIELDS:
            if not str(row.get(k, "")).strip():
                errs.append(f"Campo {k} ausente em {row.get('id')}")
        rid = row.get("id", "")
        if rid in keys:
            errs.append(f"ID duplicado: {rid}")
        keys.add(rid)
        url = row.get("url", "").strip().lower().rstrip("/")
        if url in urls:
            errs.append(f"URL duplicada: {url}")
        urls.add(url)
        seen_niches[row.get("nicho")] = seen_niches.get(row.get("nicho"), 0) + 1
    for i in range(1, 209):
        if f"SIN3D-{i:03d}" not in keys:
            errs.append(f"Baseline removida: SIN3D-{i:03d}")
    if len(seen_niches) < 38 or seen_niches != stats.get("nichos"):
        errs.append("Nichos antigos e novos ou estatísticas divergentes")
    for slug in NICHES:
        body = load(f"NICHOS/{slug}.md")
        for token in ("Como fazer", "Como validar", "Onde aprender", "Erro grave"):
            if token not in body:
                errs.append(f"Nicho sem seção: {slug}/{token}")
    curriculum = load("CURRICULO/ETAPAS-DA-PRODUCAO.md")
    stages = re.findall(r"^## \d{2} — ", curriculum, re.M)
    if len(stages) != 18:
        errs.append(f"Currículo tem {len(stages)} etapas; esperado 18")
    world = load("ECOSSISTEMA/README.md")
    regional = re.findall(r"^### .+ — .+$", world, re.M)
    if len(regional) < 19:
        errs.append(f"Fontes internacionais regionais insuficientes: {len(regional)}")
    if not all(x in world for x in ["Canadá", "Oceania", "Índia", "Rússia", "Oriente Médio"]):
        errs.append("Cobertura geográfica solicitada incompleta")
    cases = json.loads(load("SKILLS/casos-red-team.json")).get("cases", [])
    if len(cases) < 16:
        errs.append(f"Casos red team insuficientes: {len(cases)}")
    for c in cases:
        if not c.get("input") or not c.get("expected") or not c.get("id"):
            errs.append(f"Caso incompleto: {c}")
    readme = load("README.md")
    for dest in ["CURRICULO/ETAPAS-DA-PRODUCAO.md", "NICHOS/README.md",
                 "ECOSSISTEMA/README.md", "SKILLS/README.md",
                 "ATUALIDADES/README.md", "GOVERNANCA/ECP-COLISEU-2026-10-16.md"]:
        if dest not in readme:
            errs.append(f"README sem navegação: {dest}")
    if f"fontes-{len(catalog)}-" not in readme:
        errs.append("Badge catálogo README desatualizado")
    if "Meta Spark" not in readme or "Mission Lock" not in readme:
        errs.append("README omitiu proteção histórica/mission lock")
    print(f"ECP: {len(catalog)} fontes, {len(seen_niches)} nichos, "
          f"{len(stages)} etapas, {len(NICHES)} trilhas, "
          f"{len(regional)} fontes regionais, {len(cases)} casos red team; "
          f"falhas={len(errs)}")
    for e in errs:
        print("FALHA:", e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
