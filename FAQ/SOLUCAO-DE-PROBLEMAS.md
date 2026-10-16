# Diagnóstico rápido por sintoma

| Sintoma | Primeira hipótese | Teste de isolamento | Onde conferir |
|---|---|---|---|
| Modelo preto | Material, iluminação ou textura ausente | Use material cinza e luz básica | https://docs.blender.org/manual/en/latest/render/materials/ |
| Modelo rosa | Textura não encontrada | Refaça vínculos de arquivos | https://docs.blender.org/manual/en/latest/files/ |
| Modelo invertido | Eixos incompatíveis | Compare XYZ e origem em import/export | https://docs.blender.org/manual/en/latest/files/import_export/ |
| Textura esticada | UV deformada | Aplique checkerboard | https://docs.blender.org/manual/en/latest/modeling/meshes/uv/ |
| Relevo ao contrário | Normal map com convenção errada | Teste canal verde e modo de cor | https://www.khronos.org/gltf/ |
| Personagem deforma demais | Pesos/ossos incorretos | Pose extrema em cada junta | https://docs.blender.org/manual/en/latest/animation/armatures/ |
| Pés deslizam | Root motion e IK inconsistentes | Compare contato em cada quadro | https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-in-unreal-engine |
| Tracking perde pontos | Pouco parallax/contraste | Refilme com textura e luz homogênea | https://docs.blender.org/manual/en/latest/movie_clip/tracking/ |
| Web3D demora a carregar | GLB/texturas excessivos | Faça orçamento de bytes e lazy load | https://modelviewer.dev/docs/ |
| WebGL não inicia | GPU/navegador/contexto | Teste fallback e suporte no alvo | https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API |
| AR não aparece no Android | ARCore/Scene Viewer ou permissão ausente | Verifique aparelho compatível e HTTPS | https://developers.google.com/ar/develop/scene-viewer |
| AR não abre no iOS | USDZ/Quick Look, Safari ou arquivo inválido | Teste arquivo conhecido autorizado | https://developer.apple.com/documentation/quicklook |
| Lens social falha | Formato/limites/versionamento/conta | Abra profiler e documentação atual | https://developers.snap.com/ |
| Efeito TikTok é rejeitado | QA, conteúdo ou pacote | Consulte motivo de revisão e teste | https://effecthouse.tiktok.com/learn/guides/getting-started/technical-guidelines/technical-optimization |
| Quest apresenta travadas | Frame time acima do orçamento | Meça CPU/GPU em headset real | https://developers.meta.com/vr/documentation/unreal/unreal-advanced-rendering/ |
| Meta Spark não publica | Serviço de terceiros encerrado | Migre o conceito para destino ativo | https://developers.meta.com/vr/ |
| Site 3D quebra teclado | Canvas intercepta eventos | Navegue por Tab e Enter | https://www.w3.org/WAI/ |
| Asset suspeito traz scripts | Dependência não auditada | Não execute; isole e revise | https://spdx.org/licenses/ |

**Regra de diagnóstico:** reproduzir → isolar → formular hipótese → medir → corrigir → testar novamente → registrar antes/depois. Evite solucionar por tentativa sem registrar variáveis alteradas.
