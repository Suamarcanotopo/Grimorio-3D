# 04 · Animação, física e tracking

**24 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://docs.blender.org/manual/en/latest/animation/

### 1. Rigging (armação de controles)

**O que é:** Construção de ossos, controles e relações para animar.

**Por que importa:** Torna movimentos repetíveis e editáveis.

**Como praticar:** Crie esqueleto simples.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 2. Armature (armação)

**O que é:** Objeto que contém estrutura de ossos no Blender.

**Por que importa:** Organiza deformação de personagem.

**Como praticar:** Adicione armature a personagem.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 3. Bone (osso digital)

**O que é:** Elemento de rig que transmite transformações.

**Por que importa:** Define juntas e hierarquia de movimentos.

**Como praticar:** Posicione ossos de braço.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 4. Skinning (vinculação de pele)

**O que é:** Associação entre vértices e esqueleto.

**Por que importa:** Permite deformar o modelo com os ossos.

**Como praticar:** Vincule malha ao rig.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 5. Weight Painting (pintura de pesos)

**O que é:** Atribuição de influência dos ossos sobre vértices.

**Por que importa:** Evita deformações bruscas.

**Como praticar:** Pinte pesos de ombro e cotovelo.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 6. IK — Inverse Kinematics (cinemática inversa)

**O que é:** Cálculo de articulações a partir de um alvo.

**Por que importa:** Útil para mãos e pés apoiados.

**Como praticar:** Trave pés ao chão com IK.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 7. FK — Forward Kinematics (cinemática direta)

**O que é:** Animação pelas rotações dos ossos em cadeia.

**Por que importa:** Boa para gestos fluidos e arcos de movimento.

**Como praticar:** Anime braço com FK.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 8. Keyframe (quadro-chave)

**O que é:** Registro de propriedade em instante definido.

**Por que importa:** É base da animação manual.

**Como praticar:** Crie dois keyframes de rotação.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 9. Interpolation (interpolação)

**O que é:** Regra usada entre quadros-chave.

**Por que importa:** Controla aceleração e suavidade.

**Como praticar:** Compare linear e Bézier.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 10. Graph Editor (editor de curvas)

**O que é:** Interface de curvas temporais de animação.

**Por que importa:** Permite evitar movimentos mecânicos.

**Como praticar:** Ajuste ease in/out.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 11. Dope Sheet (folha de exposição)

**O que é:** Visão temporal dos keyframes.

**Por que importa:** Ajuda a ordenar cenas e personagens.

**Como praticar:** Desloque grupo de poses.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 12. NLA — Nonlinear Animation (animação não linear)

**O que é:** Combinação de ações e clipes de movimento.

**Por que importa:** Facilita reutilizar animações.

**Como praticar:** Combine caminhar e acenar.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 13. Root Motion (movimento raiz)

**O que é:** Deslocamento do personagem codificado na animação.

**Por que importa:** Evita deslizar quando runtime controla locomoção.

**Como praticar:** Teste caminhada no motor de destino.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 14. Retargeting (transferência de rig)

**O que é:** Adaptação de movimento entre esqueletos.

**Por que importa:** Permite reaproveitar bibliotecas de animação.

**Como praticar:** Compare poses base e escala.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 15. Mocap — Motion Capture (captura de movimento)

**O que é:** Registro do movimento de atores ou objetos.

**Por que importa:** Acelera movimentos realistas.

**Como praticar:** Capture gesto consentido e limpe o movimento.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 16. Face Tracking (rastreamento facial)

**O que é:** Rastreamento de pontos ou expressões no rosto.

**Por que importa:** Anima avatar, mas envolve dados pessoais.

**Como praticar:** Teste somente com pessoa autorizada.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 17. Camera Tracking (rastreamento da câmera)

**O que é:** Reconstrução de movimento de câmera usando vídeo.

**Por que importa:** Integra 3D com filmagem real.

**Como praticar:** Rastreie pontos estáveis com parallax.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 18. Matchmoving (ajuste de câmera e cena)

**O que é:** Reconstrução compatível da câmera com ação filmada.

**Por que importa:** Mantém objeto 3D fixo no mundo do vídeo.

**Como praticar:** Ajuste perspectiva e escala.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 19. Planar Tracking (rastreamento planar)

**O que é:** Rastreamento de superfície aproximadamente plana.

**Por que importa:** Ideal para telas e embalagens, não substitui tracking 3D.

**Como praticar:** Substitua imagem de um monitor.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 20. Rotoscopy (rotoscopia)

**O que é:** Desenho de máscaras para separar elementos em vídeo.

**Por que importa:** Permite oclusão e composição realista.

**Como praticar:** Masque pessoa diante de objeto 3D.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 21. Keying (remoção de fundo)

**O que é:** Separação de fundo por cor ou outros sinais.

**Por que importa:** Comum em chroma key.

**Como praticar:** Remova fundo verde com bordas limpas.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 22. Physics Simulation (simulação física)

**O que é:** Cálculo de forças, colisões e movimento.

**Por que importa:** Cria interações consistentes.

**Como praticar:** Solte objeto rígido em plano.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 23. Cloth Simulation (simulação de tecidos)

**O que é:** Comportamento de tecido ao movimento e gravidade.

**Por que importa:** Útil para roupas e bandeiras.

**Como praticar:** Teste bandeira leve.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/

### 24. Particle System (sistema de partículas)

**O que é:** Grande conjunto de instâncias com regras.

**Por que importa:** Usado em poeira, fumaça, chuva e multidões.

**Como praticar:** Crie poeira ambiental.

**Onde aprender:** https://docs.blender.org/manual/en/latest/animation/
