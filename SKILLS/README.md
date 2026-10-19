# Grimório 3D como biblioteca-fonte para Skills

**Conhecimento roteado para Skills:** [Mapa estruturado por competência](../APRENDER/mapa.json) · [Caderno de provas](../APRENDER/CADERNO-DE-PROVAS.md). São referências e evals, **não Skills automaticamente instaladas**.

**Objetivo:** servir de conhecimento canônico e avaliação para Skills de modelagem, games, cinema, publicidade, XR e websites. **Não é uma coleção de Skills instaladas**: seu trabalho é fornecer contratos e bases legíveis por máquina, reutilizadas por um processo de Skill Architect.

**Compatibilidade dos modelos:** [protocolo agnóstico de conhecimento 3D](../INTEROPERABILIDADE/README.md). Os adaptadores não instalam Skills no catálogo de nenhum provedor. Cada Skill deve possuir contrato, tools, evals e revisão próprios.

## Como o ECP roteia conhecimento

| Papel | Área | Limite de autoridade |
|---|---|---|
| Engineering Control Plane (ECP) | Mission, Completion Contract, roteamento, commits e prova de fechamento | Não finge executar editor 3D |
| SIN Skill Architect | Converte competência em pacote Skill com evidências e evals | Não se autopromove sem revisão |
| SIN Motion Expertise Council | Define especialistas de VFX, motion, 3D, câmera, arte e composição | Não substitui softwares, nem render |
| Coliseum | Testa os casos adversariais e veta alegações sem prova | Não substitui responsável por domínio |
| Blender/Unreal/WebXR OWNER | Executa ou prepara o fluxo especializado quando ferramentas existem | Não muda políticas de licenciamento |
| SEE — Skill Evolution Engine | Verifica freshness/delta e versões de skills | Não sobrescreve core sem avaliação |

**Skills canônicas e contratos transversais:** https://github.com/Suamarcanotopo/grimorio-skills

## Da leitura à Skill governada

`CASO → EVIDÊNCIA → LIÇÃO → PADRÃO → GUARDRAIL → CAPABILITY → EVAL → SKILL CANDIDATA → REVISÃO COLOSSEUM → PROMOÇÃO`

Uma ficha de curso ou link do GitHub **não é uma Skill operacional**. Para virar competência automatizável, declare gatilhos, entradas, ferramentas, saídas, permissões, contraexemplos, limites e testes.

- [Modelo de contrato e template](CONTRATO-DE-SKILL-3D.md).
- [Casos adversariais em JSON](casos-red-team.json).
- [Currículo de 18 etapas](../CURRICULO/ETAPAS-DA-PRODUCAO.md).
- [Rubrica humana](../ACADEMIA/RUBRICA-DE-HOMOLOGACAO.md).
- [Protocolo de fontes e freshness](../GOVERNANCA/FONTES-ATEMPORAIS-E-ATUAIS.md).

## Skills que mais agregariam (sem inflar a quantidade de Skills)

| Candidato de competência | Núcleo reutilizável | Especialização por destino |
|---|---|---|
| 3D Asset QA | Normais, UV, escala, licenças, formato e performance | Blender, game engine ou browser |
| SIN Web3D/AR Builder | GLB, glTF, fallback, acessibilidade, segurança | model-viewer, Three.js, Scene Viewer, Quick Look |
| SIN Virtual Production | Lens, passes, tracking, cor e sincronia | Unreal ICVFX, Nuke e hardware de set |
| SIN Social AR Studio | Otimização de modelagem e proteção de dados | Snap Lens Studio/Camera Kit ou TikTok Effect House |
| SIN Procedural World Architect | Seeds, instancing, LOD, biomas e proveniência GIS | Blender Geometry Nodes, Houdini e engines |

**Decisão atual:** construir primeiro **contratos e casos de teste reutilizáveis**. Criar Skills duplicadas antes de demonstrar necessidades específicas aumentaria tokens e downside.
