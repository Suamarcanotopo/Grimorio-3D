# As 18 etapas da produção 3D — do zero à entrega profissional

**Objetivo:** uma única sequência canônica, usada por games, cinema, anúncios, arquitetura, educação, websites e realidade estendida. Cada destino usa subconjunto das etapas, mas **não ignora licenças, importação, testes nem arquivos nativos**.

[Trilhas por mercado](../NICHOS/README.md) · [Perguntas](../FAQ/README.md) · [Glossário](../GLOSSARIO/README.md) · [Pipeline de dependências](../DEPENDENCIAS/README.md)

## Mapa visual da cadeia

`BRIEF → REFERÊNCIAS → CONCEITO → BLOCKOUT → GEOMETRIA → UV/MATERIAIS → LOOKDEV → RIG → ANIMAÇÃO/TRACKING/VFX → CÂMERA/LUZ → ÁUDIO/EDIÇÃO → OTIMIZAÇÃO → EXPORTAÇÃO → RUNTIME → DIREITOS/SEGURANÇA → HOMOLOGAÇÃO`

### Qualidade não é contagem de links

Uma etapa só é dominada quando é possível: **explicá-la em português simples, executá-la em trabalho próprio, detectar defeito, recuperar o erro, reproduzir resultado e justificar trade-offs de custo/qualidade**.

## 01 — Briefing e problema real

**O que é:** Definir público, cena, destino, orçamento, direitos, prazos, acessibilidade e métricas antes de escolher programa.

**Por que importa:** Evita render bonito que não cabe no navegador, jogo ou campanha.

**Como praticar:** Escolha cenário fictício: visualizador 3D de uma embalagem; defina arquivo-alvo GLB, público mobile e CTA.

**Critério de aceite:** Brief assinado com objetivo, dispositivo, limitações, fonte dos recursos e métrica verificável.

**Fonte primária de estudo:** https://www.w3.org/WAI/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 02 — Pesquisa e repertório com procedência

**O que é:** Construir referências de materiais, composição, escala, estilo, iluminação e mercado; separar inspiração de ativos reutilizáveis.

**Por que importa:** Copiar referência protegida pode comprometer toda a entrega.

**Como praticar:** Busque três referências autorizadas, identifique linguagem visual, registre autores e URLs sem copiar mídia.

**Critério de aceite:** Moodboard com direitos identificados; referências de casos datadas.

**Fonte primária de estudo:** https://creativecommons.org/licenses/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 03 — Conceito, storyboard e pré-visualização

**O que é:** Converter brief em esboços, thumbnails, enquadramentos, cenários de câmera e storyboard.

**Por que importa:** Valida a comunicação antes de modelar dezenas de horas.

**Como praticar:** Crie sequência de três quadros para anúncio de um produto imaginário e teste leitura sem narração.

**Critério de aceite:** Sequência aprovada para mensagem, composição e duração.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 04 — Blockout e escalas

**O que é:** Usar cubos e cilindros para volume e circulação; definir unidades, eixos, pivôs e hierarquia.

**Por que importa:** Erros de proporção se propagam para AR, rig e física.

**Como praticar:** Construa cenário com medidas físicas simples e teste percurso da câmera.

**Critério de aceite:** Projeto BLEND com volumes coerentes, origens e unidades documentadas.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/modeling/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 05 — Modelagem, escultura e topologia

**O que é:** Construir malhas, quads/tris, normal, retopologia e variantes de detalhamento.

**Por que importa:** Controla deformação, shading, custo de render e edição futura.

**Como praticar:** Modele uma cadeira com bevels, compare com uma versão decimada e confira silhueta.

**Critério de aceite:** Fonte high-poly preservada, low-poly validada, normais sem falhas críticas.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 06 — UV, UDIM, textura e baking

**O que é:** Abrir ilhas UV, verificar texel density, configurar PBR e realizar bake quando útil.

