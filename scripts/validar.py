#!/usr/bin/env python3
"""Validacao sem dependencias pagas: dados, nichos, evidencia e README."""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "FONTES/catalogo.csv"
JSON = ROOT / "FONTES/catalogo.json"
STATS = ROOT / "FONTES/ESTATISTICAS.json"
REQUIRED = (
    "id", "titulo", "descricao", "url", "nicho", "para_que_serve",
    "como_usar", "dica_pratica", "acesso", "freemium", "uso_comercial",
    "alerta", "fonte_termos", "status_verificacao", "origem", "data_referencia",
)


def validar():
    with CSV.open(encoding="utf-8-sig", newline="") as arquivo:
        reader = csv.DictReader(arquivo)
        linhas = list(reader)
        colunas = reader.fieldnames
    dados = json.loads(JSON.read_text(encoding="utf-8"))
    stats = json.loads(STATS.read_text(encoding="utf-8"))
    erros = []
    if colunas != list(REQUIRED):
        erros.append("Layout inesperado de colunas no CSV")
    if linhas != dados:
        erros.append("CSV e JSON nao apresentam exatamente os mesmos registros")
    if not linhas:
        erros.append("Catalogo vazio")
    ids, urls, contagens = set(), set(), {}
    for numero, entrada in enumerate(linhas, 2):
        ident = entrada.get("id", f"linha {numero}")
        for campo in REQUIRED:
            if campo not in entrada:
                erros.append(f"{ident}: coluna ausente: {campo}")
        for campo in ("id", "titulo", "descricao", "url", "nicho", "para_que_serve",
                      "como_usar", "dica_pratica", "acesso", "status_verificacao"):
            if not (entrada.get(campo) or "").strip():
                erros.append(f"{ident}: valor obrigatorio ausente: {campo}")
        if ident in ids:
            erros.append(f"ID duplicado: {ident}")
        ids.add(ident)
        url = entrada.get("url", "")
        normalized = url.lower().rstrip("/")
        if normalized in urls:
            erros.append(f"URL duplicada: {url}")
        urls.add(normalized)
        p = urlparse(url)
        if p.scheme != "https" or not p.netloc or p.username or p.password:
            erros.append(f"URL nao HTTPS ou com credencial: {url}")
        for campo in ("id", "titulo", "descricao", "para_que_serve", "como_usar", "dica_pratica"):
            if re.match(r"^\s*[=+@\-\t\r]", entrada.get(campo, "")):
                erros.append(f"Possivel CSV formula injection: {ident}.{campo}")
        nicho = entrada.get("nicho", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", nicho):
            erros.append(f"Nicho invalido: {nicho}")
        arquivo_nicho = ROOT / "FONTES" / "nichos" / f"{nicho}.md"
        if not arquivo_nicho.exists():
            erros.append(f"Nicho sem ficha: {nicho}")
        contagens[nicho] = contagens.get(nicho, 0) + 1
    if stats.get("total") != len(linhas):
        erros.append("Estatisticas totais divergem")
    if stats.get("nichos") != contagens:
        erros.append("Estatisticas dos nichos divergem")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if f"fontes-{len(linhas)}-" not in readme:
        erros.append("README possui contagem de fontes desatualizada")
    if f"nichos-{len(contagens)}-" not in readme:
        erros.append("README possui contagem de nichos desatualizada")
    for path in [
        "INDEX.md", "GOVERNANCA/MISSION-LOCK.md", "GOVERNANCA/MATRIZ-ACEITACAO.md",
        "GUIAS/00-TRILHA-DE-APRENDIZAGEM.md", "GUIAS/02-UV-TEXTURAS-PBR.md",
        "GUIAS/03-ANIMACAO-TRACKING.md", "GUIAS/04-WEBSITES-3D.md",
        "GUIAS/05-PIPELINE-EXPORTACAO.md", "EXEMPLOS/web-model-viewer.html",
    ]:
        if not (ROOT / path).exists():
            erros.append(f"Documento de base ausente: {path}")
    print(f"Fontes: {len(linhas)} | Nichos: {len(contagens)} | Inconsistencias: {len(erros)}")
    for problema in erros:
        print("FALHA:", problema)
    return not erros


if __name__ == "__main__":
    sys.exit(0 if validar() else 1)
