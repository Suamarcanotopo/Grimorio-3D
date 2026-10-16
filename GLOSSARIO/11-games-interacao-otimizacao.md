# 11 · Games, interação e otimização em tempo real

**18 conceitos com definição, relevância, exercício e fonte técnica.** [Índice geral](README.md) · [18 etapas](../CURRICULO/ETAPAS-DA-PRODUCAO.md).

### 1. Static Mesh (malha estática)

**O que é:** Modelo geométrico não deformado por esqueleto durante reprodução.

**Por que importa:** Base de props e arquitetura em engines.

**Como praticar:** Importe caixa como Static Mesh.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 2. Skeletal Mesh (malha esquelética)

**O que é:** Modelo deformado por bones e skin weights.

**Por que importa:** Permite personagens e criaturas animadas.

**Como praticar:** Teste rotação de perna em engine.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 3. Prefab (objeto pré-fabricado)

**O que é:** Modelo reutilizável que combina objeto, componentes e configurações.

**Por que importa:** Facilita padronização de instâncias.

**Como praticar:** Crie prefab com colisão e material.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 4. Actor (ator do Unreal)

**O que é:** Entidade de mundo capaz de conter componentes e lógica.

**Por que importa:** Organiza cenário e eventos no Unreal.

**Como praticar:** Crie Actor com mesh e evento de clique.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 5. Collision Mesh (malha de colisão)

**O que é:** Geometria usada pelo sistema físico para detectar contatos.

**Por que importa:** Previne atravessamento e custo excessivo.

**Como praticar:** Compare colisão box e malha complexa.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 6. Broad Phase (fase ampla de colisão)

**O que é:** Etapa que identifica pares potenciais de contato.

**Por que importa:** Reduz processamento antes de testar detalhes.

**Como praticar:** Observe contagem de corpos ativos.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 7. Narrow Phase (fase precisa de colisão)

**O que é:** Teste detalhado entre objetos com possível contato.

**Por que importa:** Determina interseção e resposta física.

**Como praticar:** Faça teste de esfera e piso.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 8. NavMesh — Navigation Mesh (malha de navegação)

**O que é:** Representação de locais percorríveis por personagens controlados por IA.

**Por que importa:** Permite pathfinding consistente.

**Como praticar:** Gere área navegável e teste agente.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 9. Occlusion Query (consulta de oclusão)

**O que é:** Mecanismo para identificar objetos efetivamente cobertos na cena.

**Por que importa:** Ajuda culling de elementos invisíveis.

**Como praticar:** Teste cenário com uma parede diante de props.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 10. Instanced Static Mesh (malha estática instanciada)

**O que é:** Reutilização de um asset em várias posições com menor overhead.

**Por que importa:** Acelera florestas e objetos repetidos.

**Como praticar:** Compare cem árvores instanciadas.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 11. HLOD — Hierarchical Level of Detail (nível de detalhe hierárquico)

**O que é:** Simplificação ou substituição de conjuntos de objetos distantes.

**Por que importa:** Melhora performance de mundos grandes.

**Como praticar:** Compare draw calls por distância.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 12. Overdraw (redesenho de pixels)

**O que é:** Processamento repetido do mesmo pixel por transparências ou sobreposição.

**Por que importa:** Pode sobrecarregar GPU mesmo com poucas malhas.

**Como praticar:** Compare folhagem transparente e opaca.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 13. Shader Complexity (complexidade do shader)

**O que é:** Custo de avaliação de um material por pixel ou vértice.

**Por que importa:** Influencia carga GPU do jogo.

**Como praticar:** Meça material básico e material com ruído.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 14. Texture Streaming (streaming de textura)

**O que é:** Carregamento de mipmaps/texturas segundo necessidade da câmera.

**Por que importa:** Controla VRAM e popping.

**Como praticar:** Meça VRAM mudando distância da câmera.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 15. Frame Budget (orçamento por quadro)

**O que é:** Tempo máximo disponível por frame na taxa de quadros pretendida.

**Por que importa:** Torna performance requisito mensurável.

**Como praticar:** Meça tempo de quadro em aparelho real.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 16. Profiling GPU (medição gráfica)

**O que é:** Análise dos custos de renderização e GPU por etapa.

**Por que importa:** Localiza gargalos antes de otimizar.

**Como praticar:** Compare sombras, pós-processamento e partículas.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 17. Gameplay Loop (ciclo de jogo)

**O que é:** Sequência repetitiva de ação, feedback e objetivo.

**Por que importa:** Define interação além dos gráficos.

**Como praticar:** Prototipe coletar objeto e receber pontuação.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

### 18. Deterministic Replay (reprodução determinística)

**O que é:** Reexecução de eventos com resultados previsíveis sob condições definidas.

**Por que importa:** Ajuda depuração, testes e sincronismo.

**Como praticar:** Grave entradas e compare replay local.

**Onde aprender:** https://dev.epicgames.com/documentation/en-us/unreal-engine

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se este material ajudar, deixe uma estrela no repositório.