**Por que importa:** Textura excelente falha com UV esticada ou normal map invertido.

**Como praticar:** Use checkerboard em peça com curvas, corrija distorção e faça teste de roughness.

**Critério de aceite:** UV e mapas PBR coerentes em pelo menos duas iluminações.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 07 — Direção de arte, lookdev e cor

**O que é:** Definir paleta, materiais, contraste, luz, gerenciamento OCIO/ACES e aprovar aparências.

**Por que importa:** Cor inconsistente entre renderizador e vídeo destrói fidelidade de marca.

**Como praticar:** Faça comparativo do mesmo material no Blender e em visualizador glTF; registre diferença de cor.

**Critério de aceite:** Cores e passes documentados, não só screenshot isolada.

**Fonte primária de estudo:** https://opencolorio.org/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 08 — Rig, deformação e controles

**O que é:** Preparar armature, skinning, pesos, IK/FK, rig facial e condições de retargeting.

**Por que importa:** Articulações com pesos ruins tornam personagem inutilizável.

**Como praticar:** Crie um braço com duas articulações, configure IK, faça duas poses extremas.

**Critério de aceite:** Sem clipping grave, pesos revisados e esqueleto exportável.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/animation/armatures/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 09 — Animação e captura de movimentos

**O que é:** Planejar keyframes, curvas, ritmo, ações, root motion e mocap com autorização.

**Por que importa:** Entregas exigem continuidade temporal e controle, não apenas estética estática.

**Como praticar:** Anime o mesmo gesto com FK e mocap de própria autoria, compare o resultado.

**Critério de aceite:** Vídeo de teste, origem dos movimentos, versão e rig compatível.

**Fonte primária de estudo:** https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-in-unreal-engine

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 10 — Tracking e integração com filmagem

**O que é:** Rastrear câmera/lente, resolver perspectiva, realizar planar tracking, máscaras e oclusões.

**Por que importa:** VFX exige que o virtual acompanhe filmagem real sem deslizar.

**Como praticar:** Rastreie plano de 5s filmado por você e coloque um objeto 3D estacionário.

**Critério de aceite:** Solve e erro registrados, composição revisada ao longo do plano.

**Fonte primária de estudo:** https://docs.blender.org/manual/en/latest/movie_clip/tracking/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 11 — VFX, partículas, volumes e simulações

**O que é:** Produzir fumaça, água, fogo, tecidos e destruição conforme plataforma e licenças.

**Por que importa:** Simulações exigem memória, caches e previsibilidade.

**Como praticar:** Crie pequena fumaça e exporte cache simples; compare prévia e render.

**Critério de aceite:** Parâmetros, versão e cache rastreáveis; sem exceder orçamento do alvo.

**Fonte primária de estudo:** https://www.openvdb.org/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 12 — Luz, câmera, render e passes

**O que é:** Escolher rasterização ou path tracing, configurar lente, HDRI, sombras, profundidade, EXR e passes.

**Por que importa:** Cena que funciona num render offline pode ser inviável em Quest ou web.

**Como praticar:** Faça render de objeto com duas câmeras e uma luz, produza preview e EXR.

**Critério de aceite:** Luz e câmera documentadas, render reproduzível e passes recuperáveis.

**Fonte primária de estudo:** https://www.openexr.com/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 13 — Som, montagem, motion graphics e narrativa

**O que é:** Planejar música/licenças, timing, textos, legendas, animação de logos e integração sonora.

**Por que importa:** Anúncio, cinema e educação dependem de clareza audiovisual.

**Como praticar:** Crie filme publicitário fictício de 10 segundos com três planos e texto legível.

**Critério de aceite:** Sequência com direitos de áudio claros, legendas e aprovação narrativa.

**Fonte primária de estudo:** https://www.aswf.io/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 14 — Otimização por destino

**O que é:** Controlar triângulos, instancing, draw calls, tamanho de textura, compressão, memória e tempos.

