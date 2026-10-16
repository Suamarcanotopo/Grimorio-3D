# 05 · Engines, integração e pipeline

**21 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://www.khronos.org/gltf/

### 1. Game Engine (motor de jogo)

**O que é:** Ambiente que une renderização, entrada, física e lógica.

**Por que importa:** Transforma asset em experiência executável.

**Como praticar:** Compare Unity e Unreal para mesmo objeto.

**Onde aprender:** https://www.khronos.org/gltf/

### 2. Unreal Engine

**O que é:** Motor de jogos e experiências em tempo real da Epic.

**Por que importa:** Muito usado para jogos, cinema virtual e XR.

**Como praticar:** Importe asset para projeto de teste.

**Onde aprender:** https://www.khronos.org/gltf/

### 3. Blueprints (sistema visual Unreal)

**O que é:** Programação por nós no Unreal Engine.

**Por que importa:** Ajuda a criar lógica sem começar por C++.

**Como praticar:** Faça objeto reagir a clique.

**Onde aprender:** https://www.khronos.org/gltf/

### 4. Nanite

**O que é:** Sistema de geometria virtualizada da Unreal.

**Por que importa:** Ajuda a exibir modelos de alta complexidade em hardware compatível.

**Como praticar:** Consulte requisitos do projeto e plugin.

**Onde aprender:** https://www.khronos.org/gltf/

### 5. Lumen

**O que é:** Tecnologia de iluminação global/reflexos da Unreal.

**Por que importa:** Fornece luz dinâmica com custo de runtime.

**Como praticar:** Compare configuração sob orçamento real.

**Onde aprender:** https://www.khronos.org/gltf/

### 6. Unity

**O que é:** Motor para jogos, aplicações e experiências XR.

**Por que importa:** Alternativa multiplataforma para integração de assets.

**Como praticar:** Importe FBX com escala validada.

**Onde aprender:** https://www.khronos.org/gltf/

### 7. Godot

**O que é:** Motor aberto para desenvolvimento de jogos.

**Por que importa:** Adequado a fluxos independentes e aprendizado.

**Como praticar:** Monte cena com mesh e câmera.

**Onde aprender:** https://www.khronos.org/gltf/

### 8. glTF — GL Transmission Format (formato de transmissão de gráficos)

**O que é:** Padrão aberto de entrega de cenas e modelos.

**Por que importa:** Ajuda interoperabilidade e carregamento web.

**Como praticar:** Exporte GLB de um objeto.

**Onde aprender:** https://www.khronos.org/gltf/

### 9. GLB (glTF binário)

**O que é:** Arquivo único que empacota glTF e recursos.

**Por que importa:** Facilita publicação web de modelo pequeno.

**Como praticar:** Teste GLB em visualizador externo.

**Onde aprender:** https://www.khronos.org/gltf/

### 10. FBX — Filmbox (formato de intercâmbio)

**O que é:** Arquivo comum de geometria, rig e animações.

**Por que importa:** Muito usado em engines, mas não garante materiais idênticos.

**Como praticar:** Compare importação de rig em dois motores.

**Onde aprender:** https://www.khronos.org/gltf/

### 11. USD — Universal Scene Description (descrição universal de cenas)

**O que é:** Sistema extensível de composição de cenas.

**Por que importa:** Usado em pipelines complexos e colaboração.

**Como praticar:** Separe camadas de asset e cena.

**Onde aprender:** https://www.khronos.org/gltf/

### 12. USDZ

**O que é:** Pacote USD distribuído como arquivo único.

**Por que importa:** Usado em Quick Look e outros fluxos AR Apple.

**Como praticar:** Confirme texturas e escala no iPhone.

**Onde aprender:** https://www.khronos.org/gltf/

### 13. OBJ — Wavefront Object (malha Wavefront)

**O que é:** Formato geométrico simples.

**Por que importa:** Interoperável, mas não transporta rig completo.

**Como praticar:** Envie OBJ+MTL e imagens associadas.

**Onde aprender:** https://www.khronos.org/gltf/

### 14. STL — Stereolithography (malha para fabricação)

**O que é:** Superfície triangulada para impressão 3D.

**Por que importa:** Não conserva engenharia paramétrica.

**Como praticar:** Faça teste de watertight.

**Onde aprender:** https://www.khronos.org/gltf/

### 15. IFC — Industry Foundation Classes (classes fundamentais da indústria)

**O que é:** Padrão aberto de informação BIM.

**Por que importa:** Liga geometria a dados de construção.

**Como praticar:** Valide unidades e propriedades de porta.

**Onde aprender:** https://www.khronos.org/gltf/

### 16. LOD Chain (cadeia de nível de detalhe)

**O que é:** Seleção de variantes por distância ou condição.

**Por que importa:** Reduz custo de renderização.

**Como praticar:** Teste mudanças de nível sem saltos óbvios.

**Onde aprender:** https://www.khronos.org/gltf/

### 17. Draw Call (chamada de desenho)

**O que é:** Comando enviado para GPU desenhar uma parte.

**Por que importa:** Muitas chamadas aumentam carga de CPU/GPU.

**Como praticar:** Agrupe quando não perder flexibilidade.

**Onde aprender:** https://www.khronos.org/gltf/

### 18. Occlusion Culling (ocultação)

**O que é:** Evita desenhar elementos atrás de outros.

**Por que importa:** Melhora desempenho de ambientes densos.

**Como praticar:** Oculte sala fora da visão.

**Onde aprender:** https://www.khronos.org/gltf/

### 19. Frustum Culling (recorte por volume de câmera)

**O que é:** Ignora elementos fora do campo visual.

**Por que importa:** Evita trabalho invisível.

**Como praticar:** Mova objeto para fora da câmera.

**Onde aprender:** https://www.khronos.org/gltf/

### 20. Profiling (perfilamento)

**O que é:** Medição de gargalos de CPU, GPU, memória e rede.

**Por que importa:** Evita otimizar a parte errada.

**Como praticar:** Registre frames antes de alterar a cena.

**Onde aprender:** https://www.khronos.org/gltf/

### 21. Version Pinning (fixação de versão)

**O que é:** Registrar versões testadas de motor, plugins e dependências.

**Por que importa:** Protege contra quebras de atualização.

**Como praticar:** Salve lockfile e lista de SDKs.

**Onde aprender:** https://www.khronos.org/gltf/
