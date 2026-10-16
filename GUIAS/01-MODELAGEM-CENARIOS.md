# Modelagem, escultura, topologia e construção de cenários

**Quando usar:** criar objetos, personagens, ambientes, produtos, fachadas, universos de jogos e cenas cinematográficas.

## Sequência recomendada

1. **Brief e referência:** escala, objetivo, estilo (realista/estilizado), plataforma-alvo e licenças de referências.
2. **Blockout:** volumes primários sem detalhes, composição, câmera e proporções.
3. **Modelagem:** operações de extrusão, loops, bevels, hard-surface, sculpt quando necessário.
4. **Retopologia:** reestruturar malha para deformação ou jogo; controlar densidade e pole loops.
5. **Instanciação e modularidade:** peças reutilizáveis, pivôs e orientação consistentes.
6. **Detalhe e bake:** texturas de alto detalhe a partir de geometria complexa, quando fizer sentido.
7. **Level Design:** pontos de interesse, legibilidade de percursos, visibilidade, colisões e escala humana.
8. **Performance:** orçamento de materiais, polígonos, draw calls e LOD por plataforma; homologar no dispositivo de destino.

## Quatro estratégias

| Técnica | Boa para | Evite |
|---|---|---|
| Modelagem poligonal | Props, veículos, personagens e cenários gerais | Topologia desorganizada e normais invertidas |
| Escultura digital | Criaturas, rostos e superfícies orgânicas | Enviar high-poly para mobile sem retopologia |
| CAD/NURBS | Peças industriais, produto e precisão dimensional | Perder tolerâncias ao converter em triângulos |
| Procedural por nós | Rochas, vegetação, terrenos, arranha-céus, populações | Alterar seed/versão sem registrar o resultado |

## Truques profissionais

- Faça uma biblioteca de **materiais mestres** e instâncias, em vez de criar dezenas de materiais novos.
- Pense no **pivô**: portas giram na dobradiça; rodas no eixo; peças repetíveis têm origem coerente.
- Repetições não precisam de geometria copiada: use instancing e variantes.
- Crie **duas versões** quando necessário: fonte editável e exportação otimizada.
- Para hero assets próximos da câmera, gaste polígonos onde a silhueta muda; para background, priorize ilusão visual.

## Fontes de estudo

[Blender](https://www.blender.org/) · [Autodesk Maya](https://www.autodesk.com/products/maya/overview) · [Houdini](https://www.sidefx.com/products/houdini/) · [Houdini docs](https://www.sidefx.com/docs/) · [SpeedTree](https://speedtree.com/) · [Khronos glTF](https://www.khronos.org/gltf/).

**Prova necessária:** captura de blockout, arquivo editável, revisão de topologia, lista de assets e registro da licença por item.

[Índice geral](../INDEX.md)
