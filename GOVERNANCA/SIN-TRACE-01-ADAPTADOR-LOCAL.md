# SIN-TRACE-01 — adaptador local de rastreabilidade e comunicação

**Estado:** CANDIDATE — somente neste PR, sem editar material autoral, sem aprovação implícita nem alteração de outros repositórios.  
**Missão federada:** `SIN-TRACE-4HOUSES-20261102`. **Casa:** `Suamarcanotopo/Grimorio-3D`.

Este documento consome por ponte o [contrato SIN-TRACE-01 do Grimório de Skills](https://github.com/Suamarcanotopo/grimorio-skills/blob/main/GOVERNANCA/SIN-TRACE-01-CONTRATO-FEDERADO.md) **quando aprovado e integrado**. Até lá, conferir também o PR candidato de origem. A Constituição local e [Mission Lock](../GOVERNANCA/MISSION-LOCK.md) prevalecem em conflitos.

## Atribuição de autoridade

**OWNER local:** Conhecimento de 3D, fontes, tutoriais, render, XR, formatos e licenças individuais. ECP seleciona as skills pertinentes, Governance Guard preserva limites, SEE só governa evolução de Skills na sua casa, COLISEUM revisa evidência e risco, GitHub Flow dá rastreabilidade Git. Nenhum desses nomes concede acesso a ferramentas nem significa execução. Conectar os outros Grimórios por `bridges` no manifesto, nunca copiando conteúdo como se fosse fonte original.

## Para cada mudança: fluxo obrigatório

1. Consultar `AGENTS.md`, README, Constituição, Mission Lock, catálogo integral e PRs ativos.
2. Identificar o arquivo/ID canônico e owner; verificar se já existe conteúdo relacionado.
3. Fazer alterações em branch de curta duração; preservar arquivos/IDs/origens/restrições vigentes.
4. Criar `GOVERNANCA/RASTREABILIDADE/changes/<ID>.json` que cobre **todos** os arquivos do PR e documenta `mission_id`, `repository`, `base_sha`, `owner`, `risk`, `state`, `changed_paths`, `tests`, `rollback`, `handoff`, `bridges`.
5. Atualizar `CATALOGO-TOTAL-ARQUIVOS.md` para novos caminhos, e mapa didático/índices de domínio quando a navegação mudar.
6. Declarar ponte a outras casas com destino e estado, **sem mutação automática** do destino.
7. Executar `python3 scripts/validar-rastreabilidade-sin.py --repo Suamarcanotopo/Grimorio-3D` (em CI de PR), `python3 scripts/validar-indice-total.py` e testes próprios deste repositório.
8. Na revisão, COLISEUM contesta origem, OWNER omitido, links quebrados, duplicação, regressão, direitos, falsa alegação de teste e ausência de handoff.

**Downside protegido:** os registros são versionados, e descartar este PR preserva a biblioteca anterior. O índice garante localização dos arquivos **que foram versionados e incluídos na verificação**, não de anexos externos ou alterações locais não enviadas ao Git.

## Handoff para outras Skills/casas

Referência única de missão: `SIN-TRACE-4HOUSES-20261102`; cada casa registra seu PR, SHA, testes e próximo responsável. Revisor pode consultar as pontes para decidir atualização em outra casa, mas não declarar automaticamente que outro agente já leu ou executou o handoff.

**Pendências:** integração com o índice de OWNERs no PR #90 e Pantheon Connect PR #55; homologação em cada runtime; proteção real de `main` (não está comprovada). 
