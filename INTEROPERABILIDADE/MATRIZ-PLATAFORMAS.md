# Matriz de compatibilidade — OpenAI, Claude, Gemini e Grok

**Objetivo:** a mesma semântica, as mesmas fontes e os mesmos gates; *não* os mesmos nomes de ferramentas ou carregadores. Atualização técnica: outubro de 2026. Verifique documentação oficial novamente ao atualizar as plataformas.

| Ambiente | Entrada recomendada | Como usar | Status |
|---|---|---|---|
| OpenAI **Codex CLI/IDE** | `AGENTS.md` → [contrato](CONTRATO-CANONICO.md) | Abra o repositório; leia só as fontes necessárias à tarefa; respeite permissões e ordem de instruções | Arquivo reconhecido/documentado; execução nessa instalação: **NOT_TESTED** |
| **ChatGPT web** | [prompt portátil](PROMPT-PORTAVEL.md) com anexos/arquivos ou acesso autorizado | Cole o prompt e disponibilize os documentos relevantes; não assumir descoberta automática de `AGENTS.md` | Uso manual; execução cruzada: **NOT_TESTED** |
| **Claude Code** | `CLAUDE.md` com import `@INTEROPERABILIDADE/CONTRATO-CANONICO.md` | Abra o repositório no Claude Code e confirme o contexto realmente carregado | Entrada documentada; teste nesta sessão: **NOT_TESTED** |
| **Claude chat/web** | [prompt portátil](PROMPT-PORTAVEL.md) + documentos | Envie o material ou conecte o repositório com autorização | Carregamento manual/contextual; teste: **NOT_TESTED** |
| **Gemini CLI** | `GEMINI.md` com import `@./INTEROPERABILIDADE/CONTRATO-CANONICO.md` | Abra repositório e confira os arquivos reconhecidos pelo mecanismo de contexto | Entrada documentada; teste nesta sessão: **NOT_TESTED** |
| **Gemini web / AI Studio** | [prompt portátil](PROMPT-PORTAVEL.md) + arquivos | Anexe ou disponibilize os arquivos de forma explícita | Carregamento manual/contextual; teste: **NOT_TESTED** |
| **Grok Build, ambiente de código** | `AGENTS.md` | O projeto Grok Build documenta descoberta de regras do projeto; **pode também ler `CLAUDE.md`**. Não criar instruções divergentes em arquivos paralelos | Entrada documentada no projeto; teste nesta sessão: **NOT_TESTED** |
| **Grok chat/API** | [prompt portátil](PROMPT-PORTAVEL.md) + conteúdo do repositório | Passe contexto via mensagens/arquivos conforme API/produto; verifique políticas, permissões e ferramentas | Sem auto-leitura universal de arquivos locais; teste: **NOT_TESTED** |

## Fontes oficiais de convenções de projeto

- OpenAI: <https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex> — uso do `AGENTS.md`.
- Anthropic: <https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts> — `CLAUDE.md`.
- Gemini CLI: <https://geminicli.com/docs/cli/gemini-md/> — `GEMINI.md` e imports.
- Grok Build: <https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/12-project-rules.md> — regras de projeto; é necessário observar versão/ambiente.
- xAI Grok API: <https://docs.x.ai/developers/model-capabilities/text/generate-text> — mensagens, contexto e API.

## Prioridade e duplicação

`AGENTS.md`, `CLAUDE.md` e `GEMINI.md` são **adaptadores de carregamento**; `INTEROPERABILIDADE/CONTRATO-CANONICO.md` é o **núcleo comum**, e `GOVERNANCA/MISSION-LOCK.md` é a referência de invariantes do projeto. Em conflito, interrompa modificações e relate a divergência; as instruções superiores de segurança e permissão do ambiente prevalecem.

O Grok Build pode carregar mais de um desses arquivos: esse comportamento não autoriza multiplicar responsabilidades ou criar mensagens incompatíveis. O conteúdo auxiliar do Claude/Gemini é propositalmente curto.

## O que NÃO foi homologado

- Não executamos quatro modelos via API nem criamos credenciais.
- Não validamos chamadas de ferramenta, limite de contexto, custo, consistência semântica ou qualidade de assets produzidos em cada provedor.
- A CI avalia **contratos, referências e cenários esperados**, não respostas geradas pelas quatro IAs.
- Imagens, GLB, vídeos, hardware VR/MR, Lens Studio e Effect House exigem testes reais específicos; não tratar `NOT_TESTED` como `PASS`.

## Sequência para homologação futura (manual e reversível)

1. Selecione **a mesma versão do repositório**, o mesmo prompt e os mesmos trechos de fonte para cada modelo.
2. Execute os casos em `EVALS/agnostico-casos.json` em ambientes autorizados e anote versões, ferramentas e permissões.
3. Avalie cada resposta pelos invariantes (IDs corretos, didática, licença, não alegar execução, uso de ferramentas).
4. Registre evidências por provedor. Faça uma comparação justa e documente diferenças sem inventar notas.
5. Corrija uma divergência por vez; use branch, regressão, PR e rollback.
