# 13 · AR espacial, rastreamento e realidades imersivas

**18 conceitos**. Cada verbete explica a técnica, sua importância e um teste que pode ser reproduzido com material próprio.

[Índice do Glossário](README.md) · [Trilhas profissionais](../NICHOS/README.md)

### 1. Depth API (API de profundidade)

**O que é:** Tecnologia que estima distância de elementos vistos pela câmera.

**Por que importa:** Permite oclusão realista e interação espacial.

**Como praticar:** Teste mão passando à frente de objeto.

**Onde aprender:** https://developers.google.com/ar

### 2. Geospatial API (API geoespacial)

**O que é:** Conjunto de recursos AR associados a posições do mundo físico.

**Por que importa:** Viabiliza experiências AR ao ar livre.

**Como praticar:** Coloque objeto em posição de teste autorizada.

**Onde aprender:** https://developers.google.com/ar

### 3. VPS — Visual Positioning System (posicionamento visual)

**O que é:** Estimativa de localização por correspondência visual do ambiente.

**Por que importa:** Pode permitir ancoragem precisa em áreas cobertas.

**Como praticar:** Confira disponibilidade VPS no local de teste.

**Onde aprender:** https://developers.google.com/ar

### 4. Cloud Anchor (âncora em nuvem)

**O que é:** Referência espacial compartilhada entre sessões ou dispositivos.

**Por que importa:** Permite experiência multiusuário em espaço físico.

**Como praticar:** Compartilhe posição entre dois aparelhos compatíveis.

**Onde aprender:** https://developers.google.com/ar

### 5. Geospatial Anchor (âncora geográfica)

**O que é:** Posicionamento de conteúdo virtual por coordenadas geográficas e altitude.

**Por que importa:** Ajuda criar camadas de informação urbana.

**Como praticar:** Teste WGS84, terreno e cobertura.

**Onde aprender:** https://developers.google.com/ar

### 6. Terrain Anchor (âncora de terreno)

**O que é:** Âncora relativa ao modelo da superfície do terreno.

**Por que importa:** Reduz necessidade de informar altitude absoluta.

**Como praticar:** Posicione um objeto acima de solo autorizado.

**Onde aprender:** https://developers.google.com/ar

### 7. Rooftop Anchor (âncora de cobertura)

**O que é:** Âncora que usa altitude da cobertura de estrutura.

**Por que importa:** Útil para AR urbana e referências prediais.

**Como praticar:** Demonstre marcador em edifício de simulação.

**Onde aprender:** https://developers.google.com/ar

### 8. Streetscape Geometry (geometria urbana)

**O que é:** Dados de formas de edifícios e terreno usados em AR geoespacial.

**Por que importa:** Auxilia oclusão e alinhamento de conteúdo.

**Como praticar:** Teste frente de prédio com aparelho suportado.

**Onde aprender:** https://developers.google.com/ar

### 9. Environment Meshing (malha do ambiente)

**O que é:** Reconstrução de superfícies físicas em malhas espaciais.

**Por que importa:** Ajuda interação de objetos virtuais com paredes e mesas.

**Como praticar:** Teste colisão de bola virtual em mesa.

**Onde aprender:** https://developers.google.com/ar

### 10. Scene Understanding (compreensão de cena)

**O que é:** Identificação estruturada de paredes, chão, mesas e limites do ambiente.

**Por que importa:** Facilita aplicações MR em espaço real.

**Como praticar:** Compare âncoras de chão e parede.

**Onde aprender:** https://developers.google.com/ar

### 11. Hand Tracking (rastreamento de mãos)

**O que é:** Estimativa de postura e gesto das mãos.

**Por que importa:** Permite controles sem controle físico em XR.

**Como praticar:** Crie gesto simples sem armazenar biometria.

**Onde aprender:** https://developers.google.com/ar

### 12. Eye Tracking (rastreamento ocular)

**O que é:** Medição da direção aproximada do olhar quando suportado.

**Por que importa:** Ajuda interações e pesquisas, envolve privacidade sensível.

**Como praticar:** Teste em modo de demonstração com permissão.

**Onde aprender:** https://developers.google.com/ar

### 13. Foveated Rendering (renderização foveada)

**O que é:** Maior qualidade renderizada na região visual prioritária.

**Por que importa:** Pode economizar GPU em headsets compatíveis.

**Como praticar:** Compare qualidade e frame time em teste.

**Onde aprender:** https://developers.google.com/ar

### 14. Passthrough Occlusion (oclusão passthrough)

**O que é:** Composição entre imagem real capturada e conteúdo virtual com profundidade.

**Por que importa:** Aumenta coerência espacial em MR.

**Como praticar:** Teste mão na frente de prop em Quest compatível.

**Onde aprender:** https://developers.google.com/ar

### 15. Spatial Audio (áudio espacial)

**O que é:** Som posicionado e atenuado com base em orientação no espaço 3D.

**Por que importa:** Ajuda navegação e imersão.

**Como praticar:** Compare fontes à esquerda e atrás do usuário.

**Onde aprender:** https://developers.google.com/ar

### 16. Room Scale (escala de sala)

**O que é:** Área física definida para movimentação em VR/MR.

**Por que importa:** Influencia conforto, colisão e design de gameplay.

**Como praticar:** Trace limites de experiência em protótipo.

**Onde aprender:** https://developers.google.com/ar

### 17. Guardian/Boundary (limite de segurança)

**O que é:** Mecanismo de delimitação da área segura de usuário XR.

**Por que importa:** Evita colisões físicas com móveis ou paredes.

**Como praticar:** Crie teste que respeita limites da área.

**Onde aprender:** https://developers.google.com/ar

### 18. AR Session State (estado de sessão AR)

**O que é:** Condição de inicialização, rastreamento, pausa ou erro do runtime.

**Por que importa:** Permite recuperar falhas e informar o usuário.

**Como praticar:** Simule permissão negada e implemente mensagem.

**Onde aprender:** https://developers.google.com/ar

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se este material ajudar, deixe uma estrela no repositório.
