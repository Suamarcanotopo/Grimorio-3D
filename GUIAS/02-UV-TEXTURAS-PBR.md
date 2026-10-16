# UV, mapas, materiais, PBR, UDIM e baking

## Conceitos claros

**UV mapping (mapeamento UV)** abre uma superfície 3D como um molde de papel para definir onde cada pixel da textura será pintado. **UV islands (ilhas UV)** são pedaços desse molde; **seams (costuras)** determinam onde a superfície é cortada.

**PBR (Physically Based Rendering; renderização baseada em propriedades físicas)** representa superfícies com parâmetros coerentes. O fluxo mais comum usa **Base Color/Albedo** (cor sem luz), **Metallic** (metal ou dielétrico), **Roughness** (rugosidade), **Normal** (relevo aparente), **Ambient Occlusion/AO** (oclusão ambiente) e, conforme caso, **Height/Displacement**, **Opacity** e **Emission**.

**UDIM (U-Dimension; convenção de blocos de textura UV)** usa vários tiles de textura, úteis para personagens e assets de alta qualidade; verificar suporte no destino, pois não é solução universal para GLB em websites.

**Baking (gravação em mapas)** transfere detalhes da malha high-poly a texturas para exibição eficiente em low-poly.

## Exercício verificável

1. Crie um objeto com cavidades e superfícies curvas.
2. Aplique escala e confirme normais, seams e UV sem sobreposição indesejada.
3. Crie imagem checker; verifique deformações.
4. Faça bake de normal/AO usando origem high-poly e alvo low-poly quando necessário.
5. Monte material PBR e compare sob iluminação neutra e HDRI.
6. Exporte GLB e compare visual no Blender e no visualizador destino.
7. Registre orientação do normal map, espaço de cor, formato e resolução.

## O que evitar

| Erro | Consequência | Correção |
|---|---|---|
| Color map em modo linear incorreto | Cores lavadas ou contrastadas | Tratar sRGB vs dados corretamente |
| Normal maps invertidos | Iluminação parece vir do lado errado | Verificar convenção OpenGL/DirectX |
| UV comprimida/esticada | Padrão deformado e baixa qualidade | Checker + alinhamento da densidade de texel |
| Uso de 4K em objetos minúsculos | Consumo alto de VRAM e download | Reduzir resolução conforme tamanho na tela |
| UDIM sem suporte no motor | Texturas ausentes | Empacotar/associar material adequado |
| Bake sem alvo válido | Mapas vazios/incorretos | Configurar UV e imagem ativa corretamente |

## Fontes primárias

- [Manual de UV do Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/)
- [Blender Cycles Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)
- [Adobe Substance 3D Painter — Baking](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/baking/baking)
- [Adobe — trabalho com UDIM](https://www.adobe.com/learn/substance-3d-painter/web/working-with-uv-tiles-udim-in-substance-3d-painter)
- [KTX2 — formato de texturas comprimidas](https://registry.khronos.org/KTX/specs/2.0/ktxspec.v2.html)

[Índice geral](../INDEX.md)
