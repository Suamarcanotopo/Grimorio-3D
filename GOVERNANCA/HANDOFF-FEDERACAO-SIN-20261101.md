# Handoff — Federação SIN / Grimorio-3D / 01-11-2026

**ID:** FED-SIN-20261101-GRIMORIO-3D. **Estado:** CANDIDATE — branch `feat/sin-federacao-4-grimorios-20261101`, PR a verificar antes de qualquer merge. **BASE:** main real na criação da branch; conferir o `base_sha` e `head_sha` do PR no GitHub quando homologar. **Não instalado em runtime; não publicado; sem concessão de autoridade.**

## Por que esta missão existe
O proprietário informou que instalou externamente quatro Skills candidatas — ECP, Governance Guard, SEE e Coliseum — e pediu que elas organizassem as quatro casas do conhecimento. A execução no repositório é proposta documental com fonte, competência OWNER, handoff e testes; não transforma análise da IA em auditoria humana independente.

## Escopo escrito / Source Lock
- Fonte humana: [README](../README.md) → [Mapa por objetivo](../MAPA-COMPLETO.md) → corpus canônico no `main`.
- Fonte técnica transversal: [contrato federado central](https://github.com/Suamarcanotopo/grimorio-skills/blob/main/GOVERNANCA/FEDERACAO-SIN-4-GRIMORIOS-v1.md), **link que funcionará após integração**. Enquanto não integrado, consultar o PR da federação.
- Fonte local vinculante: AGENTS.md, Mission Locks vigentes e constituição específica do repositório, que **prevalecem** se alguma regra nova for incompatível.
- Delta desta missão: contrato local de competência (somente para as três casas consumidoras), handoff, ponte de navegação em README/AGENTS, atualização do catálogo integral.
- **Proibidos:** alteração do conteúdo substantivo, schemas, pacotes, licenças, direitos, dados privados, históricos e status epistemológicos.

## Invariantes a proteger
368 fontes e seus direitos intactos, 18 etapas e 10 trilhas existentes preservadas, nenhum asset ou licença modificado.

## ECP — plano e entrega
R0 de navegação e contrato documental, com revisão reforçada porque os textos orientam agentes. U00 fonte verdadeira, U01 escopo, U03 anti-regressão, U05 testes, U06 revisão adversarial, U10 handoff. Gates U02/U04/U07/U08/U09 avaliados na medida do risco; U11 não autoriza merge automaticamente; U12 pós-runtime permanece NOT_RUN.

## SEE — baseline e upgrade
Novas regras são **camada candidata**, sem versionamento de Skills neste repositório; os quatro ZIPs informados pelo usuário não se tornam automaticamente sincronizados com o main Git. Dados e capacidades canônicos anteriores devem continuar intactos.

## Coliseum — contraprovas
- FALHA se duplicar o conteúdo proprietário de outra casa;
- FALHA se disser que código/recibo textual é prova de execução ou aprovação humana;
- FALHA se quebrar referência/ID/índice de um conteúdo protegido;
- FALHA se confundir técnica, ficção, dado científico, licença ou comando oficial;
- RETEST se não houver CI real para o SHA final ou se houver conflito com um PR ativo;
- ESCALATE se uma mudança futura envolver direitos, aprovação editorial, permissão, remoção ou produção.

## Testes necessários antes da promoção
```bash
python3 scripts/validar.py
python3 scripts/validar-indice-total.py
teste real em dispositivo NOT_RUN
```
Um teste estrutural PASS não comprova qualidade pedagógica, legalidade de cada asset, geração real de imagem, funcionamento de modelo específico nem publicação. Registrar estados honestos.

## Pendências, próximo passo e rollback
**Pendências:** Licenças externas dependem de verificação por caso; nenhum viewer/dispositivo foi executado nesta missão.

**Próxima ação:** confirmar CI e diff reais da PR do repositório, comparar com Mission Locks atuais, corrigir conflitos e solicitar revisão autorizada para eventual merge.

**Rollback:** manter PR DRAFT; não mesclar. Caso seja integrado depois, reverter somente os commits da federação, sem remover conteúdo canônico ou histórico.


## Checkpoint Coliseum — diffs e CI observados em 2026-11-01

- **PR candidata:** https://github.com/Suamarcanotopo/Grimorio-3D/pull/15, ainda DRAFT, sem merge.
- **Escopo inspecionado:** cinco caminhos somente — `README.md`, `AGENTS.md`, `CATALOGO-TOTAL-ARQUIVOS.md` e dois contratos em `GOVERNANCA/`. Nenhum corpus, asset, skill package, licencia­mento, schema, arquivo cliente ou produção foi modificado.
- **GitHub Actions da revisão original:** [41330540615](https://github.com/Suamarcanotopo/Grimorio-3D/actions/runs/41330540615) · [41330540619](https://github.com/Suamarcanotopo/Grimorio-3D/actions/runs/41330540619).
- **Resultados reais observados:** Catálogo 3D: PASS; índice: PASS; 229 caminhos no catálogo. São testes estruturais, não validação humana de ensino, instalação, uso de modelo, renderização ou deploy.
- **Veredito:** `RETEST` para adoção federada: evidência estrutural permite considerar a documentação, mas não comprova que as quatro Skills externas executaram suas instruções em runtime. Revisão humana e aprovação de merge permanecem pendentes.
- **Ordem de integração:** [grimorio-skills PR #73](https://github.com/Suamarcanotopo/grimorio-skills/pull/73) primeiro, depois os contratos locais dos outros três PRs. Reexecutar checks sobre os commits finais antes de qualquer promoção.

**Proteção de downside:** caso a federação não seja aprovada, conservar evidências de diff e testes; nenhum acervo ou Skill canônica foi substituído. **Próxima ação:** avaliar governança real GitHub (required checks, revisões), testar navegação de pessoas e uma ponte de conteúdo ponta a ponta, sem misturar conteúdos privados.
