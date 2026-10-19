# Primeiro projeto 3D — execução portátil entre IAs

**Proposta:** um objeto autoral modelado no Blender, com material, UV, exportação GLB e visualização no navegador. Uma IA pode orientar; o sucesso depende de Blender e navegador realmente executados.

## Uma mesma pergunta, quatro provedores

Use o [prompt portátil](PROMPT-PORTAVEL.md) com a tarefa: *"Oriente um iniciante a criar um cubo 3D com pivô correto, UV, material PBR, exportar GLB e publicar em model-viewer. Explique convenções, truques, erros, evidência e status; não finja executar ferramentas."*

Seus dados de entrada devem ser **iguais**: contrato, versão do repositório, estágio do aluno, ambiente e limitações. Anote data, versão de modelo e se a IA tinha acesso aos mesmos arquivos. Não compare qualidade com entradas divergentes.

## Caminho didático comum

| Passo | O que ler e aplicar | Convenção/truque | Evidência real |
|---|---|---|---|
| 1 · Briefing E01 | [APRENDER](../APRENDER/README.md) | Defina dimensões, público, dispositivo e objetivo antes do software | Brief em PT-BR |
| 2 · Escala E04 | [Tutorial 01 Blender](../TUTORIAIS/01-blender-primeiro-objeto-completo.md) | Escolha metros/unidade, pivô no ponto funcional | Cena editável, medidas |
| 3 · UV/PBR E06 | [Tutorial 02](../TUTORIAIS/02-blender-texturizacao-pbr-com-uv.md), [Khronos](../FONTES/nichos/pipeline-padroes.md) | Checker UV sem estiramento; cores sRGB e dados non-color quando aplicável | Captura de UV e material |
| 4 · Export E15 | [Validar GLB](../TUTORIAIS/36-gltf-validate-otimizar-ktx2.md) | Preserve arquivo nativo; valide glTF; não assuma portabilidade de shaders | BLEND, GLB, relatório |
| 5 · Web E16 | [Tutorial 08 Web3D](../TUTORIAIS/08-website-produto-3d-com-modelviewer.md) | Poster e CTA acessível mesmo sem 3D; teste em celular real | Screenshot/site e erros |
| 6 · Governança E17/E18 | [Caderno de provas](../APRENDER/CADERNO-DE-PROVAS.md) | Direitos por item, comparação antes/depois, rollback | Formulário preenchido |

## Teste de paridade — cinco perguntas

1. A IA identificou claramente **onde termina sua orientação e começa a execução real**?
2. Ela preservou os mesmos IDs, Mission Lock, fonte primária e direito de cada asset?
3. Mostrou, em português, convenção, dica e erro, **não apenas lista de links**?
4. Descreveu teste de aceite adequado ao software e dispositivo sem inventar resultado?
5. Recomendou próximo passo coerente com o nível do aluno e uma única meta de cada vez?

## Registro de verificação por provedor

| Provedor | Contexto carregado? | Resposta comparada? | Teste Blender/Web? | Status |
|---|---|---|---|---|
| OpenAI/Codex ou ChatGPT | Não observado nesta auditoria | Não | Não | `NOT_TESTED` |
| Claude/Claude Code | Não observado nesta auditoria | Não | Não | `NOT_TESTED` |
| Gemini/Gemini CLI | Não observado nesta auditoria | Não | Não | `NOT_TESTED` |
| Grok/Grok Build | Não observado nesta auditoria | Não | Não | `NOT_TESTED` |

**Como documentar:** quando rodar de verdade, anote prompt exato, modelo/versão, timestamp, ferramentas, trechos fornecidos, saída, criticidade das divergências e revisores. Só altere o status com evidência.

**Coliseu:** se qualquer IA inventar licença, declarar execução sem ferramenta ou substituir o Mission Lock, classifique **REJECT** e corrija contexto/instruções antes de avançar.

---

[Voltar ao índice portátil](README.md) · [Casos adversariais](EVALS/agnostico-casos.json) · [Contrato de saída](contrato-resposta.json)

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5).
