# Animação, rigging, mocap, tracking e composição

## Três caminhos diferentes

| Necessidade | Técnica | Entrada | Saída |
|---|---|---|---|
| Animar personagem sintético | Rigging + keyframes | Modelo e esqueleto | Sequência de poses/animação |
| Transformar atuação real em movimento digital | Motion capture (captura de movimento) | Vídeo, sensores ou marcadores | Movimento editável e retargeting |
| Colocar objeto 3D em filmagem | Matchmoving / camera tracking | Vídeo e dados da lente | Câmera 3D reconstruída e composição |

**Rigging:** criar controles e hierarquias; **skinning:** vincular pele/vertices aos ossos e pesos; **IK (Inverse Kinematics; cinemática inversa):** resolver posição de articulações a partir de alvo; **FK (Forward Kinematics; cinemática direta):** animar por rotações dos ossos; **retargeting:** transferir animação entre esqueletos compatíveis.

## Fluxo de personagem

1. Revisar malha e loops nas articulações.
2. Criar ou importar skeleton; padronizar nomenclatura e orientação.
3. Pintar pesos; testar ombros, cotovelos, joelhos e dedos em poses extremas.
4. Planejar controlador IK/FK e testar transições.
5. Animar poses principais, breakdowns, in-betweens, curvas de tempo e root motion.
6. Exportar animação; testar no software de destino e revisar contato dos pés.

## Fluxo de camera tracking

1. Importar vídeo autorizado; registrar frame rate, resolução, lente e método de captura.
2. Identificar pontos estáveis e com parallax.
3. Fazer solve da câmera; observar erro residual e geometria de referência.
4. Definir escala, plano do chão e orientação; integrar objeto de prova.
5. Igualar iluminação, lente, sombras e oclusão; compor passes.
6. Validar com movimento ao longo de toda sequência, não só em um frame.

## Armadilhas

- 2D planar tracking **não** é, por si só, reconstrução completa de câmera 3D.
- Captura de rostos/pessoas depende de autorização, privacidade e finalidade legítima.
- Retargeting entre rigs não equivalentes pode mudar direção, escala, base pose e contatos.
- Arquivos mocap e plugins podem incorporar direitos diferentes do modelo base.

## Referências

[Blender Movie Tracking](https://docs.blender.org/manual/en/latest/movie_clip/tracking/) · [Nuke CameraTracker](https://learn.foundry.com/nuke/16.0/content/reference_guide/3d_nodes/cameratracker.html) · [SideFX KineFX](https://www.sidefx.com/docs/houdini/character/kinefx/index.html) · [Unreal Control Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine) · [Adobe Mixamo](https://www.mixamo.com/).

[Índice geral](../INDEX.md)
