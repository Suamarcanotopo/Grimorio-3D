# 01 · Conceitos fundamentais

**15 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://docs.blender.org/manual/pt/4.5/index.html

### 1. 3D

**O que é:** Representação de objetos com largura, altura e profundidade em coordenadas espaciais.

**Por que importa:** Permite representar volume, posição e escala.

**Como praticar:** Compare cubo real com objeto no viewport.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 2. Viewport

**O que é:** Janela de trabalho onde a cena é visualizada e editada.

**Por que importa:** Visualização prévia não é necessariamente render final.

**Como praticar:** Alterne visualizações de material e câmera.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 3. Cena (Scene)

**O que é:** Conjunto de objetos, luzes, câmeras e configurações.

**Por que importa:** Organiza a produção e a exportação.

**Como praticar:** Separe cenas de produto e de testes.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 4. Objeto (Object)

**O que é:** Unidade manipulável que referencia geometria ou outros dados.

**Por que importa:** Pivô, escala e hierarquia afetam exportação.

**Como praticar:** Nomeie objetos de maneira semântica.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 5. Coordenadas XYZ

**O que é:** Três eixos que definem localização no espaço.

**Por que importa:** Evita trocar orientação e posicionamento.

**Como praticar:** Teste subir no eixo Z no Blender.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 6. Transform (transformação)

**O que é:** Localização, rotação e escala de um objeto.

**Por que importa:** Escala não aplicada provoca falhas de exportação e física.

**Como praticar:** Confira transformações antes do rig.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 7. Pivot/Origin (origem)

**O que é:** Ponto de referência de rotação, escala e posição.

**Por que importa:** Porta deve girar pela dobradiça, não pelo centro.

**Como praticar:** Reposicione a origem de uma porta.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 8. Unidades de cena

**O que é:** Medidas usadas para representar tamanho físico.

**Por que importa:** AR e engenharia exigem escala real.

**Como praticar:** Crie um cubo com dimensão conhecida em metros.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 9. Câmera

**O que é:** Ponto de vista virtual com propriedades de lente.

**Por que importa:** Define enquadramento e perspectiva.

**Como praticar:** Teste uma câmera de produto.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 10. Focal length (distância focal)

**O que é:** Parâmetro de lente que afeta campo de visão.

**Por que importa:** Altera percepção de proporções.

**Como praticar:** Compare lentes curta e longa na mesma cena.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 11. Clip planes (planos de corte)

**O que é:** Limites de proximidade e distância visíveis pela câmera.

**Por que importa:** Cortes errados ocultam objetos.

**Como praticar:** Ajuste near/far sem exceder o necessário.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 12. Coleção (Collection)

**O que é:** Agrupamento lógico de objetos em cenas Blender.

**Por que importa:** Facilita versionamento e exportação por grupo.

**Como praticar:** Crie coleções produto, luz, câmeras e auxiliares.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 13. Hierarchy (hierarquia)

**O que é:** Relações pai-filho entre objetos e controles.

**Por que importa:** Transformações se propagam entre elementos.

**Como praticar:** Vincule rodas ao corpo de um veículo.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 14. Parenting (parentalidade)

**O que é:** Atribuição de objeto pai para outro.

**Por que importa:** Simplifica animação coordenada.

**Como praticar:** Mova o objeto pai e observe os filhos.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html

### 15. Instancing (instanciação)

**O que é:** Reutilização de geometria em múltiplas posições.

**Por que importa:** Economiza memória e facilita mudanças.

**Como praticar:** Repita árvores como instâncias.

**Onde aprender:** https://docs.blender.org/manual/pt/4.5/index.html
