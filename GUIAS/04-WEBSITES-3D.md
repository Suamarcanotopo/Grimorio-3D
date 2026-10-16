# Websites 3D — produtos interativos, cenários, parallax e XR

## Como escolher a ferramenta certa

| Cenário | Solução inicial | Justificativa |
|---|---|---|
| Produto 3D rotacionável sem experiência de shader | [model-viewer](https://modelviewer.dev/) | Componente web para GLB/glTF e AR em ambientes compatíveis |
| Landing page 3D com React | [React Three Fiber](https://r3f.docs.pmnd.rs/) + [Drei](https://drei.docs.pmnd.rs/) | Composição de cenas reutilizáveis |
| Website com JavaScript sem React | [Three.js](https://threejs.org/) | Controle completo de câmera, cena, luz e material |
| Game e visualização avançada no browser | [Babylon.js](https://www.babylonjs.com/) ou [PlayCanvas](https://playcanvas.com/) | Engines 3D completas |
| Experiência guiada no editor visual | [Spline](https://spline.design/) ou [Vectary](https://www.vectary.com/) | Menos código, limitações do plano |
| WebXR/imersão | [A-Frame](https://aframe.io/) + [WebXR](https://www.w3.org/TR/webxr/) | Dispositivos e sessões XR |

## Arquitetura recomendada

**Página HTML/React → contêiner de tamanho estável → renderizador 3D isolado → assets GLB comprimidos → controles progressivos → fallback 2D acessível.**

1. Avalie se o objeto 3D realmente eleva compreensão ou conversão: hero animado sem objetivo aumenta custo.
2. Crie modelo nativo com escala real, pivô coerente e material padronizado.
3. Exporte um GLB mínimo e valide em [PlayCanvas Model Viewer](https://playcanvas.com/model-viewer) ou ferramenta equivalente.
4. Comprima malhas com meshoptimizer e texturas com KTX2 quando o cliente suportar.
5. Carregue sob demanda abaixo da dobra; priorize texto e conversão.
6. Limite pixel ratio, pós-processamento, shaders e transparências; observe memória GPU.
7. Respeite **prefers-reduced-motion**, acesso por teclado, textos alternativos e ação equivalente sem canvas.
8. Teste desktop básico, Android intermediário, iPhone e redes lentas; registre métricas.

## O que medir

- **LCP (Largest Contentful Paint; maior elemento de conteúdo carregado):** indicador da percepção de carregamento.
- **INP (Interaction to Next Paint; interação até a próxima pintura):** responsividade a ações.
- **CLS (Cumulative Layout Shift; mudança cumulativa de layout):** estabilidade visual.
- FPS, tempo de inicialização, número de draw calls, triângulos visíveis, memória e download total do pacote.

**Nenhum orçamento de MB/triângulos é universal:** defina requisitos por dispositivo e aceite somente após teste real.

## Acessibilidade e segurança

Canvas precisa alternativa textual e funcional. Botões controlam rotação/zoom sem exigir gesto; modelos não devem capturar teclado quando usuário navega no conteúdo. Não renderize conteúdo de origem desconhecida como HTML ou scripts. Higienize URLs e isole arquivos enviados por usuários. Imagens, ícones, texturas e modelos preservam suas licenças próprias.

## Exemplo reutilizável

[EXEMPLOS/web-model-viewer.html](../EXEMPLOS/web-model-viewer.html) é um ponto de partida com fallback, controle semântico e tratamento de motion reduzido. **O exemplo não inclui modelos de terceiros**: substitua o endereço do GLB por arquivo autorizado.

## Fontes oficiais

[Khronos glTF](https://www.khronos.org/gltf/) · [Babylon Viewer v2](https://doc.babylonjs.com/features/featuresDeepDive/babylonViewer) · [PlayCanvas Model Viewer](https://playcanvas.com/model-viewer) · [W3C WAI](https://www.w3.org/WAI/).

[Índice geral](../INDEX.md)
