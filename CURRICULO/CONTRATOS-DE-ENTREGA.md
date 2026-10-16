# Contratos de entrega por destino 3D

A pergunta não é "qual software é melhor?", mas **qual arquivo, licença e teste o destino exige**.

| Destino | Fonte editável | Exportação provável | Aceite específico |
|---|---|---|---|
| Filme/VFX em pós | BLEND/Maya/Houdini e cenas em camadas | EXR multicanal, USD, VDB, Alembic, OTIO | Revisão de cor, timecode, passes, lens e composição |
| Jogo Unity/Unreal | BLEND/Maya/3ds Max | FBX/glTF conforme rig/material/suporte | Retargeting, colisão, escala, LOD e build |
| Anúncio produto renderizado | BLEND/C4D | Sequência PNG/EXR e filme final | Marca, consistência de cor, legenda e direitos de música |
| Produto web | BLEND | GLB/glTF com materiais compatíveis | Carregamento, rotação, alt, CTA e fallback |
| WebAR Android | Projeto 3D | GLB e integração Scene Viewer | ARCore/Scene Viewer reais ou fallback |
| WebAR Apple | Projeto 3D | USDZ ou transformação suportada | Quick Look no iPhone/iPad real ou fallback |
| Snap Lens Studio | Origem 3D | Formato suportado no editor Snap | Teste móvel, Lens ID e política de publicação |
| Snap Camera Kit em site | Lens elegível, origem e runtime web | SDK Web + credenciais oficiais | Permissão de câmera, CSS, CSP, stop tracks, licenças |
| TikTok Effect House | Origem 3D | Asset segundo instrução oficial | Teste no editor, QA e publicação aprovada |
| Meta Quest | Origem 3D/Unreal | Build Android/Quest adequado | Frame time no headset real, acesso, privacidade |
| CAD/Arquitetura | STEP/IFC/Rhino/Revit e origem | STEP, IFC e malha derivada | Tolerâncias, escala, propriedades e autoria |
| Impressão 3D | CAD ou Blender original | STL/3MF conforme impressora | Malha fechada, tolerância e viabilidade de fabricação |

## Quando houver um plugin ou SDK

Não copie instruções de instalação genéricas como "use a última versão": estabeleça **(a)** dispositivo e software exatos, **(b)** matriz de compatibilidade oficial, **(c)** decisão de licença, **(d)** checksum/versão e **(e)** teste de regressão.

### Dependência do catálogo vs dependência de execução

- **Fonte de conhecimento:** hyperlink para manual ou livro, não requer instalação.
- **Ferramenta de autoria:** Blender/Unreal/Maya/etc., instalada localmente quando de fato usada.
- **SDK de execução:** package/plugin requerido por projeto específico, fixado em lockfile do projeto.
- **Serviço opcional:** plataforma com login, termos, cobrança e permissão.
- **Asset externo:** terceiro sob licença individual, nunca tratado como dependência do código MIT.

**Regra:** o Grimório não instala SDKs, não aciona serviços e não empacota assets pagos.
