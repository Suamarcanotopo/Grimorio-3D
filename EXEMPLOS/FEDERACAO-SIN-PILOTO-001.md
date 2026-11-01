# PILOTO SIN-FED-001 — Vitrine de produto tridimensional e quatro fontes canônicas

**Estado:** candidata de demonstração para homologação, não publicação comercial. **Data:** 01/11/2026. **OWNER do artefato técnico:** Grimorio-3D. **Baseline:** main, consultar SHA do PR; branch `feat/sin-federacao-piloto-001-webgl-20261101`. **Execução externa:** não alterada. Este piloto não precisa do PR da federação para preservar seus próprios registros, mas sua adoção completa depende da integração controlada da política candidata.

## Produto e problema simulado

**Módulo Zero** é um objeto geométrico fictício sem marca comercial externa. A demonstração testa se quatro Grimórios podem cooperar para construir um resultado técnico verificável e comercialmente reutilizável sem copiar acervos, atribuir licença inexistente ou fingir teste de IA.

**Entregáveis reais:**
- `EXEMPLOS/FEDERACAO-SIN-PILOTO-001.html`: página offline, original e responsiva com geometria WebGL em JavaScript, texto, controles de giro, teclado, pausa e fallback.
- Este documento: storyboard, critérios, proveniência, gates, resultado e planos de testes.
- Um teste de regressão estático de requisitos que bloqueia URLs externas, submissão de dados e perda de controles.
- Um artifact da Action contendo HTML e este dossiê, para homologação sem instalar dependências no site.

## Federação real — origem → uso → prova

