# 06 · Websites, acessibilidade e AR/XR

**24 conceitos** · [Voltar ao índice](README.md) (use [índice geral](../GLOSSARIO/README.md))

Para cada termo, entenda **o que é**, **por que importa** e **como aplicar**. Nenhum exemplo implica compatibilidade universal.

**Manual de referência:** https://modelviewer.dev/docs/

### 1. WebGL — Web Graphics Library (biblioteca gráfica web)

**O que é:** API para gráficos 3D no navegador.

**Por que importa:** Permite cenas 3D sem plugin tradicional.

**Como praticar:** Teste canvas 3D em navegador comum.

**Onde aprender:** https://modelviewer.dev/docs/

### 2. WebGPU — Web Graphics Processing Unit (API gráfica web de GPU)

**O que é:** API moderna de computação e gráficos para navegadores.

**Por que importa:** Pode oferecer capacidades adicionais onde suportada.

**Como praticar:** Detecte suporte e ofereça fallback.

**Onde aprender:** https://modelviewer.dev/docs/

### 3. Three.js

**O que é:** Biblioteca JavaScript para construir cenas 3D.

**Por que importa:** Base de vários sites interativos.

**Como praticar:** Exiba cubo com câmera e luz.

**Onde aprender:** https://modelviewer.dev/docs/

### 4. React Three Fiber (renderizador Three para React)

**O que é:** Integra Three.js a componentes React.

**Por que importa:** Reutiliza cenas ligadas a estado de interfaces.

**Como praticar:** Comece com Canvas e mesh.

**Onde aprender:** https://modelviewer.dev/docs/

### 5. model-viewer (componente web)

**O que é:** Componente HTML para apresentar modelos 3D e AR em dispositivos compatíveis.

**Por que importa:** Começo simples para produto no site.

**Como praticar:** Mostre GLB com camera-controls e ar.

**Onde aprender:** https://modelviewer.dev/docs/

### 6. AR — Augmented Reality (realidade aumentada)

**O que é:** Posicionamento ou composição de conteúdo virtual no ambiente real.

**Por que importa:** Permite experimentar produtos no espaço do cliente.

**Como praticar:** Coloque objeto 3D no chão da sala.

**Onde aprender:** https://modelviewer.dev/docs/

### 7. VR — Virtual Reality (realidade virtual)

**O que é:** Experiência visual envolvente em ambiente predominantemente virtual.

**Por que importa:** Útil para simulações, jogos e experiências imersivas.

**Como praticar:** Teste com headset compatível.

**Onde aprender:** https://modelviewer.dev/docs/

### 8. MR — Mixed Reality (realidade mista)

**O que é:** Experiência que integra conteúdo digital e ambiente físico.

**Por que importa:** Permite interação com paredes, chão e objetos detectados.

**Como praticar:** Use scene understanding quando disponível.

**Onde aprender:** https://modelviewer.dev/docs/

### 9. XR — Extended Reality (realidade estendida)

**O que é:** Termo guarda-chuva que inclui AR, VR e MR.

**Por que importa:** Evita confundir modalidade e hardware.

**Como praticar:** Classifique seu projeto por interação e display.

**Onde aprender:** https://modelviewer.dev/docs/

### 10. WebXR — Web Extended Reality Device API (API de dispositivos XR para web)

**O que é:** Acesso a sessões imersivas por navegadores compatíveis.

**Por que importa:** Permite experiências AR/VR sem app nativo em alguns dispositivos.

**Como praticar:** Teste suporte por navegador e dispositivo.

**Onde aprender:** https://modelviewer.dev/docs/

### 11. ARCore

**O que é:** Plataforma Google de capacidades AR em Android.

**Por que importa:** Ajuda ancoragem, detecção de planos e rastreamento.

**Como praticar:** Teste compatibilidade do smartphone.

**Onde aprender:** https://modelviewer.dev/docs/

### 12. ARKit

**O que é:** Framework Apple para AR em dispositivos compatíveis.

