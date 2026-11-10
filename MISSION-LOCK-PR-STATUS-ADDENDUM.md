# Adendo de Mission Lock — ML-PR-STATUS-01

<!-- SIN-PR-STATUS-ML-ADDENDUM-V1 -->
Versão: 1.0 — 2026-11-10
Repositório: Suamarcanotopo/Grimorio-3D
Origem da proposta: 868f72e3b7c7231cb7133bd974d904e3dcad8822
Mission Lock canônico identificado: GOVERNANCA/MISSION-LOCK.md
Fonte de referência transversal: https://github.com/Suamarcanotopo/grimorio-skills/issues/118

## 1. Regra obrigatória antes de cada missão
Ler AGENTS.md, o Mission Lock aplicável e este adendo. Consultar o último checkpoint, estado real da PR e HEAD. Se o HEAD não mudou, NÃO reler todo o repositório: conferir CI, decisões, testes, instalação e bloqueios. Se mudou, analisar somente o delta afetado e suas dependências; abrir arquivos completos quando a precisão exigir. Nunca exigir que o usuário repita contexto já documentado nem iniciar uma implementação duplicada.

## 2. Estado em cinco eixos independentes
- GITHUB: NO_PR / DRAFT / OPEN_REVIEW / MERGED / CLOSED_UNMERGED.
- IMPLEMENTACAO: NOT_STARTED / IMPLEMENTING / CODE_READY / WAITING_TEST / BLOCKED / DONE_WITH_EVIDENCE.
- QUALIDADE: NOT_RUN / FAIL / PARTIAL / RETEST / PASS / INDEPENDENT_ACCEPT.
- APLICACAO: BRANCH_ONLY / MERGED_MAIN / HOST_INSTALLED_VERIFIED / PRODUCTION_HOMOLOGATED.
- OPERACAO: PLANNED / EXECUTED_VERIFIED / ROLLED_BACK / UNKNOWN.

Invariante: COMMIT != PR != MERGE != INSTALACAO != HOMOLOGACAO. Documentação escrita não prova runtime; uma PR Draft não está aplicada na branch principal. Aprovação Coliseum independente exige rastreio verificável e não pode ser autoatribuída.

## 3. Registro incremental (PR/Issue canônica)
Em cada atualização anotar: work_id, PR e URL, issue, branch, owner, HEAD anterior/novo, caminhos alterados, objetivo, escopo bloqueado, estados cinco eixos, CI com URL, testes executados com prova, artefatos e hashes, ambiente de instalação, falhas e riscos, correções propostas, próximo passo, decisão humana e rollback. Atualizar o registro EXISTENTE; não abrir uma segunda PR para a mesma competência sem motivo demonstrado.

## 4. Aprendizado, continuidade e entrega
Todo defeito confirmado deve ter proposta de correção, risco de regressão e uma evidência de reteste. Preservar last-known-good. Conservar conhecimento transferível mesmo quando uma mudança é rejeitada. Relatórios devem distinguir CONCLUÍDO NO REPOSITÓRIO, AGUARDANDO TESTE, AGUARDANDO MERGE, INSTALADO e NÃO VERIFICADO; reportar commits e bloqueios quando verificáveis. Em falta de GitHub/host, marcar UNKNOWN e não inventar estado.

## 5. Hierarquia e limites
Adendo documental, complementar ao Mission Lock da missão, ao ECP, aos OWNERs e aos gates Coliseum. NÃO autoriza deploy, merge automático, alteração em produção, acesso a dados privados, consumo pago, publicação ou reescrita de escopo. Em conflito material, registrar REVIEW_REQUIRED e preservar o estado anterior. Este próprio adendo só vigora na main após merge; a existência de PR não basta.

## 6. Gatilho de revisão de próxima tarefa
CHECK_LAST_CHECKPOINT -> VERIFY_LIVE_GITHUB -> DIFF_ONLY -> DEPENDENCIES -> TEST_EVIDENCE -> CLASSIFY_STATE -> NEXT_ACTION -> UPDATE_LEDGER. Em projeto sem Mission Lock prévio, este texto estabelece somente a camada de rastreabilidade, não define produtos, requisitos ou permissões inexistentes.
