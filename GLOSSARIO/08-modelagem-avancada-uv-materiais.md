# 08 · Modelagem avançada, UV e materiais

**18 conceitos com definição, relevância, exercício e fonte técnica.** [Índice geral](README.md) · [18 etapas](../CURRICULO/ETAPAS-DA-PRODUCAO.md).

### 1. Blockout (bloqueio de formas)

**O que é:** Prototipagem volumétrica com geometrias simples antes do acabamento.

**Por que importa:** Permite validar escala e silhueta sem retrabalho.

**Como praticar:** Monte três variantes de produto com cubos e cilindros.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 2. Topology Budget (orçamento de geometria)

**O que é:** Limite planejado de complexidade da malha para o destino.

**Por que importa:** Ajuda a controlar memória e frame time.

**Como praticar:** Compare três versões do mesmo prop.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 3. Retopology Cage (malha-gaiola)

**O que é:** Malha auxiliar que controla projeção ou transferência entre alta e baixa resolução.

**Por que importa:** Minimiza artefatos de baking.

**Como praticar:** Faça projeção de normal com distância controlada.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 4. Shrinkwrap (aderência de geometria)

**O que é:** Projeção de vértices em superfície-alvo.

**Por que importa:** Acelera retopologia e conformação.

**Como praticar:** Faça aderir malha simples em escultura.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 5. Weighted Normals (normais ponderadas)

**O que é:** Cálculo de normais para melhorar aparência em faces planas e chanfros.

**Por que importa:** Reduz artefatos de shading hard-surface.

**Como praticar:** Compare bevel com e sem normais ponderadas.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 6. Auto Smooth (suavização controlada)

**O que é:** Uso de limites de aresta ou ângulo para organizar transições entre faces.

**Por que importa:** Preserva bordas duras e superfícies lisas.

**Como praticar:** Compare a borda de uma peça metálica.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 7. Triplanar Projection (projeção triplanar)

**O que é:** Texturização por três eixos sem depender exclusivamente de UV tradicional.

**Por que importa:** Acelera protótipos procedurais, com custos e limitações.

**Como praticar:** Aplique material a rocha com e sem UV.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 8. UV Overlap (sobreposição UV)

**O que é:** Ilhas que ocupam as mesmas coordenadas de textura.

**Por que importa:** Pode economizar textura ou estragar bake quando não intencional.

**Como praticar:** Pinte ilhas espelhadas e teste diferenças.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 9. UV Padding (margem de textura)

**O que é:** Distância entre ilhas para evitar vazamento nos mipmaps.

**Por que importa:** Evita costuras visíveis em runtime.

**Como praticar:** Gere bake com margens distintas.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 10. Mipmapping (mipmaps)

**O que é:** Conjunto de texturas progressivamente menores segundo escala de visualização.

**Por que importa:** Reduz cintilação e custo de amostragem.

**Como praticar:** Inspecione textura distante com mipmaps.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 11. Texture Compression (compressão de textura)

**O que é:** Codificação para reduzir espaço e banda de imagens de material.

**Por que importa:** Ajuda memória e download, com perdas possíveis.

**Como praticar:** Compare base color PNG, WebP e KTX2 no destino.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 12. Channel Packing (empacotamento de canais)

**O que é:** Uso dos canais RGB/A para armazenar diferentes dados de material.

**Por que importa:** Economiza arquivos e acessos de textura.

**Como praticar:** Crie textura ORM quando o motor permitir.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 13. ORM — Occlusion Roughness Metallic (mapa ORM)

**O que é:** Convenção que armazena AO, roughness e metallic em canais distintos.

**Por que importa:** Padroniza PBR no glTF e alguns motores.

**Como praticar:** Compare canais R, G, B de um arquivo ORM.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 14. Material Variant (variante de material)

**O que é:** Opção de aparência para o mesmo modelo 3D.

**Por que importa:** Permite configuradores sem duplicar malha.

**Como praticar:** Crie três cores para o mesmo produto.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 15. SDF — Signed Distance Field (campo de distância com sinal)

**O que é:** Representação da distância de pontos a uma superfície.

**Por que importa:** Serve a efeitos, volume e algumas operações de geometria.

**Como praticar:** Modele esfera SDF e visualize isosuperfície.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 16. Topology Flow (fluxo de topologia)

**O que é:** Direção e continuidade das arestas segundo forma ou deformação.

**Por que importa:** Melhora animação e subdivisão.

**Como praticar:** Trace loops ao redor de olhos ou cotovelos.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 17. Baking Cage Bias (deslocamento de projeção)

**O que é:** Ajuste entre superfície receptora e emissora para mapas de bake.

**Por que importa:** Diminui manchas e projeções equivocadas.

**Como praticar:** Compare normal bake com duas distâncias.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

### 18. Pivot Alignment (alinhamento de origem)

**O que é:** Organização da origem do objeto para rotações e transformações previsíveis.

**Por que importa:** Essencial a portas, robôs e componentes interativos.

**Como praticar:** Teste dobradiça com pivô correto.

**Onde aprender:** https://github.com/KhronosGroup/3DC-Asset-Creation

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se este material ajudar, deixe uma estrela no repositório.
