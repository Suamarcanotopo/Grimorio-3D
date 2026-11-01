# Dependências 3D explicadas — 10 caminhos sem jargão

**Objetivo:** entender a sequência para chegar a um resultado 3D utilizável, mesmo sem programar. Este guia transforma os [10 pipelines originais](matriz.json) em passos simples sem alterar seus contratos ou marcar testes não feitos.

## Mini-glossário na primeira leitura
- **3D — três dimensões:** objeto com profundidade; imagem *que parece 3D* não comprova um arquivo 3D funcional.
- **UV — coordenadas de textura:** explicam onde uma imagem será aplicada à superfície do objeto; como o molde que determina o tecido.
- **PBR — Physically Based Rendering, renderização baseada em propriedades físicas:** método para simular como materiais reagem à luz; não garante perfeição visual.
- **GLB — forma binária do glTF (GL Transmission Format, formato de transmissão de cenas 3D):** arquivo para entregar geometrias, materiais e cenas, sujeito à compatibilidade de uso.
- **AR — Augmented Reality, realidade aumentada:** mistura representação digital e câmera/ambiente físico.
- **XR — Extended Reality, realidade estendida:** conjunto de experiências imersivas, incluindo AR e realidade virtual.
- **MR — Mixed Reality, realidade mista:** integração de objetos digitais ao ambiente com diferentes graus de interação.
- **SDK — Software Development Kit, kit de desenvolvimento de software:** ferramentas e instruções de um fornecedor; depende da versão e dos termos.
- **API — Application Programming Interface, interface de programação de aplicações:** meio pelo qual sistemas trocam pedidos e resultados.
- **VFX — Visual Effects, efeitos visuais:** elementos visuais compostos ou modificados durante a produção.
- **CMS — Content Management System, sistema de gestão de conteúdo:** aplicativo que organiza conteúdo de sites.
- **HTTPS — Hypertext Transfer Protocol Secure, protocolo seguro de comunicação web:** conexão criptografada para acesso ao site.
- **Gate:** condição de verificação antes de considerar a etapa pronta.
- **ECP — Engineering Control Plane, plano de controle de engenharia:** orquestra responsabilidades conforme a missão.
- **Coliseum:** revisão adversarial de riscos, provas e regressões.
- **Skill:** competência documentada do ecossistema, não programa instalado por este guia.

**Fórmula geral:** escolha seu resultado → confira o pré-requisito → produza um arquivo → teste no destino → registre defeitos → corrija → só então considere usar em público. Não confunda representação, integração escrita e execução real.

## D01 — Blender → produto 3D no website

**Analogia:** Produto em uma vitrine online: primeiro criar o objeto, depois uma embalagem compatível com o navegador, por fim testar a entrega.

**Para que serve:** entregar um resultado em **Site HTML, WordPress ou CMS**, partindo de **Blender (arquivo BLEND)**.

**O que preciso entender antes:** 1) UV + PBR → 2) GLB/glTF → 3) model-viewer. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Modelo com licença válida e dimensões corretas. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. GLB exportado e aberto no viewer. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Página HTTPS, texto alternativo, poster e fallback. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Teste celular de entrada e carregamento real. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** KTX2 quando compatível; Compressão de malha em fluxo validado.

**Skills que podem ajudar, se a missão exigir:** [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [ux-guider](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/ux-guider). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / integração não executada. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://docs.blender.org/manual/pt/4.5/index.html> · <https://www.khronos.org/gltf/> · <https://modelviewer.dev/docs/index.html>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D02 — Blender → WebAR Android/iOS

**Analogia:** Experimentar um sofá virtual na sala: o modelo precisa ter tamanho certo e o celular precisa suportar a tecnologia.

**Para que serve:** entregar um resultado em **AR aberta a partir de website**, partindo de **Blender (BLEND)**.

**O que preciso entender antes:** 1) GLB com escala física → 2) Android Scene Viewer (ARCore) → 3) iOS Quick Look (USDZ ou conversão suportada). Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Aparelho ARCore compatível ou Apple com Quick Look. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. HTTPS e permissões quando exigidas. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Modelo correto em metros e ancoragem testada. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Fallback 3D ou imagem. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Arquivo USDZ verificado no iOS; Lançamento por model-viewer.

**Skills que podem ajudar, se a missão exigir:** [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec), [ux-guider](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/ux-guider). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / testes de dispositivos pendentes. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://developers.google.com/ar/develop/scene-viewer?hl=pt-BR> · <https://developer.apple.com/documentation/quicklook> · <https://modelviewer.dev/docs/index.html>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D03 — Blender → Lens Studio → Snapchat

**Analogia:** Filtro do aplicativo: desenhar o objeto não significa que a câmera conseguirá segui-lo.

**Para que serve:** entregar um resultado em **Snapchat Lens**, partindo de **BLEND / asset licenciado**.

**O que preciso entender antes:** 1) Exportação 3D compatível → 2) Snap Lens Studio → 3) Preview, perfis e otimização. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Conta Snap com acesso à ferramenta. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Asset com licença, formato e UV suportados. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Teste câmera/track e performance. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Submissão e aprovação conforme regras. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Templates para interação; Tracking corporal/facial se autorizado.

