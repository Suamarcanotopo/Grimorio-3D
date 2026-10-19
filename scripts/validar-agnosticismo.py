#!/usr/bin/env python3
"""Coliseu documental: paridade e proveniência dos contratos multi-LLM.

Não executa APIs externas, não verifica carga automática de contextos e não
homologa a qualidade de respostas reais em Codex/Claude/Gemini/Grok.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = {"openai", "claude", "grok", "gemini"}
STATUSES = {"LIDO", "PRATICADO", "TESTADO", "HOMOLOGADO", "NÃO TESTADO", "BLOQUEADO"}
REQUIRED_DOCS = (
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "INTEROPERABILIDADE/CONTRATO-CANONICO.md",
    "INTEROPERABILIDADE/MATRIZ-PLATAFORMAS.md",
    "INTEROPERABILIDADE/PROMPT-PORTAVEL.md",
    "INTEROPERABILIDADE/contrato-resposta.json",
    "INTEROPERABILIDADE/EVALS/agnostico-casos.json",
)
REQUIRED_TERMS = (
    "Mission Lock", "fontes", "truque", "convenção", "NÃO TESTADO",
    "HOMOLOGADO", "licença", "privacidade", "teste", "rollback",
)

def txt(path):
    return (ROOT / path).read_text(encoding="utf-8")

def load(path):
    return json.loads(txt(path))

def main():
    errors = []
    for p in REQUIRED_DOCS:
        if not (ROOT / p).is_file():
            errors.append("Arquivo exigido inexistente: " + p)
    if errors:
        print("\n".join("FALHA: " + err for err in errors))
        return 1
    catalog = load("FONTES/catalogo.json")
    graph = load("APRENDER/mapa.json")["competencias"]
    source_ids = {row["id"] for row in catalog}
    stages = {row["id"] for row in graph}
    root = txt("README.md")
    agents = txt("AGENTS.md")
    claude = txt("CLAUDE.md")
    gemini = txt("GEMINI.md")
    core = txt("INTEROPERABILIDADE/CONTRATO-CANONICO.md")
    matrix = txt("INTEROPERABILIDADE/MATRIZ-PLATAFORMAS.md")
    prompt = txt("INTEROPERABILIDADE/PROMPT-PORTAVEL.md")
    response = load("INTEROPERABILIDADE/contrato-resposta.json")
    evals = load("INTEROPERABILIDADE/EVALS/agnostico-casos.json")
    if len(catalog) != 368 or len(stages) != 18:
        errors.append("Baseline de fontes ou competências mudou")
    for name, data, marker in (
        ("AGENTS.md", agents, "INTEROPERABILIDADE/CONTRATO-CANONICO.md"),
        ("CLAUDE.md", claude, "@INTEROPERABILIDADE/CONTRATO-CANONICO.md"),
        ("GEMINI.md", gemini, "@./INTEROPERABILIDADE/CONTRATO-CANONICO.md"),
    ):
        if marker not in data:
            errors.append(name + " não aponta ao núcleo canônico")
    if len(claude) > 2500 or len(gemini) > 2500:
        errors.append("Adaptador de plataforma ficou grande: risco de divergência")
    if "[Agnóstico" not in root or "INTEROPERABILIDADE/MATRIZ-PLATAFORMAS.md" not in root:
        errors.append("README sem acesso à compatibilidade entre provedores")
    for term in REQUIRED_TERMS:
        if term.lower() not in core.lower():
            errors.append("Contrato sem invariante: " + term)
    if "NOT_TESTED" not in matrix or "NOT_TESTED" not in prompt and "NÃO TESTADO" not in prompt:
        errors.append("Sem declaração explícita de testes pendentes")
    for provider in PROVIDERS:
        if provider not in matrix.lower():
            errors.append("Provedor não explicado na matriz: " + provider)
    if "Grok Build" not in matrix or "Claude Code" not in matrix or "Gemini CLI" not in matrix:
        errors.append("Matriz mistura chat com agentes de repositório")
    if evals.get("model_executions") != 0 or evals.get("provider_run_status") != "NOT_TESTED":
        errors.append("Há alegação não suportada de execução multi-LLM")
    cases = evals.get("cases", [])
    if len(cases) < 20:
        errors.append(f"Menos de 20 cenários: {len(cases)}")
    ids = set()
    for i, row in enumerate(cases, 1):
        cid = f"PA{i:02d}"
        if row.get("id") != cid or cid in ids:
            errors.append("ID de cenário repetido/desordenado: " + str(row.get("id")))
        ids.add(cid)
        if set(row.get("providers", [])) != PROVIDERS:
            errors.append(cid + ": provedores não equivalentes")
        if row.get("runtime_result") != "NOT_TESTED" or row.get("method") != "STATIC_EXPECTATIONS_ONLY":
            errors.append(cid + ": resultado estático indevidamente descrito como teste executado")
        if row.get("source_id") not in source_ids or row.get("stage") not in stages:
            errors.append(cid + ": fonte ou etapa inválida")
        if row.get("expected_status") not in STATUSES:
            errors.append(cid + ": estado de avaliação inválido")
        for field in ("title", "input", "expected_behavior", "forbidden_behavior", "expected_decision"):
            if len(str(row.get(field, "")).strip()) < (3 if field=="expected_decision" else 10):
                errors.append(cid + ": campo insuficiente " + field)
    props = response.get("properties", {})
    for key in response.get("required", []):
        if key not in props:
            errors.append("Schema de saída não define campo: " + key)
    if set(response.get("properties", {}).get("status", [])) != STATUSES:
        errors.append("Contrato de resposta diverge dos seis status canônicos")
    if len(response.get("examples", [])) < 1:
        errors.append("Contrato de resposta sem exemplo iniciante")
    for example in response.get("examples", []):
        if example.get("stage_id") not in stages:
            errors.append("Exemplo não usa etapa válida")
        if example.get("status") not in STATUSES:
            errors.append("Exemplo tem status desconhecido")
        for row in example.get("knowledge_sources", []):
            if row.get("source_id") not in source_ids:
                errors.append("Exemplo usa fonte não canônica")
    for file in [
        "GOVERNANCA/MISSION-LOCK.md",
        "FONTES/catalogo.json",
        "APRENDER/mapa.json",
        "INTEROPERABILIDADE/MATRIZ-PLATAFORMAS.md",
        "INTEROPERABILIDADE/PROMPT-PORTAVEL.md",
    ]:
        if not (ROOT / file).exists():
            errors.append("Referência canônica inexistente: " + file)
    workflow = txt(".github/workflows/validar-catalogo.yml")
    if "scripts/validar-agnosticismo.py" not in workflow or "'INTEROPERABILIDADE/**'" not in workflow:
        errors.append("CI não executa verificador agnóstico quando documentação muda")
    print(
        f"Interoperabilidade documental: 4 provedores, {len(cases)} cenários estáticos, "
        f"{len(catalog)} fontes, {len(graph)} competências. "
        f"Execuções reais de LLM: 0 (NOT_TESTED). Erros: {len(errors)}"
    )
    for error in errors:
        print("FALHA:", error)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
