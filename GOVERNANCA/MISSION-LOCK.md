# Mission Lock — Grimório 3D

**Objetivo imutável:** ser base de conhecimento técnico, didático e internacional sobre 3D em PT-BR, com links verificáveis e prática reproduzível, sem redistribuição indevida de propriedade intelectual ou downgrade.

## Deveres obrigatórios

**ML-01 — Escopo:** abranger modelagem, UV, texturização, escultura, topologia, rigging, animação, tracking, VFX, render, games, arquitetura, industrial/CAD, web, XR, IA, captura, normas e comunidades globais.

**ML-02 — Cadastro:** toda fonte deve possuir ID único, título, descrição, URL HTTPS, nicho, finalidade, primeiro passo, dica prática, indicação de acesso, status de direitos e data de referência.

**ML-03 — Não inventar:** ausência de prova deve aparecer como `não homologado` ou `não verificado`; não inventar preços, promessas de licença ou aprovação.

**ML-04 — Proteção de dados:** imagem/voz/mocap/scan de pessoas requer avaliação de autorização e LGPD. Não armazenar segredos, credenciais ou dados de clientes.

**ML-05 — Propriedade intelectual:** MIT do repositório cobre apenas os arquivos originais sob nossa autoria; **não** impõe licença MIT aos assets de terceiros listados. CC0, CC BY, CC BY-SA, CC BY-NC e condições exclusivas devem ser tratadas individualmente.

**ML-06 — Segurança:** scripts, extensões, executáveis e dependências são potencialmente executáveis. Quarentena e inspeção antes de execução, e não incluir downloads binários sem direitos.

**ML-07 — Pipeline:** nunca sobrescrever fonte editável; exportação de runtime não substitui projeto de origem. Manter manifesto e checksum.

**ML-08 — Performance/acessibilidade:** publicar em web/game/XR apenas após testes por dispositivo e fallback funcional onde pertinente.

**ML-09 — Rastreabilidade:** modificar por branch + Pull Request, registrar evidência e regressão; preservar histórico Git, fontes e notas de migração.

**ML-10 — Sem maquiagem:** não relatar teste/CI/homologação que não ocorreu. Quantidade de links ≠ qualidade garantida.

## Convenções locais de coordenação

- **ECP:** aqui, nome metodológico de orquestração e verificação; não é norma internacional nem serviço invocado automaticamente.
- **Coliseum / Red Team:** papéis de revisão adversarial para detectar licenças incertas, links duvidosos, vieses, segurança e pontos de quebra.
- **OWNER:** responsável por aceitar uma mudança; **REVIEWER:** verifica evidências e riscos; **CONTRIBUTOR:** propõe mudança documentada.
- **Mission Lock:** conjunto de invariantes e critérios de bloqueio documentados; **não** significa que um texto por si só proteja o runtime ou o GitHub.

## Portões mínimos de aprovação

1. **A — Evidência da fonte:** link, organização e finalidade têm fundamento.
2. **B — Esquema:** CSV/JSON e categorias sem duplicações.
3. **C — Didática:** termos explicados, caso prático e 'o que evitar'.
4. **D — Direitos:** risco e status comercial explícitos.
5. **E — Segurança/privacidade:** sem scripts desconhecidos ou dados pessoais.
6. **F — Integridade:** README e documentos apontam para arquivos existentes.
7. **G — Revisão humana:** revisão de licenciamento quando houver incorporação comercial.

**Prova:** [Script de validação](../scripts/validar.py), [Matriz de aceitação](MATRIZ-ACEITACAO.md), [Política de contribuições](CONTRIBUICAO.md).

