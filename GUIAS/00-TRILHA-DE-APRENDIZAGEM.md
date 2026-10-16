# Trilha didática — do zero ao produto 3D

**Objetivo:** dominar fundamentos para entregar um objeto 3D útil sem pular etapas. Este é um roteiro de competências, não uma promessa de certificado.

## Três níveis

| Nível | Você aprende | Exercício | Evidência de conclusão |
|---|---|---|---|
| 1 — Fundamentos | Eixos XYZ, malha, faces, UV, material, câmera, luz, formatos | Criar e texturizar um objeto simples | Arquivo editável, imagem renderizada e GLB |
| 2 — Produção | Topologia, bake, rigging, animação, escalas, exportação | Personagem ou miniambiente animado | Projeto nativo, UV sem distorção crítica, animação testada |
| 3 — Entrega | LOD, compressão, licenças, acessibilidade, integração, métricas | Cena interativa em game ou website | Checklist, registro de desempenho, rastreabilidade de assets |

## Percurso de 10 exercícios

1. **Orientação espacial:** criar cubo, esfera, plano; mover, rotacionar e escalar, observar XYZ e unidades.
2. **Malha:** editar vértices, arestas e faces; entender normais e quads/tris.
3. **Topologia:** construir objeto low-poly, eliminar faces internas e non-manifold.
4. **UV:** marcar seams; aplicar checkerboard; corrigir stretch e organizar ilhas.
5. **Material PBR:** configurar cor base, rugosidade, metalicidade, normal e AO quando aplicável.
6. **Iluminação:** usar luz principal, preenchimento e fundo; comparar render em tempo real vs path tracing.
7. **Bake:** transferir detalhes high-poly para mapas de textura, com UV e imagem de destino.
8. **Animação:** introduzir keyframes, ciclo curto e pivôs ou esqueleto.
9. **Exportação:** preparar modelo GLB/glTF para destino; validar orientação, escala e materiais.
10. **Entrega:** executar teste mobile, medir carga, salvar metadados de origem e licença.

## Ponto de decisão: para que mercado?

- **Game:** colisão, LOD, rig e animação; prefira modelos modulares e orçamento de triângulos.
- **Website:** carregamento, responsividade, experiência de teclado e fallback; não renderizar o que não precisa.
- **Animação/filme:** continuidade visual, direção de arte, render passes, composição, keying e tracking.
- **Arquitetura/indústria:** unidades, precisão, materiais e origem dos dados; CAD/BIM pode preceder a malha.
- **XR:** latência e conforto visual; evitar animação excessiva ou acessos que dependam apenas de gestos.
- **Impressão 3D:** malha fechada e espessura; validar orientação, tolerâncias e material.

## Glossário mínimo

- **Malha (mesh):** rede de vértices, arestas e faces que forma o objeto 3D.
- **UV mapping (mapeamento UV):** disposição da superfície tridimensional sobre uma imagem 2D; U e V são coordenadas dessa imagem.
- **PBR (Physically Based Rendering — renderização baseada em propriedades físicas):** método de materiais que respondem coerentemente à luz.
- **LOD (Level of Detail — nível de detalhe):** versões de complexidade diferente para economizar processamento.
- **Rigging (preparação de controles):** montar esqueleto ou estrutura que permite animar.
- **Bake (gravar informações em textura):** transferir geometria, sombreamento ou outras propriedades para imagens.
- **GLB:** contêiner binário do padrão glTF; conveniente para entregar cena 3D na web.
- **Tracking (rastreamento):** recuperar movimento ou localização de câmera/elementos a partir de vídeo.
- **Mocap (motion capture — captura de movimento):** registrar movimentos reais para aplicá-los a personagens digitais.

**Fontes primárias:** [Blender Manual](https://docs.blender.org/manual/en/latest/), [Khronos glTF](https://www.khronos.org/gltf/), [W3C Web Accessibility Initiative](https://www.w3.org/WAI/).

[Índice geral](../INDEX.md)