**Skills que podem ajudar, se a missão exigir:** [sin-motion-expertise-council](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-motion-expertise-council), [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / publicação não realizada. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://developers.snap.com/lens-studio/home> · <https://developers.snap.com/lens-studio/assets-pipeline/3d/exporting-content/overview> · <https://developers.snap.com/lens-studio/publishing/optimization/overview>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D04 — Lens Studio → Snap Camera Kit → website

**Analogia:** Levar uma função de câmera para um site: conectar serviços exige direitos, contas e segurança.

**Para que serve:** entregar um resultado em **Filtro AR com câmera dentro de site**, partindo de **Lens autorizada no Lens Studio**.

**O que preciso entender antes:** 1) Camera Kit Web SDK → 2) Token e conta de desenvolvedor → 3) Sessão com MediaStream e canvas → 4) Lens ID e Lens Group ID. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Acesso/autorização de Camera Kit e Lens. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Ambiente Web com HTTPS e permissão de câmera. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Política de Segurança de Conteúdo configurada sem abrir excessos desnecessários. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Gestão segura de tokens e encerramento da câmera. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
5. Compatibilidade e licenciamento do SDK validados. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Preview em React/TypeScript; Tratamento de erro de Lens.

**Skills que podem ajudar, se a missão exigir:** [ai-wiring](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/ai-wiring), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec), [wiring-specialist](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/wiring-specialist). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / credenciais e termos precisam homologação. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://developers.snap.com/camera-kit/home> · <https://developers.snap.com/camera-kit/integrate-sdk/web/web-configuration> · <https://developers.snap.com/camera-kit/integrate-sdk/web/tutorials/camera-kit-web-react-typescript>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D05 — Blender → TikTok Effect House

**Analogia:** Efeito social: um vídeo bonito não comprova que o filtro funcionará no aplicativo.

**Para que serve:** entregar um resultado em **Efeito AR publicado no TikTok**, partindo de **BLEND e assets próprios**.

**O que preciso entender antes:** 1) Exportação FBX/glTF/OBJ conforme especificação → 2) Importação e componentes Effect House → 3) Teste de performance e política de conteúdo. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Conferir limites vigentes no editor atual. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. UV/texturas/rig compatíveis. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Conta e direitos sobre imagens/sons/modelos. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Teste real no TikTok e aprovação. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Visual Scripting; Templates faciais/mundiais.

**Skills que podem ajudar, se a missão exigir:** [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [sin-motion-expertise-council](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-motion-expertise-council), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / publicação não realizada. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://effecthouse.tiktok.com/learn/guides/workspace/assets/asset-preparation/3d> · <https://effecthouse.tiktok.com/learn/guides/getting-started/technical-guidelines/technical-optimization> · <https://effecthouse.us.tiktok.com/learn/guides/publishing/submit-your-effect>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D06 — Blender → Unreal → Meta Quest XR/MR

**Analogia:** Mundo virtual em óculos: a cena deve ser construída e medida no dispositivo real.

**Para que serve:** entregar um resultado em **Aplicativo XR/MR para Meta Quest**, partindo de **Asset BLEND**.

**O que preciso entender antes:** 1) FBX/glTF com escala e UV → 2) Unreal Engine compatível → 3) Meta XR Plugin e configurações Android → 4) VR Template / Mixed Reality features. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Dispositivo e conta Meta Developer adequados. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Matriz Unreal/Meta XR verificada. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Teste de rastreamento, conforto, FPS e privacidade. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Build real em Quest. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Passthrough e âncoras conforme dispositivo; Control Rig e interações.

**Skills que podem ajudar, se a missão exigir:** [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / hardware e plugin não validados em execução. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://developers.meta.com/vr/documentation/unreal/unreal-engine/> · <https://developers.meta.com/vr/documentation/unreal/unreal-quick-start-install-unreal-engine/> · <https://developers.meta.com/vr/documentation/native/mr-experience-and-use-cases/>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D07 — Unreal → AR nativa Android/iOS

**Analogia:** Um aplicativo precisa ser gerado e instalado; apenas o editor aberto não prova funcionamento.

**Para que serve:** entregar um resultado em **Aplicativo mobile AR**, partindo de **Projeto Unreal e assets**.

**O que preciso entender antes:** 1) Handheld AR Template → 2) Android/iOS device setup → 3) Plano/âncora e interação. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Build de app separado de website. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Câmera e permissões mínimas. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Dispositivo suportado e testes. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Modelo em escala física. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Visualização conjunta com backend web.

