# IA generativa 3D, fotogrametria, NeRF e Gaussian Splatting

## Técnicas que não devem ser confundidas

| Técnica | O que produz | Quando faz sentido |
|---|---|---|
| Texto/imagem para malha 3D | Geometria estimada a partir de prompt ou referência | Conceitos e protótipos que serão corrigidos |
| Fotogrametria (Structure from Motion + Multi-View Stereo) | Câmeras, nuvem de pontos e malha a partir de fotos | Digitalizar objetos e fachadas com referência real |
| LiDAR (Light Detection and Ranging; detecção de distância por luz) | Amostras de profundidade / pontos | Captura de espaços e escala |
| NeRF (Neural Radiance Fields; campos neurais de radiância) | Representação neural de vistas da cena | Explorar reconstrução de visualizações |
| 3D Gaussian Splatting | Representação por gaussianas renderizáveis | Navegação visual em cenários digitalizados |
| Mocap com vídeo | Estimativa de movimentos do corpo | Animar personagens a partir de atuação real |

## Experimento responsável

1. Use **objeto próprio** e fundo sem informações pessoais.
2. Documente câmera, fotos, resolução, iluminação e local de captura.
3. Compare resultado com referência de medida; uma cena bonita não é necessariamente dimensionalmente correta.
4. Gere malha editável e avalie limpeza/retopologia, se for para games.
5. Verifique se plano gratuito permite **uso comercial**, divulgação pública e dados de treinamento.
6. Registre versão do modelo de IA, parâmetros, licença, autor e evidências.
7. Para pessoas e propriedades privadas, obtenha autorização e delimite tratamento de dados.

**Alerta específico:** plano gratuito do Tripo3D pode restringir uso comercial; não generalize permissão entre planos e datas.

**Fontes:** [COLMAP](https://colmap.github.io/) · [AliceVision](https://alicevision.org/) · [Nerfstudio](https://docs.nerf.studio/) · [Gaussian Splatting (pesquisa)](https://github.com/graphdeco-inria/gaussian-splatting) · [Tripo3D](https://www.tripo3d.ai/pt).

[Índice geral](../INDEX.md)