**Por que importa:** Web, mobile e XR têm budgets distintos de workstation cinematográfica.

**Como praticar:** Meça GLB 4K, 2K e 1K no celular; compare carga/legibilidade.

**Critério de aceite:** Tabela antes/depois de bytes, FPS/frame time, GPU e contexto de hardware.

**Fonte primária de estudo:** https://www.khronos.org/gltf/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 15 — Intercâmbio, contratos e dependências

**O que é:** Escolher BLEND/FBX/GLB/USD/USDZ/EXR/VDB/IFC por destino, com hashes e versões.

**Por que importa:** Evita aprisionamento a ferramenta e conversão quebrada.

**Como praticar:** Exporte GLB e FBX de cena própria, reimporte e liste as perdas observadas.

**Critério de aceite:** Manifesto e matriz de compatibilidade, fonte editável preservada.

**Fonte primária de estudo:** https://openusd.org/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 16 — Interação, distribuição AR e runtime

**O que é:** Selecionar model-viewer, Three.js, Unreal, Camera Kit, Effect House, Meta XR ou outra pilha apropriada.

**Por que importa:** Não existe um único build AR que funcione em todas as plataformas sem adaptação.

**Como praticar:** Monte protótipo de produto para site e teste fallback sem AR.

**Critério de aceite:** Runtime demonstrado em dispositivo específico, sem afirmar suporte universal.

**Fonte primária de estudo:** https://modelviewer.dev/docs/index.html

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 17 — Segurança, direitos e acessibilidade

**O que é:** Revisar licenças, uploads, autorização de captura, controle de câmera, fallback, teclado e movimento reduzido.

**Por que importa:** Um protótipo técnicamente bom ainda pode violar direito ou excluir usuários.

**Como praticar:** Teste falha no carregamento, teclado e outro aparelho; confirme licença por asset.

**Critério de aceite:** Assinatura de decisão dos gates críticos; sem bloqueios abertos.

**Fonte primária de estudo:** https://www.w3.org/WAI/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## 18 — Entrega, auditoria e evolução

**O que é:** Registrar fontes, versões, métricas, testes, screenshots, arquivos editáveis e plano de manutenção.

**Por que importa:** Permite corrigir e migrar sem perder investimento intelectual e comercial.

**Como praticar:** Faça pacote com origem, runtime, manifesto de licença, relatório de testes e rollback.

**Critério de aceite:** Artefato rastreável + checklist aceito no escopo, não 100% presumido.

**Fonte primária de estudo:** https://spdx.org/licenses/

**Cuidado ECP/Coliseu:** use a fonte no contexto da ferramenta, versão e dispositivo; **não** transforme exemplo de software em certificação de uso comercial ou compatibilidade universal.


## Mini-projetos com rotas diferentes

| Destino | Etapas centrais | Prova |
|---|---|---|
| Produto 3D para e-commerce | 1–7, 12, 14–18 | GLB no site com conversão/fallback e métrica mobile |
| Filme publicitário 3D | 1–13, 15, 17–18 | Sequência renderizada, passes e trilha sonora autorizada |
| Personagem animado para game | 1–9, 12, 14–18 | Animação sem clipping em build do motor |
| Cenário de produção virtual | 1–7, 10–12, 14–18 | Teste de palco/LED e sincronização, não só preview |
| Arquitetura/indústria | 1–7, 12, 14–18 | Dimensão coerente, IFC/STEP e render validado |
| Lens AR social | 1–7, 9, 12, 14–18 | Lens aprovada na plataforma real, não só editor |

## Padrão de evidência para todos os exercícios

```text
ID-etapa / Objetivo / Ambiente e versões / Autor e fontes
Artefato original / Exportação / Licença por item
Teste executado / Dispositivo / Evidência / Resultado
Falhas reproduzidas / Solução / Pendência / Revisor
```

**Este currículo não substitui prática orientada ou aprovação profissional externa.**
