# Pipelines de dependências — contratos de handoff

**Nada neste documento executa SDK ou baixa modelos.** Use projetos de teste, leia licenças e verifique versão antes de levar à produção.

## D01

### Blender → produto 3D no website

**De:** Blender (arquivo BLEND)

**Passa por:** UV + PBR → GLB/glTF → model-viewer

**Entregue em:** Site HTML, WordPress ou CMS

**Dependências obrigatórias:**
- [ ] Modelo com licença válida e dimensões corretas
- [ ] GLB exportado e aberto no viewer
- [ ] Página HTTPS, texto alternativo, poster e fallback
- [ ] Teste celular de entrada e carregamento real

**Opcionais:** KTX2 quando compatível; Compressão de malha em fluxo validado

**Onde aprender e verificar:**
- https://docs.blender.org/manual/pt/4.5/index.html
- https://www.khronos.org/gltf/
- https://modelviewer.dev/docs/index.html

**Status:** documentado / integração não executada.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D02

### Blender → WebAR Android/iOS

**De:** Blender (BLEND)

**Passa por:** GLB com escala física → Android Scene Viewer (ARCore) → iOS Quick Look (USDZ ou conversão suportada)

**Entregue em:** AR aberta a partir de website

**Dependências obrigatórias:**
- [ ] Aparelho ARCore compatível ou Apple com Quick Look
- [ ] HTTPS e permissões quando exigidas
- [ ] Modelo correto em metros e ancoragem testada
- [ ] Fallback 3D ou imagem

**Opcionais:** Arquivo USDZ verificado no iOS; Lançamento por model-viewer

**Onde aprender e verificar:**
- https://developers.google.com/ar/develop/scene-viewer?hl=pt-BR
- https://developer.apple.com/documentation/quicklook
- https://modelviewer.dev/docs/index.html

**Status:** documentado / testes de dispositivos pendentes.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D03

### Blender → Lens Studio → Snapchat

**De:** BLEND / asset licenciado

**Passa por:** Exportação 3D compatível → Snap Lens Studio → Preview, perfis e otimização

**Entregue em:** Snapchat Lens

**Dependências obrigatórias:**
- [ ] Conta Snap com acesso à ferramenta
- [ ] Asset com licença, formato e UV suportados
- [ ] Teste câmera/track e performance
- [ ] Submissão e aprovação conforme regras

**Opcionais:** Templates para interação; Tracking corporal/facial se autorizado

**Onde aprender e verificar:**
- https://developers.snap.com/lens-studio/home
- https://developers.snap.com/lens-studio/assets-pipeline/3d/exporting-content/overview
- https://developers.snap.com/lens-studio/publishing/optimization/overview

**Status:** documentado / publicação não realizada.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D04

### Lens Studio → Snap Camera Kit → website

**De:** Lens autorizada no Lens Studio

**Passa por:** Camera Kit Web SDK → Token e conta de desenvolvedor → Sessão com MediaStream e canvas → Lens ID e Lens Group ID

**Entregue em:** Filtro AR com câmera dentro de site

**Dependências obrigatórias:**
- [ ] Acesso/autorização de Camera Kit e Lens
- [ ] Ambiente Web com HTTPS e permissão de câmera
- [ ] Política de Segurança de Conteúdo configurada sem abrir excessos desnecessários
- [ ] Gestão segura de tokens e encerramento da câmera
- [ ] Compatibilidade e licenciamento do SDK validados

**Opcionais:** Preview em React/TypeScript; Tratamento de erro de Lens

**Onde aprender e verificar:**
- https://developers.snap.com/camera-kit/home
- https://developers.snap.com/camera-kit/integrate-sdk/web/web-configuration
- https://developers.snap.com/camera-kit/integrate-sdk/web/tutorials/camera-kit-web-react-typescript

**Status:** documentado / credenciais e termos precisam homologação.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D05

### Blender → TikTok Effect House

**De:** BLEND e assets próprios

**Passa por:** Exportação FBX/glTF/OBJ conforme especificação → Importação e componentes Effect House → Teste de performance e política de conteúdo

**Entregue em:** Efeito AR publicado no TikTok

**Dependências obrigatórias:**
- [ ] Conferir limites vigentes no editor atual
- [ ] UV/texturas/rig compatíveis
- [ ] Conta e direitos sobre imagens/sons/modelos
- [ ] Teste real no TikTok e aprovação

**Opcionais:** Visual Scripting; Templates faciais/mundiais

**Onde aprender e verificar:**
- https://effecthouse.tiktok.com/learn/guides/workspace/assets/asset-preparation/3d
- https://effecthouse.tiktok.com/learn/guides/getting-started/technical-guidelines/technical-optimization
- https://effecthouse.us.tiktok.com/learn/guides/publishing/submit-your-effect

