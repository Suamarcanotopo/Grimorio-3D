# 02 · Malhas, modelagem e escultura

**20 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 1. Mesh (malha)

**O que é:** Representação por vértices, arestas e faces.

**Por que importa:** Base de grande parte dos modelos em jogos e web.

**Como praticar:** Inspecione a malha em Edit Mode.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 2. Vertex (vértice)

**O que é:** Ponto que compõe a geometria.

**Por que importa:** É a unidade mais simples da malha.

**Como praticar:** Mova um vértice e observe superfícies próximas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 3. Edge (aresta)

**O que é:** Ligação entre dois vértices.

**Por que importa:** Controla contornos e fluxo de topologia.

**Como praticar:** Crie um loop de arestas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 4. Face (face)

**O que é:** Superfície definida por vértices.

**Por que importa:** É triangulada na maioria dos renderizadores.

**Como praticar:** Confira faces externas e internas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 5. Quad (quadrilátero)

**O que é:** Face com quatro lados.

**Por que importa:** Favorece certos fluxos de deformação e edição.

**Como praticar:** Modele superfícies orgânicas com quads coerentes.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 6. Tri (triângulo)

**O que é:** Face com três lados.

**Por que importa:** Unidade final usual em GPU e motores.

**Como praticar:** Observe triangulação antes de exportar.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 7. N-gon (polígono complexo)

**O que é:** Face com mais de quatro lados.

**Por que importa:** Pode produzir triangulação inesperada.

**Como praticar:** Evite em articulações e superfícies críticas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 8. Topology (topologia)

**O que é:** Organização das conexões de geometria.

**Por que importa:** Influencia deformação, shading e edição.

**Como praticar:** Revise loops em cotovelos.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 9. Edge loop (anel de arestas)

**O que é:** Sequência contínua de arestas.

**Por que importa:** Permite cortes uniformes e controle da forma.

**Como praticar:** Adicione loops junto a uma articulação.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 10. Extrude (extrusão)

**O que é:** Criação de volume a partir de faces ou arestas.

**Por que importa:** Ferramenta fundamental de modelagem.

**Como praticar:** Extrude uma parede de um plano.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 11. Bevel (chanfro)

**O que é:** Suavização ou corte de cantos.

**Por que importa:** Quase todo produto real tem bordas não infinitamente afiadas.

**Como praticar:** Adicione bevel moderado.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 12. Subdivision Surface (subdivisão)

**O que é:** Aumento e suavização controlada da malha.

**Por que importa:** Aproxima curvas sem modelar cada ponto.

**Como praticar:** Compare subdivisões 0, 1 e 2.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 13. Boolean (operação booleana)

**O que é:** União, subtração ou interseção entre sólidos.

**Por que importa:** Ajuda em hard-surface e arquitetura.

**Como praticar:** Recorte uma janela em parede.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 14. Hard-surface

**O que é:** Modelagem de peças rígidas e superfícies industriais.

**Por que importa:** Demanda precisão de silhueta e normais.

**Como praticar:** Modele pequeno equipamento.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 15. Digital Sculpting (escultura)

**O que é:** Alteração orgânica da geometria com pincéis.

**Por que importa:** Ideal para criaturas, rostos e detalhes.

**Como praticar:** Esculpa uma rocha e remalhe.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 16. Retopology (retopologia)

**O que é:** Reconstrução de geometria para topologia mais útil.

**Por que importa:** Reduz custo e melhora animação.

**Como praticar:** Recrie malha leve a partir de escultura.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 17. Normal (normal de superfície)

**O que é:** Vetor perpendicular à face ou vértice.

**Por que importa:** Afeta iluminação e orientação de faces.

**Como praticar:** Ative visualização de normais.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 18. Non-manifold (geometria não-manifold)

**O que é:** Malha com conectividade inadequada a um sólido fechado.

**Por que importa:** Prejudica física e impressão 3D.

**Como praticar:** Use análise de non-manifold no Blender.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 19. Decimation (decimação)

**O que é:** Redução de quantidade de polígonos.

**Por que importa:** Ajuda na entrega para dispositivos fracos.

**Como praticar:** Compare forma antes e depois.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/

### 20. LOD — Level of Detail (nível de detalhe)

**O que é:** Variantes geométricas por distância/qualidade.

**Por que importa:** Poupa processamento em jogos e XR.

**Como praticar:** Gere versões alta, média e baixa.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/
