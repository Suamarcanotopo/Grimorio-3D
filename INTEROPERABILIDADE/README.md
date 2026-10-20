# Grimório 3D interoperável — começar por aqui

O Grimório não pertence a um modelo de IA. A **informação é a mesma** para OpenAI, Claude, Grok e Gemini; mudam as ferramentas e a forma de colocar o projeto no contexto.

## O que fazer

1. **Uso pelo navegador, sem coding agent:** copie o [prompt portátil](PROMPT-PORTAVEL.md) e compartilhe o [contrato canônico](CONTRATO-CANONICO.md) e apenas os documentos necessários à tarefa; explique se não tiver dado acesso ao repositório.
2. **OpenAI Codex:** trabalhe no repositório; o arquivo `AGENTS.md` aponta ao contrato. Ferramentas, permissões e limites são próprios da instalação.
3. **Claude Code:** o `CLAUDE.md` importa o mesmo contrato; confirme se o arquivo foi carregado antes de seguir.
4. **Gemini CLI:** o `GEMINI.md` importa o mesmo contrato; confirme o contexto no CLI antes de seguir.
5. **Grok Build:** o `AGENTS.md` é o ponto de entrada previsto na documentação; ele pode carregar `CLAUDE.md` adicionalmente, mas os dois remetem à mesma fonte. Se utilizar apenas Grok chat/API, passe o contexto explicitamente.
6. **Verificação:** siga o [estudo portátil do primeiro projeto](PRIMEIRO-PROJETO-PORTAVEL.md) e os [casos comparáveis](EVALS/agnostico-casos.json); marque `NOT_TESTED` onde não foi executado.

## Homologação operacional (separada da compatibilidade documental)

[Status auditado de execução real](STATUS-EXECUCAO.md) · [Rubrica Coliseu](RUBRICA-REVISAO.md) · [Workflow GitHub Actions sob autorização](../.github/workflows/avaliar-llms-reais.yml).

Um mock ou dry-run **não é resposta de nenhum provedor**. Resultados válidos exigem ID fornecido pela API, hash dos prompts e revisão semântica.

## Documentos principais

- [Contrato único de comportamento](CONTRATO-CANONICO.md)
- [Matriz por provedor e ambiente](MATRIZ-PLATAFORMAS.md)
- [Prompt para copiar em qualquer chat](PROMPT-PORTAVEL.md)
- [Exercício guiado independente de IA](PRIMEIRO-PROJETO-PORTAVEL.md)
- [Contrato opcional de resposta estruturada](contrato-resposta.json)
- [20 casos de avaliação](EVALS/agnostico-casos.json)
- [Mission Lock](../GOVERNANCA/MISSION-LOCK.md)
- [Academia/APRENDER](../APRENDER/README.md)

**Importante:** portabilidade de documentação não significa que uma UI de chat consiga modificar GitHub, executar Blender, instalar um plugin ou compartilhar memória com outro modelo. Isso depende de acesso, ferramentas e aprovação, e os quatro modelos não foram submetidos a testes de execução nesta etapa.

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Dicas e Tutoriais](https://chat.whatsapp.com/F11omHqfI4KKCC0Sgbc4Vm?s=cl&p=i&mlu=4&ilr=4) · [Working Lab](https://chat.whatsapp.com/FcyMOdQqyW8Ci104P8i3Gg?s=cl&p=i&mlu=4&ilr=4) · [Comunidade 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Deixe uma estrela no Grimório.
