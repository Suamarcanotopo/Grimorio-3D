# Auditoria de execução real — quatro provedores

**Data de auditoria:** 20/10/2026 · **Escopo:** enviar os mesmos 20 cenários a APIs OpenAI, Anthropic, Google Gemini e xAI Grok e obter evidências com ID de resposta.

## Acesso verificado nesta sessão

| Provedor | Acesso nesta execução | Resultado |
|---|---|---|
| OpenAI | Modelo GPT-6 desta conversa responde; não há canal de chamada independente à API OpenAI neste runtime | API: NOT_TESTED |
| Claude | Havia abas abertas no navegador conectado, mas a ferramenta acessível permite leitura, não controle; nenhuma sessão autenticada de automação externa confirmada | API: NOT_TESTED |
| Gemini | Sem cliente/API autenticado acessível para invocação nesta sessão | API: NOT_TESTED |
| Grok | Sem cliente/API autenticado acessível para invocação nesta sessão | API: NOT_TESTED |

A conta GitHub permite criar branches/PRs, mas não permite inspecionar metadados de GitHub Actions Secrets por esta conexão. **Não afirmamos que os quatro segredos estão ausentes do repositório**; somente que não estão disponíveis como credenciais para uma chamada nesta sessão.

**Chamadas comprovadas:** 0 de 4 provedores. **Execuções semânticas homologadas:** 0. Os testes locais com mocks e o dry-run não contam como execuções reais.

## O que já está pronto para execução

- Cliente HTTP Python padrão: [executar-avaliacoes-llm.py](../scripts/executar-avaliacoes-llm.py).
- Workflow exclusivamente manual: [avaliar-llms-reais.yml](../.github/workflows/avaliar-llms-reais.yml).
- Casos canônicos: [20 testes adversariais](EVALS/agnostico-casos.json).
- [Rubrica para revisar respostas verdadeiras](RUBRICA-REVISAO.md).
- Status de cada tentativa: NOT_EXECUTED, BLOCKED_NO_CREDENTIALS, BLOCKED_NO_MODEL, API_ERROR, INVALID_API_RESPONSE, API_RESPONSE_RECEIVED.
- A ocorrência de API_RESPONSE_RECEIVED comprova apenas que a API retornou ID e texto. **Não significa que o modelo obedeceu ao Mission Lock**.

## Executar no GitHub de modo seguro

1. Abra o repositório → **Settings → Secrets and variables → Actions**.
2. Cadastre cada chave como **Repository secret**: OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, XAI_API_KEY. Não cole chaves em chats, issues, commits, artefatos nem logs.
3. Consulte os catálogos oficiais de modelos e anote os quatro IDs vigentes. **Não há modelos fictícios fixados por padrão.**
4. Abra **Actions → Testar APIs LLM reais (execucao manual e paga) → Run workflow**; confirme autorização de chamadas pagas, selecione os provedores e comece com 1 caso por modelo.
5. Escolha IDs reais de modelos; execute. O workflow rejeitará falta de credenciais, modelo ou resposta. Baixe o artefato RESULTADOS/RESUMO/SHA256 para auditar os request IDs sem expor segredos.
6. Revise as saídas segundo [rubrica](RUBRICA-REVISAO.md), registrando falhas. Só então faça 4 casos e, posteriormente, 20 por modelo (80 chamadas no total).

**Custos e segurança:** chamadas são faturadas pelos provedores conforme os planos de API, independentemente de assinaturas de chat. O workflow exige autorização explícita, não roda a cada PR/push e não cria segredos. Artefatos podem ter respostas em texto e seguir as permissões de acesso do repositório; use apenas os casos públicos de teste incluídos.

## Executar localmente (somente no ambiente com acesso e chaves)

Faça teste sem rede (nunca é aprovação):

    python3 -m unittest discover -s scripts -p testar_avaliacoes_llm.py
    python3 scripts/executar-avaliacoes-llm.py --max-cases 4 --out resultados-secos

Para chamadas reais, configure os quatro secrets no ambiente local sem exibi-los e também os IDs MODEL_OPENAI, MODEL_ANTHROPIC, MODEL_GEMINI, MODEL_XAI. Depois use:

    python3 scripts/executar-avaliacoes-llm.py --execute --approve-spend --max-cases 1 --out resultados-reais

**Recusa de downgrade:** nenhuma evidência produzida por mocks ou modo dry-run pode preencher campos de teste real. Nenhuma avaliação de texto dispensa testes de ferramentas e dispositivos, quando aplicável.