**Referência transversal:** [Glossário de governança legível do SIN](https://github.com/Suamarcanotopo/grimorio-skills/blob/main/dependencies/governanca-legivel/GLOSSARIO.md).


## ML-11 — Didática progressiva (2026-10-16)

O Glossário, FAQ e os Laboratórios são dependências obrigatórias da formação. Toda instrução técnica deve informar **o que é**, **por que importa**, **como fazer**, **onde aprender** e **como testar**. Quando recurso, preço ou versão depender de fornecedor, registrar status e data de referência.

## ML-12 — Compatibilidade XR e social não presumida

O conhecimento autoral em BLEND deve ser preservado e exportado individualmente a **web (GLB), WebAR (Scene Viewer/Quick Look), Snap Lens, TikTok Effect House, Unreal/Meta Quest ou Horizon** conforme os contratos. **Meta Spark de terceiros encerrado em 2025** nunca deve ser apresentado como opção de nova publicação. O termo *Snapshot* é ambíguo: na rota de efeitos sociais, usar o nome oficial **Snap/Snapchat** e Lens Studio.

## ML-13 — Mudanças de versões e SDKs

As dependências de SDK não devem ser instaladas pelo repositório documental. Cada produto real exige versão fixada, termo e aprovação da plataforma, prova no aparelho, política de câmera e rollback. Divergências de documentação — inclusive limites TikTok — devem ser mostradas como conflito a conferir, não ocultadas.

## ML-14 — Critério de excelência verificável

O Grimório pode ensinar práticas de nível profissional; nunca prometer que somente ler a documentação torna alguém especialista. Para homologação de habilidade, exigir entrega reproduzível, revisão humana, comparação com documentos oficiais e evidências de desempenho e direitos no destino.

**Documentos vinculantes:** [Currículo](../ACADEMIA/MAPA-DE-COMPETENCIAS.md), [Glossário](../GLOSSARIO/README.md), [FAQ](../FAQ/README.md), [Tutoriais](../TUTORIAIS/README.md), [Dependências](../DEPENDENCIAS/README.md).


## ML-15 — ECP: fonte única, competência, contrato e não duplicação

As **18 etapas canônicas**, as **10 trilhas profissionais** e o **catálogo JSON/CSV** têm responsabilidades diferentes. Não duplicar cadastro de fonte em listas paralelas não sincronizadas: documentação por nicho deve apontar a referência canônica. Padrões técnicos e conhecimento atemporal não podem ser silenciosamente substituídos por notícias recentes ou por hype.

## ML-16 — Coliseu: contestação e decisão com evidência

Toda ampliação registra baseline, fonte, risco, teste e resultado. O protocolo adversarial usa **ACCEPT, REJECT, RETEST ou ESCALATE**. Uma revisão de texto não equivale a execução de ferramenta ou aprovação humana; o relatório deve separar revisão metodológica, validação automatizada e resultados de dispositivos.

## ML-17 — Amplitude geográfica sem ranking inventado

As fontes internacionais são institucionais, documentais ou editoriais de alta relevância. Não criar hierarquia de países sem metodologia independente; conteúdo estrangeiro tem **orientação didática PT-BR**, preservando URLs, nomes de comandos e direitos autorais.

## ML-18 — Invariantes Skill-ready e dependências mínimas

Este repositório é base de competências para Skills e não instala pacotes, não faz cópia não autorizada e não reescreve Skills de outro repositório. Runtime/SDKs só devem ser especificados no **projeto do usuário** com versão testada e licença; links educacionais permanecem dependências de conhecimento.

## ML-19 — Atualidade com data e reversibilidade

Informações de versão, custo, requisitos e API entram no radar datado; mantêm status **CURRENT, STALE, NEEDS_TEST, BLOCKED ou DEPRECATED**. Não incluir agendamento de busca inexistente. Todo PR preserva IDs, arquivos originais, normas, licenças e resultado de teste de regressão.

**Interlocks:** [ECP/Coliseu](ECP-COLISEU-2026-10-16.md) · [18 etapas](../CURRICULO/ETAPAS-DA-PRODUCAO.md) · [Política de fontes](FONTES-ATEMPORAIS-E-ATUAIS.md) · [Contrato para Skills](../SKILLS/README.md).

## ML-20 — evolução por camadas isoladas (2026-10-16)

Expansões volumétricas seguem ordem **fontes → glossário → FAQ → laboratórios → navegação/qualidade**, cada fase com branch, baseline, diff, regressão e merge independentes. Aumento de quantidade NÃO substitui curadoria, revisão de licenças ou testes reais de ferramentas. A fonte canônica permanece `FONTES/catalogo.json`, que alimenta CSV, nichos e README. Preservar CTA e Mission Lock anteriores.

## ML-21 — laboratórios offline e limites de execução

O diretório `EXEMPLOS/01` a `10` ensina conceitos por HTML/CSS/JavaScript local, sem baixar SDK nem enviar arquivos à rede. A simulação didática não deve ser descrita como renderização 3D de produção, benchmark de GPU, teste em headset, física de engenharia ou homologação de produto. O arquivo `07` interpreta parte do GLB no navegador; **não executa o arquivo, não transfere dados e não substitui validador glTF completo**. Cada demo deve ter idioma PT-BR, descrição, controle acessível, fallback conceitual e rodapé SIN. O teste automático avalia estrutura e conteúdo declarados, não execução real em navegadores.

## ML-22 — relações didáticas canônicas e anti-orfandade (2026-10-17)

O mapa `APRENDER/mapa.json` conecta fontes e 38 nichos, 293 verbetes, 210 FAQs, 37 tutoriais, 10 demos e 10 percursos de mercado, **sem substituir os cadastros canônicos**. Toda competência deve preservar objetivos, pré-requisitos, convenção técnica, truque aplicável, erro comum, correção e prova documentada. O índice individual referencia títulos originais e não duplica definições de terceiros. Alterações futuras devem exigir validação do grafo e das rotas no CI, evitando material órfão, IDs perdidos, tutoriais desconectados e links SIN quebrados.

**Interlock Coliseu:** texto e execução têm estados separados (`LIDO`, `PRATICADO`, `TESTADO`, `HOMOLOGADO`, `NÃO TESTADO`, `BLOQUEADO`). CI documental não substitui avaliação em Blender, Unreal, Meta Quest, Snap, TikTok ou direitos individuais. Evoluir por PR com reversão e sem downgrade.