**Por que importa:** Oferece experiências nativas de AR no ecossistema Apple.

**Como praticar:** Use projeto de teste com detecção de planos.

**Onde aprender:** https://modelviewer.dev/docs/

### 13. Scene Viewer

**O que é:** Visualizador Google de 3D/AR em Android.

**Por que importa:** Permite abrir modelo a partir de link web.

**Como praticar:** Use model-viewer com AR e fallback.

**Onde aprender:** https://modelviewer.dev/docs/

### 14. Quick Look AR

**O que é:** Visualizador Apple de objetos USDZ.

**Por que importa:** Permite abrir AR em iPhone/iPad compatível.

**Como praticar:** Teste modelo USDZ real no Safari.

**Onde aprender:** https://modelviewer.dev/docs/

### 15. Passthrough (visão do ambiente)

**O que é:** Vídeo ou imagem do mundo real integrado ao headset.

**Por que importa:** Base visual de várias experiências MR.

**Como praticar:** Teste transparência e segurança espacial.

**Onde aprender:** https://modelviewer.dev/docs/

### 16. Spatial Anchor (âncora espacial)

**O que é:** Referência digital associada a local físico rastreado.

**Por que importa:** Mantém objetos alinhados ao ambiente.

**Como praticar:** Posicione um objeto em superfície detectada.

**Onde aprender:** https://modelviewer.dev/docs/

### 17. SLAM — Simultaneous Localization and Mapping (localização e mapeamento simultâneos)

**O que é:** Método de mapear espaço enquanto estima movimento.

**Por que importa:** Ajuda tracking espacial em AR.

**Como praticar:** Observe perda de tracking em paredes lisas.

**Onde aprender:** https://modelviewer.dev/docs/

### 18. FPS — Frames Per Second (quadros por segundo)

**O que é:** Quantidade de quadros renderizados a cada segundo.

**Por que importa:** Indica fluidez, mas não cobre sozinho estabilidade.

**Como praticar:** Meça distribuição de frame times.

**Onde aprender:** https://modelviewer.dev/docs/

### 19. Frame Time (tempo de quadro)

**O que é:** Tempo necessário para renderizar um frame.

**Por que importa:** Picos causam travamentos mesmo com FPS médio alto.

**Como praticar:** Compare percentis em dispositivo real.

**Onde aprender:** https://modelviewer.dev/docs/

### 20. LCP — Largest Contentful Paint (maior elemento de conteúdo carregado)

**O que é:** Métrica de carregamento da página.

**Por que importa:** 3D não deve atrasar o conteúdo principal.

**Como praticar:** Carregue GLB depois do hero textual.

**Onde aprender:** https://modelviewer.dev/docs/

### 21. INP — Interaction to Next Paint (interação até próxima pintura)

**O que é:** Métrica de resposta a interações.

**Por que importa:** Canvas pesado pode deixar botões lentos.

**Como praticar:** Monitore clique e resposta.

**Onde aprender:** https://modelviewer.dev/docs/

### 22. CLS — Cumulative Layout Shift (mudança cumulativa de layout)

**O que é:** Métrica de instabilidade de layout.

**Por que importa:** Canvas que muda de tamanho incomoda usuário.

**Como praticar:** Reserve altura do visualizador.

**Onde aprender:** https://modelviewer.dev/docs/

### 23. Fallback (alternativa funcional)

**O que é:** Modo alternativo caso AR ou WebGL falhem.

**Por que importa:** Mantém acesso ao conteúdo e ação comercial.

**Como praticar:** Tenha imagem e descrição com CTA.

**Onde aprender:** https://modelviewer.dev/docs/

### 24. Reduced Motion (movimento reduzido)

**O que é:** Preferência do usuário de minimizar animações.

**Por que importa:** Reduz desconforto e melhora acessibilidade.

**Como praticar:** Desative autorotação quando solicitada.

**Onde aprender:** https://modelviewer.dev/docs/