**Status:** documentado / publicação não realizada.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D06

### Blender → Unreal → Meta Quest XR/MR

**De:** Asset BLEND

**Passa por:** FBX/glTF com escala e UV → Unreal Engine compatível → Meta XR Plugin e configurações Android → VR Template / Mixed Reality features

**Entregue em:** Aplicativo XR/MR para Meta Quest

**Dependências obrigatórias:**
- [ ] Dispositivo e conta Meta Developer adequados
- [ ] Matriz Unreal/Meta XR verificada
- [ ] Teste de rastreamento, conforto, FPS e privacidade
- [ ] Build real em Quest

**Opcionais:** Passthrough e âncoras conforme dispositivo; Control Rig e interações

**Onde aprender e verificar:**
- https://developers.meta.com/vr/documentation/unreal/unreal-engine/
- https://developers.meta.com/vr/documentation/unreal/unreal-quick-start-install-unreal-engine/
- https://developers.meta.com/vr/documentation/native/mr-experience-and-use-cases/

**Status:** documentado / hardware e plugin não validados em execução.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D07

### Unreal → AR nativa Android/iOS

**De:** Projeto Unreal e assets

**Passa por:** Handheld AR Template → Android/iOS device setup → Plano/âncora e interação

**Entregue em:** Aplicativo mobile AR

**Dependências obrigatórias:**
- [ ] Build de app separado de website
- [ ] Câmera e permissões mínimas
- [ ] Dispositivo suportado e testes
- [ ] Modelo em escala física

**Opcionais:** Visualização conjunta com backend web

**Onde aprender e verificar:**
- https://dev.epicgames.com/documentation/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine?lang=en-US
- https://developers.google.com/ar
- https://developer.apple.com/augmented-reality/

**Status:** documentado / build não realizado.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D08

### Blender / criação de mundos → Meta Horizon

**De:** Assets originais e projeto de mundo

**Passa por:** Ferramentas Horizon Create/Studio ou Desktop Editor conforme acesso → Regras de importação do editor efetivamente disponível → Teste social/multiplayer e políticas

**Entregue em:** Experiência no ecossistema Horizon

**Dependências obrigatórias:**
- [ ] Confirmar elegibilidade e disponibilidade por conta
- [ ] Revisar suporte real de importação em sua versão
- [ ] Cumprir padrões e regras de publicação
- [ ] Testar plataforma-alvo

**Opcionais:** Automação de criação assistida por IA nas ferramentas disponíveis

**Onde aprender e verificar:**
- https://developers.meta.com/horizon-worlds/
- https://developers.meta.com/horizon-worlds/documentation/desktop-editor/get-started/install-desktop-editor/
- https://developers.meta.com/blog/meta-connect-recap/

**Status:** em evolução / não confundir com Meta Spark encerrado.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D09

### Web3D imersivo → Meta Quest browser

**De:** Modelo GLB + aplicação web

**Passa por:** Three.js / WebXR → Browser compatível com sessão imersiva → Opcional Meta Immersive Web SDK

**Entregue em:** Experiência XR pelo navegador Quest

**Dependências obrigatórias:**
- [ ] Secure context HTTPS
- [ ] Sessão WebXR com detecção de suporte
- [ ] Controles acessíveis e fallback não imersivo
- [ ] Teste Quest real

**Opcionais:** SDK específico Meta conforme objetivo

**Onde aprender e verificar:**
- https://www.w3.org/TR/webxr/
- https://threejs.org/
- https://developers.meta.com/vr/

**Status:** documentado / testes reais pendentes.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.


## D10

### Blender → Unity / Unreal games

**De:** Arquivo BLEND

**Passa por:** Mesh + UV + textura PBR → FBX/glTF conforme target → Importação e rig retargeting → Colisão + LOD + profiler

**Entregue em:** Game executável

**Dependências obrigatórias:**
- [ ] Licenças dos assets
- [ ] Escala, orientação e material conferidos
- [ ] FPS/frame time testado no hardware alvo
- [ ] Projeto nativo preservado

**Opcionais:** Animações Mixamo autorizadas; Instâncias e otimização

**Onde aprender e verificar:**
- https://docs.unity3d.com/
- https://dev.epicgames.com/documentation/en-us/unreal-engine
- https://docs.blender.org/manual/en/latest/

**Status:** documentado / dependências dependem de versão.

**Proteção de downside:** retenha arquivos nativos, documente os termos de cada SDK e crie um protótipo mínimo antes de investir em integração profunda.

