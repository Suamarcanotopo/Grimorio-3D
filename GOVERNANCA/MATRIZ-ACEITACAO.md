# Matriz de aceitação — evidência, não marketing

| Nº | Critério | Procedimento | Resultado atual |
|---|---|---|---|
| 01 | Fonte oficial do repositório preservada | GitHub original mantém LICENSE e histórico | PASS após conferir |
| 02 | Catálogo original não perdido | Comparar 87 IDs e URLs anteriores | Executar script |
| 03 | IDs únicos | Executar `scripts/validar.py` | Executar script |
| 04 | URLs HTTPS únicas | Executar `scripts/validar.py` | Executar script |
| 05 | Campos didáticos preenchidos | Executar `scripts/validar.py` | Executar script |
| 06 | CSV/JSON sincronizados | Executar `scripts/validar.py` | Executar script |
| 07 | README aponta para caminhos existentes | Revisar links internos | Revisão necessária |
| 08 | Pelo menos um exemplo web 3D | Inspecionar EXEMPLOS | Revisão necessária |
| 09 | Cobertura 3D interdisciplinar | Revisar índice e nichos | Revisão humana necessária |
| 10 | Direitos por item | Consultar licenças concretas antes de usar | NÃO HOMOLOGADO globalmente |
| 11 | Links ativos na internet | Monitoramento sob demanda, fonte a fonte | NÃO VERIFICADO globalmente |
| 12 | Segurança de plugins | Sandbox/inspeção por integração | NÃO APLICÁVEL ao catálogo sem execução |
| 13 | Performance real em aparelhos | Teste de produto concreto | NÃO TESTADO |
| 14 | Revisão didática por equipe | Aprovação manual formal | PENDENTE |
| 15 | CI GitHub | Execução real registrada | PENDENTE até execução |
| 16 | Publicação na main | PR revisado e merge identificado | PENDENTE |

**Importante:** nunca converter 'pendente' ou 'não aplicável' em 'aprovado'. Estado deve ser revisado a cada liberação.


## Aditivo v0.3 — gates ECP + Coliseu

| Gate | Evidência necessária | Estado inicial |
|---|---|---|
| ECP-01 Base preservada | 208 IDs anteriores e README original | Verificar por CI |
| ECP-02 Catálogo novo íntegro | ≥238 fontes, 38 nichos, CSV=JSON | Verificar por CI |
| ECP-03 Currículo | 18 etapas didáticas e documento de contratos | Verificar por CI |
| ECP-04 Nichos profissionais | 10 cadernos com prática e aceite | Verificar por CI |
| ECP-05 Panorama internacional | Pelo menos 19 registros e não ranking | Verificar por CI |
| ECP-06 Skill evals | 16 casos válidos com resposta esperada | Verificar por CI |
| ECP-07 Fontes vivas | Radar datado e política de atualização | Verificar por CI |
| ECP-08 Dependências | Separadas em referência, técnica, ferramenta, SDK e asset | Verificar por CI |
| ECP-09 Links internos | Nenhum caminho ausente | Verificar por CI |
| ECP-10 Direitos e hardware | Testes/termos por projeto | **PENDENTE por escopo** |

**Regras:** "PENDENTE" não é 100% aprovado. Registre resultado de PR/CI real antes de promover o estado.
