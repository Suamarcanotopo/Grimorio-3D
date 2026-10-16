# 03 · UV, texturas, materiais e renderização

**27 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 1. UV Mapping (mapeamento UV)

**O que é:** Correspondência da superfície 3D com coordenadas 2D.

**Por que importa:** Define localização de pixels na malha.

**Como praticar:** Abra caixa em ilhas UV.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 2. Seam (costura UV)

**O que é:** Corte definido para abrir a superfície.

**Por que importa:** Controla distorção e posição das ilhas.

**Como praticar:** Marque costuras nas bordas ocultas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 3. UV Island (ilha UV)

**O que é:** Conjunto contínuo de faces no mapa UV.

**Por que importa:** Permite organizar o atlas de texturas.

**Como praticar:** Separe base, tampa e laterais.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 4. Unwrap (desdobramento UV)

**O que é:** Operação que transforma faces em ilhas.

**Por que importa:** Prepara pintura e baking.

**Como praticar:** Use checkerboard para inspecionar estiramento.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 5. Texel density (densidade de pixels na superfície)

**O que é:** Quantidade de pixels por unidade de área 3D.

**Por que importa:** Evita resolução desigual entre peças.

**Como praticar:** Compare um material entre objetos de tamanhos distintos.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 6. UV Packing (empacotamento UV)

**O que é:** Distribuição das ilhas em espaço de textura.

**Por que importa:** Aproveita a imagem e reduz desperdício.

**Como praticar:** Deixe margens apropriadas entre ilhas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 7. Texture Atlas (atlas de texturas)

**O que é:** Imagem compartilhada por objetos ou materiais.

**Por que importa:** Pode reduzir troca de materiais e draw calls.

**Como praticar:** Agrupe props pequenos.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 8. UDIM — U-Dimension Tiles (blocos UV numerados)

**O que é:** Conjunto de imagens associado a tiles UV distintos.

**Por que importa:** Ajuda em personagens de alta qualidade; não é universal no runtime.

**Como praticar:** Cheque suporte do exportador escolhido.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 9. PBR — Physically Based Rendering (renderização fisicamente baseada)

**O que é:** Modelo de materiais coerentes com propriedades de superfície.

**Por que importa:** Melhora consistência entre luzes e ambientes.

**Como praticar:** Compare plástico e metal sob HDRI.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 10. Albedo/Base Color (cor base)

**O que é:** Cor principal da superfície sem iluminação embutida.

**Por que importa:** Separar cor de sombras evita resultado inconsistente.

**Como praticar:** Use textura base color sem sombras pintadas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 11. Metallic (metalicidade)

**O que é:** Parâmetro que define comportamento de material metálico.

**Por que importa:** Altera reflexão e resposta à luz.

**Como praticar:** Compare metallic 0 e 1.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 12. Roughness (rugosidade)

**O que é:** Controle de microaspereza e nitidez de reflexos.

**Por que importa:** Distingue metal polido de fosco.

**Como praticar:** Teste 0.1 e 0.8.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 13. Normal Map (mapa de normais)

**O que é:** Textura que simula orientação microscópica da superfície.

**Por que importa:** Cria relevo aparente com pouca geometria.

**Como praticar:** Verifique convenção de eixo verde.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 14. AO — Ambient Occlusion (oclusão ambiente)

**O que é:** Aproxima escurecimento em cantos e contato.

**Por que importa:** Aumenta leitura de forma, mas pode exagerar sujeira.

**Como praticar:** Compare com/sem AO.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 15. Height Map (mapa de altura)

**O que é:** Imagem que representa diferenças de altitude/relevo.

**Por que importa:** Usada em displacement e parallax.

**Como praticar:** Teste em ladrilho.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 16. Displacement (deslocamento)

**O que é:** Alteração efetiva ou aparente da superfície a partir de altura.

**Por que importa:** Adiciona silhueta real quando geometria permite.

**Como praticar:** Compare com normal map.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 17. Baking (gravação em textura)

**O que é:** Transfere detalhes de geometria/iluminação para mapas.

**Por que importa:** Reduz necessidade de polígonos e custo de runtime.

**Como praticar:** Faça bake de normal do high-poly ao low-poly.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 18. Tangent Space (espaço tangente)

**O que é:** Referencial local utilizado em muitos normal maps.

**Por que importa:** Incompatibilidade gera relevo invertido.

**Como praticar:** Compare resultados Blender e destino.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 19. sRGB (espaço de cor perceptual)

**O que é:** Codificação comum de imagens de cor.

**Por que importa:** Não deve ser tratada como dado linear para mapas técnicos.

**Como praticar:** Use sRGB para Base Color, Non-Color para dados.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 20. Linear Color (cor linear)

**O que é:** Representação proporcional à intensidade luminosa.

**Por que importa:** Necessária em cálculos de shading corretos.

**Como praticar:** Confira pipeline de color management.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 21. HDRI — High Dynamic Range Image (imagem de alto alcance dinâmico)

**O que é:** Ambiente de iluminação contendo intensidades amplas.

**Por que importa:** Permite reflexos e luz ambiental realistas.

**Como praticar:** Ilumine esfera metálica com panorama.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 22. Shader (programa de superfície)

**O que é:** Conjunto de instruções que determina aparência na renderização.

**Por que importa:** Personaliza materiais e pode sobrecarregar GPU.

**Como praticar:** Comece por Principled BSDF.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 23. BSDF — Bidirectional Scattering Distribution Function (função de espalhamento bidirecional)

**O que é:** Modelo matemático de interação entre luz e superfície.

**Por que importa:** Fundamenta diferentes materiais realistas.

**Como praticar:** Estude Principled BSDF no Blender.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 24. Ray Tracing (traçado de raios)

**O que é:** Simulação de trajetórias de luz.

**Por que importa:** Melhora reflexos/sombras com custo maior.

**Como praticar:** Compare cena com render em tempo real.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 25. Path Tracing (traçado de caminhos)

**O que é:** Método de iluminação global que amostra percursos de luz.

**Por que importa:** Produz resultados realistas com ruído/amostragem.

**Como praticar:** Teste Cycles com samples graduais.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 26. Denoising (remoção de ruído)

**O que é:** Redução de granulação em render.

**Por que importa:** Acelera preview, pode eliminar detalhes finos.

**Como praticar:** Compare antes/depois.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

### 27. Render Pass (passe de render)

**O que é:** Saída separada como cor, sombra ou profundidade.

**Por que importa:** Facilita composição e correções sem refazer tudo.

**Como praticar:** Exporte passe de sombra.

**Onde aprender:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/