| Etapa | Fonte exata (verificada por leitura do GitHub) | O que é consumido | Prova/limite |
| --- | --- | --- | --- |
| 1. Significado | [Grimorio-SIN / cinema, semiótica e linguagem visual](https://github.com/Suamarcanotopo/Grimorio-SIN/blob/main/ESCOLA/CINEMA-IMAGEM-SIGNOS/INDEX.md) | a distinção entre **interpretar**, **produzir** e **verificar**, composição e significado | conceito aplicado ao texto; sem alegar eficácia de vendas |
| 2. Arquétipos | [Grimorio-SIN / 78 matrizes LORE](https://github.com/Suamarcanotopo/Grimorio-SIN/blob/main/ESCOLA/ARQUETIPOS-LORE/INDEX.md) | limites para não converter ferramenta criativa em psicometria | evitado teste sobre pessoas; nenhuma inferência clínica |
| 3. Enquadramento | [ListOFprompts / índice de 362 fichas](https://github.com/Suamarcanotopo/ListOFprompts/blob/main/livro-visual-sin/INDICE-362-SHEETS.md) | transformar intenção visual em plano de câmera e variações de cena | prompts descritos abaixo; **nenhuma imagem de IA gerada** |
| 4. Fidelidade | [ListOFprompts / Character Lock](https://github.com/Suamarcanotopo/ListOFprompts/blob/main/livro-visual-sin/CHARACTER-LOCK.md) | diferenciar preservação de identidade visual de garantia matemática | caso do produto sem pessoa/foto; comparar empiricamente variações futuras |
| 5. Visualização | [Grimorio-3D / websites 3D](https://github.com/Suamarcanotopo/Grimorio-3D/blob/main/GUIAS/04-WEBSITES-3D.md) | página com renderização isolada, controles acessíveis e fallback | WebGL implementado com geometria original; testes por aparelho futuros |
| 6. Entrega | [Grimorio-3D / pipeline e formatos](https://github.com/Suamarcanotopo/Grimorio-3D/blob/main/GUIAS/05-PIPELINE-EXPORTACAO.md) | original editável ≠ exportação GLB ≠ render | HTML é fonte deste piloto; **nenhum arquivo GLB produzido** |
| 7. Coordenação | [grimorio-skills / ECP canônico](https://github.com/Suamarcanotopo/grimorio-skills/blob/main/skills/engineering-control-plane/SKILL.md) | objetivo, escopo, risks, Mission Lock, testes, handoff e rollback | ECP 3.6.0-rc.1 foi informado instalado externamente, ainda candidato no GitHub PR #72 |
| 8. Governança | [grimorio-skills / PR #73](https://github.com/Suamarcanotopo/grimorio-skills/pull/73) | proprietário único, links, nenhum privilégio cruzado, Coliseum/SEE | PR ainda requer reconciliação e autorização, não é uma norma incorporada |

## Storyboard autoral reproduzível — não testado em modelos

**Cena 1 — estabelecimento (5 segundos):** fundo de estúdio azul escuro, luz suave sobre um módulo geométrico azul com seis faces, câmera frontal aproximando-se lentamente. Símbolo: clareza da forma. **Prompt candidato:** “Fotografia de produto fictício em estúdio: módulo cúbico geométrico azul, sem marcas e sem tipografia, luz difusa lateral, ambiente escuro, lente equivalente a 50 mm, preservar proporções, sem peças inventadas. Registrar modelo, versão, seed e limitações ao gerar.”

**Cena 2 — entendimento (5 segundos):** mesmo objeto sob luz constante, três ângulos progressivos sem alterar geometria. **Prompt candidato:** “Produza três visões do mesmo módulo cúbico de seis faces, sem novos componentes, escala e textura constantes, câmera mudando apenas a rotação horizontal, cenário idêntico. Verificar consistência antes de aprovar variações.”

**Cena 3 — interação (livre):** usuário gira o objeto em página e lê sobre transparência metodológica. **Implementado:** WebGL offline com geometria por vértices, botão de pausa, giro por teclado e fallback.

**Risco da transferência:** um modelo de geração de imagem pode adicionar detalhes. Nunca declarar Character Lock aprovado por só escrever o texto. O WebGL é renderização geométrica independente de modelo generativo.

## ECP — Completion Contract

| Prova | Como verificar | Estado inicial |
| --- | --- | --- |
| Fonte de cada competência | links canônicos dos 4 repositórios | URLs e conteúdo lidos via GitHub |
| Material técnico entregue | HTML existente e fonte sem bibliotecas externas | IMPLEMENTADO, sujeito a teste |
| Segurança de dados | inspecionar scripts, network e permissões | revisão estática pendente |
| Acessibilidade | foco em controles, teclado, redução de movimento, fallback | implementado; teste humano pendente |
| Regressão | testes estruturais + validadores atuais do Grimorio-3D | CI pendente |
| Browser E2E | renderização pixel a pixel, clique, teclado, fallback | NOT_RUN até executar |
| IA audiovisual | imagem/vídeo real conforme storyboard | NOT_RUN |
| GLB exportado e licenciado | arquivo GLB com checksum e viewer | NOT_APPLICABLE (não prometido neste piloto) |
| Conversão e receita | experimento de landing com tráfego real | NOT_RUN |

## Governance Guard — Mission Lock

- **Permitido:** somente HTML, dossiê, scripts/workflow de teste, índice integral e handoff deste piloto em branch separada.
- **Proibido:** alterar fontes, licenças, preços, contratos de outros repositórios, outros exemplos, assets, catálogos originais e produção.
- **Risco:** R2 por código WebGL de demonstração e novo workflow; nenhuma escrita externa, sem credenciais, sem dependência de CDN.
- **Rollback:** não mesclar PR. Se integrado, reverter apenas arquivos deste piloto, atualizando índice.
- **Autoridade:** solicitação de execução da missão; não significa liberação comercial ou aprovação de código independente.

## Coliseum — Red Team

1. HTML gera pedidos de rede? **Bloquear qualquer dependência externa não justificada.**
2. Código injeta dados sensíveis? **Não há formulários, segredos ou persistência; inspecionar fonte.**
3. Cubo gira mas a cena é falsa 3D? **Verificar contexto WebGL e pixels em navegador real.**
4. Contraste e teclado quebram? **Testes de interação e revisão humana de acessibilidade.**
5. Movimento reduzido é ignorado? **A animação inicial deve estar pausada quando aplicável.**
6. URL do exemplo aponta a branch errada? **Manter caminhos canônicos e indexação 100%.**
7. Provedor IA já rodou? **Não: NOT_RUN.**
8. GLB ou assets de terceiros foram criados? **Não: não afirmar.**
9. CI PASS implica garantia multi-browser? **Não.**
10. Experiência mostra resultado de vendas? **Não; este é um protótipo sem teste comercial.**

## SEE — Downside protegido, upside comercial

Se o WebGL falhar ou o piloto for rejeitado, ficam código original, mapa de 4 fontes, critérios, acessibilidade e testes como material reutilizável. Se for aprovado, o modelo é ponto de partida para vitrines 3D de indústrias com direitos, métricas e propostas claras. Nenhuma receita comercial foi presumida.

## Handoff e próxima ação

**Prioridade:** executar validação da página em navegador headless e ações do usuário; registrar resultado por run/SHA. Depois revisar escopo, direitos e publicação. Adoção no main só após prova, revisão e autorização do proprietário, em PR separado do contrato da Federação #15.


## Checkpoint real de navegador — Playwright + Chromium (01/11/2026)

**Ambiente:** Chromium headless local, viewport desktop 1280×800 e mobile 375×812, Playwright, HTML exportado do artifact GitHub Actions. **Resultado confirmado:** documento HTML abriu; nenhum erro JavaScript de página; sem overflow horizontal nas duas resoluções; quando `canvas.getContext('webgl')` retornou `null`, a interface revelou corretamente um fallback e desativou os três botões.

**Limitação importante:** o sandbox de Chromium deste teste bloqueou WebGL mesmo tentando SwiftShader. A renderização tridimensional real, a compilação de shaders, os testes de GPU e a interação com o cubo **NÃO FORAM HOMOLOGADOS**. Como resultado, Coliseum emite **RETEST** para o requisito WebGL, e não PASS. Teste de dispositivos reais e navegação por teclado em WebGL continuam pendentes.

A iteração posterior melhorou o fallback: agora ele inclui uma ilustração CSS explicitamente identificada, sem fingir ser um render WebGL. O ramo condicionado por falha de compilação também desabilita controles. Uma nova execução do navegador deve ser registrada após esse commit; os resultados acima pertencem ao artefato anterior.

**Verificação estática de CI:** workflow `SIN Federation Pilot 001 — offline WebGL` [run 41334677068](https://github.com/Suamarcanotopo/Grimorio-3D/actions/runs/41334677068) concluiu SUCCESS antes do ajuste visual; os workflows de índice e catálogo também concluíram SUCCESS. Reexecutar no SHA final. **Source Lock federado:** PRs #73, #20, #5 e #15 foram integrados ao `main` após autorização do proprietário para execução da sequência; esta PR técnica #16 continua separada e NÃO foi mesclada.

**Gate de publicação:** realizar prova do modelo 3D em navegador com WebGL disponível, revisão técnica e decisão expressa antes de promover esta demonstração à `main`.