**Skills que podem ajudar, se a missão exigir:** [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [wiring-specialist](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/wiring-specialist), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / build não realizado. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://dev.epicgames.com/documentation/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine?lang=en-US> · <https://developers.google.com/ar> · <https://developer.apple.com/augmented-reality/>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D08 — Blender / criação de mundos → Meta Horizon

**Analogia:** Criar um espaço compartilhado depende de regras da plataforma e permissão da conta.

**Para que serve:** entregar um resultado em **Experiência no ecossistema Horizon**, partindo de **Assets originais e projeto de mundo**.

**O que preciso entender antes:** 1) Ferramentas Horizon Create/Studio ou Desktop Editor conforme acesso → 2) Regras de importação do editor efetivamente disponível → 3) Teste social/multiplayer e políticas. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Confirmar elegibilidade e disponibilidade por conta. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Revisar suporte real de importação em sua versão. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Cumprir padrões e regras de publicação. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Testar plataforma-alvo. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Automação de criação assistida por IA nas ferramentas disponíveis.

**Skills que podem ajudar, se a missão exigir:** [sin-motion-expertise-council](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-motion-expertise-council), [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [researcher-of-truth](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/researcher-of-truth). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** em evolução / não confundir com Meta Spark encerrado. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://developers.meta.com/horizon-worlds/> · <https://developers.meta.com/horizon-worlds/documentation/desktop-editor/get-started/install-desktop-editor/> · <https://developers.meta.com/blog/meta-connect-recap/>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D09 — Web3D imersivo → Meta Quest browser

**Analogia:** Um site imersivo no visor exige controle, desempenho e acessibilidade reais.

**Para que serve:** entregar um resultado em **Experiência XR pelo navegador Quest**, partindo de **Modelo GLB + aplicação web**.

**O que preciso entender antes:** 1) Three.js / WebXR → 2) Browser compatível com sessão imersiva → 3) Opcional Meta Immersive Web SDK. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Secure context HTTPS. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Sessão WebXR com detecção de suporte. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. Controles acessíveis e fallback não imersivo. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Teste Quest real. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** SDK específico Meta conforme objetivo.

**Skills que podem ajudar, se a missão exigir:** [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [ux-guider](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/ux-guider), [cybersec](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/cybersec). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / testes reais pendentes. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://www.w3.org/TR/webxr/> · <https://threejs.org/> · <https://developers.meta.com/vr/>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## D10 — Blender → Unity / Unreal games

**Analogia:** Um objeto usado em jogo precisa ser importado e testado pelo motor, não apenas desenhado.

**Para que serve:** entregar um resultado em **Game executável**, partindo de **Arquivo BLEND**.

**O que preciso entender antes:** 1) Mesh + UV + textura PBR → 2) FBX/glTF conforme target → 3) Importação e rig retargeting → 4) Colisão + LOD + profiler. Se algum termo não estiver claro, consulte o [glossário](../GLOSSARIO/README.md) e o [FAQ](../FAQ/README.md) antes de instalar ferramentas.

**Passos obrigatórios e como conferir:**
1. Licenças dos assets. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
2. Escala, orientação e material conferidos. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
3. FPS/frame time testado no hardware alvo. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.
4. Projeto nativo preservado. **Prova:** registre um teste ou documento específico de que cumpriu o requisito; sem prova, marque pendente.

**Opcionais, não exigências:** Animações Mixamo autorizadas; Instâncias e otimização.

**Skills que podem ajudar, se a missão exigir:** [sin-media-pipeline-architect](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-pipeline-architect), [sin-media-runtime-engineer](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/sin-media-runtime-engineer), [coliseum](https://github.com/Suamarcanotopo/grimorio-skills/tree/main/skills/coliseum). **Papel:** apoiar planejamento, produção, verificação técnica ou risco; nenhuma Skill é automaticamente ativada ou aprova o produto.

**Estado que a fonte registra:** documentado / dependências dependem de versão. Não chamar de funcional, publicado ou compatível em todos os dispositivos.

**Fontes de consulta registradas no pipeline:** <https://docs.unity3d.com/> · <https://dev.epicgames.com/documentation/en-us/unreal-engine> · <https://docs.blender.org/manual/en/latest/>.

**Exercício do aluno:** desenhe o fluxo em cinco caixas (“origem → transformação → arquivo → destino → teste”); marque uma etapa que depende de equipamento ou conta e outra que você pode aprender hoje sem instalar nada. Escreva a evidência que faltaria para afirmar que esse destino está funcional.

## Decisão Coliseum por tipo de dependência
- **ACCEPT:** estudo de pré-requisitos, fontes, glossário, tarefas e rastreabilidade no mesmo repositório.
- **RETEST:** integração com SDK, versão ou dispositivo sem evidência atual. Pesquisar documentação do fornecedor e testar em equipamento autorizado.
- **REJECT:** chamar `NOT_TESTED` de concluído ou tornar cada ferramenta dependência global do repositório.
- **ESCALATE:** direitos, identificação de pessoas, câmera, contas de publicação e operação comercial; exigem aprovação apropriada.

## Aprender sem dispersão
Escolha **um D por vez**. Comece pelo [D01: objeto 3D em site](#d01--blender--produto-3d-no-website) se quer um resultado simples e observável; não execute D01–D10 simultaneamente. Registre sempre software/versão, equipamento, arquivo, resultado e o que falhou.

[Voltar ao índice das dez rotas](README.md) · [Portal de aprendizagem 3D](../APRENDER/README.md) · [Mission Lock](../GOVERNANCA/MISSION-LOCK.md).
