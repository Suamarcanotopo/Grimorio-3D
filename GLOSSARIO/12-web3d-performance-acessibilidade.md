# 12 · Web3D, performance e acessibilidade avançada

**18 conceitos**. Cada verbete explica a técnica, sua importância e um teste que pode ser reproduzido com material próprio.

[Índice do Glossário](README.md) · [Trilhas profissionais](../NICHOS/README.md)

### 1. Progressive Enhancement (melhoria progressiva)

**O que é:** Projeto que funciona sem recursos avançados e melhora em navegadores capazes.

**Por que importa:** Garante que falha de WebGL não bloqueie o conteúdo.

**Como praticar:** Crie página com CTA e imagem mesmo sem canvas.

**Onde aprender:** https://www.w3.org/WAI/

### 2. WebGL Context Loss (perda de contexto WebGL)

**O que é:** Falha ou reinício do contexto gráfico do navegador.

**Por que importa:** Pode apagar recursos de GPU e travar visualizador.

**Como praticar:** Simule perda de contexto e recarregue recurso.

**Onde aprender:** https://www.w3.org/WAI/

### 3. WebGPU Feature Detection (detecção WebGPU)

**O que é:** Verificação de capacidades de GPU antes de usar API avançada.

**Por que importa:** Evita erros em dispositivos sem suporte.

**Como praticar:** Implemente fallback para WebGL ou imagem.

**Onde aprender:** https://www.w3.org/WAI/

### 4. GLTFLoader (carregador glTF)

**O que é:** Componente usado para importar cenas glTF no Three.js.

**Por que importa:** Separa autoria de geometria e runtime web.

**Como praticar:** Carregue GLB próprio com logs de erro.

**Onde aprender:** https://www.w3.org/WAI/

### 5. Lazy Loading (carregamento sob demanda)

**O que é:** Transferência de recurso apenas quando necessário.

**Por que importa:** Reduz bytes iniciais e melhora carregamento da página.

**Como praticar:** Carregue o GLB ao aparecer no viewport.

**Onde aprender:** https://www.w3.org/WAI/

### 6. Intersection Observer (observador de interseção)

**O que é:** API que observa quando elementos entram na área visível.

**Por que importa:** Permite iniciar uma cena somente quando visível.

**Como praticar:** Ative render ao rolar página.

**Onde aprender:** https://www.w3.org/WAI/

### 7. DPR — Device Pixel Ratio (densidade de pixels)

**O que é:** Razão entre pixels físicos e CSS na tela.

**Por que importa:** DPR alto pode multiplicar custo gráfico.

**Como praticar:** Compare DPR 1 e 2 em mobile.

**Onde aprender:** https://www.w3.org/WAI/

### 8. Responsive Canvas (tela adaptável)

**O que é:** Canvas que acompanha dimensões e proporções do componente.

**Por que importa:** Impede distorção e overflow de interface.

**Como praticar:** Teste rotação de celular e resize.

**Onde aprender:** https://www.w3.org/WAI/

### 9. Shader Compilation (compilação de shader)

**O que é:** Preparação de programas gráficos para GPU.

**Por que importa:** Pode gerar travamento perceptível na primeira renderização.

**Como praticar:** Pré-aqueça material e meça stutter.

**Onde aprender:** https://www.w3.org/WAI/

### 10. Shader Cache (cache de shaders)

**O que é:** Armazenamento de resultados ou binários de shader para reutilização.

**Por que importa:** Pode reduzir repetição de compilação.

**Como praticar:** Compare primeira e segunda sessão.

**Onde aprender:** https://www.w3.org/WAI/

### 11. Asset Preload (pré-carregamento de recursos)

**O que é:** Antecipação de download de modelos ou texturas críticos.

**Por que importa:** Pode melhorar resposta, mas congestionar rede se excessivo.

**Como praticar:** Compare LCP com/sem preload do GLB.

**Onde aprender:** https://www.w3.org/WAI/

### 12. Draco Compression (compressão Draco)

**O que é:** Técnica de compressão de geometria glTF.

**Por que importa:** Reduz download com custo de decodificação.

**Como praticar:** Compare tamanho e tempo até interação.

**Onde aprender:** https://www.w3.org/WAI/

### 13. Meshopt Compression (compressão Meshopt)

**O que é:** Codificação para dados de malha com foco em performance.

**Por que importa:** Reduz payload em formatos compatíveis.

**Como praticar:** Teste viewer suportado e compare decode.

**Onde aprender:** https://www.w3.org/WAI/

### 14. KTX2/BasisU (textura compactada)

**O que é:** Contêiner e codificação de texturas de GPU para runtime.

**Por que importa:** Reduz armazenamento e custo de memória.

**Como praticar:** Compare memória de textura em Android.

**Onde aprender:** https://www.w3.org/WAI/

### 15. AR Modes (modos AR)

**O que é:** Opções específicas de plataforma para apresentar AR via navegador.

**Por que importa:** Determina se abre Scene Viewer, Quick Look ou WebXR.

**Como praticar:** Teste seleção e fallback por aparelho.

**Onde aprender:** https://www.w3.org/WAI/

### 16. Accessible Description (descrição acessível)

**O que é:** Descrição textual útil de um modelo quando 3D não é percebido.

**Por que importa:** Permite entendimento sem GPU ou visão de cena.

**Como praticar:** Escreva descrição funcional de produto.

**Onde aprender:** https://www.w3.org/WAI/

### 17. Keyboard Orbit (órbita por teclado)

**O que é:** Forma de controlar câmera sem depender do mouse.

**Por que importa:** Ajuda pessoas com restrição motora.

**Como praticar:** Teste foco, setas e saída do visualizador.

**Onde aprender:** https://www.w3.org/WAI/

### 18. Motion Sickness (cinetose em XR)

**O que é:** Desconforto causado por movimento, latência e conflito sensorial.

**Por que importa:** Exige render estável e padrões confortáveis.

**Como praticar:** Compare teleporte e movimento contínuo em protótipo.

**Onde aprender:** https://www.w3.org/WAI/

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se este material ajudar, deixe uma estrela no repositório.
