# FAQ 12 — Materiais PBR, UV, baking e texturas

**13 perguntas com resposta, justificativa e exercício.** [Voltar ao FAQ](README.md) · [Glossário](../GLOSSARIO/README.md).

## 1. Como definir textura para produto visto muito de perto?

**Resposta:** Considere tamanho em pixels na tela, texel density e capacidade do dispositivo.

**Por que isso importa?** Textura 8K desnecessária penaliza carregamento.

**Como fazer:**

1. Meça visualização esperada.
2. Comece em 1K/2K.
3. Compare 4K.
4. Escolha menor aceitável.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 2. Por que o metal parece plástico no render?

**Resposta:** Metallic, roughness, reflexos e ambiente de luz podem estar incoerentes.

**Por que isso importa?** Material metálico depende de reflexão significativa.

**Como fazer:**

1. Metallic próximo do apropriado.
2. Configure HDRI.
3. Ajuste roughness.
4. Compare em duas luzes.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 3. Quais mapas PBR realmente preciso?

**Resposta:** Em muitos casos Base Color, Metallic/Roughness e Normal bastam; AO/Height variam por efeito.

**Por que isso importa?** Menos mapas pode significar menor custo sem perder qualidade.

**Como fazer:**

1. Defina aparência desejada.
2. Crie base e rugosidade.
3. Adicione normal só se útil.
4. Meça runtime.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 4. Como saber se normal map deve ser invertido?

**Resposta:** Convenções de espaço tangente podem diferir por software.

**Por que isso importa?** Canal verde invertido pode mostrar relevo ao contrário.

**Como fazer:**

1. Verifique documento do destino.
2. Compare direção de luz.
3. Teste canal verde.
4. Corrija origem.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 5. Por que meu bake tem manchas pretas?

**Resposta:** Normal invertida, cage incorreto, malhas sobrepostas ou UV problemáticas são causas comuns.

**Por que isso importa?** Bake defeituoso degrada ativo otimizado.

**Como fazer:**

1. Isole high/low.
2. Recalcule normais.
3. Inspecione UV.
4. Ajuste cage.
5. Refaça teste pequeno.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 6. Devo usar UDIM em um site comum?

**Resposta:** Só quando o renderer/exportador suportar; para web simples, GLB com texturas comuns costuma ser mais interoperável.

**Por que isso importa?** Evita pipeline de alta resolução incompatível com navegador.

**Como fazer:**

1. Determine destino.
2. Teste export de um tile.
3. Avalie atlas.
4. Escolha solução.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 7. Quando empacotar AO, Roughness e Metallic?

**Resposta:** Quando destino utiliza convenção de canais e sua otimização de textura compensa.

**Por que isso importa?** Empacotamento errado troca propriedades do material.

**Como fazer:**

1. Leia especificação.
2. Coloque canais correspondentes.
3. Faça export.
4. Valide no viewer.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 8. Minha textura muda de cor entre programas; por quê?

**Resposta:** Configuração de color management, gamma e tone mapping podem diferir.

**Por que isso importa?** Comparação visual sem pipeline consistente é enganosa.

**Como fazer:**

1. Identifique espaço de origem.
2. Confira sRGB/Non-Color.
3. Compare view transforms.
4. Faça teste de referência.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 9. É melhor material procedural ou textura pronta?

**Resposta:** Procedural facilita parametrização; mapas podem ser melhores para entrega em motores simples.

**Por que isso importa?** Decisão depende de compatibilidade e custo do runtime.

**Como fazer:**

1. Modele shader procedural.
2. Faça bake se preciso.
3. Teste destino.
4. Compare fidelidade.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 10. Como criar material de vidro sem travar o celular?

**Resposta:** Transmissão e transparência têm custo e compatibilidade diferentes entre renderizadores.

**Por que isso importa?** Vidro complexo pode ser inviável em mobile.

**Como fazer:**

1. Escolha shader compatível.
2. Simplifique camadas.
3. Meça GPU.
4. Forneça fallback visual.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 11. Como corrigir costura visível em UV?

**Resposta:** Ajuste continuidade da textura, margem de bake e posição das ilhas UV.

**Por que isso importa?** Costuras atrapalham realismo e close-up.

**Como fazer:**

1. Aplique textura checker.
2. Inspecione seams.
3. Aumente padding.
4. Compare render.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 12. Por que a textura perdeu detalhes depois de comprimir?

**Resposta:** Compressão com perdas e redução de resolução removem informação fina.

**Por que isso importa?** Tamanho menor não compensa artefatos comerciais graves.

**Como fazer:**

1. Capture comparação antes/depois.
2. Teste distância de tela.
3. Ajuste qualidade.
4. Preserve fonte.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 13. Onde encontro referência oficial para asset 3D de e-commerce?

**Resposta:** As diretrizes 3D Commerce da Khronos tratam formatos, geometria, materiais e entrega.

**Por que isso importa?** Padrão aberto ajuda interoperabilidade sem prender-se a um marketplace.

**Como fazer:**

1. Abra guia 2.0.
2. Selecione material.
3. Modele produto simples.
4. Valide glTF.

**Onde aprender / boas práticas:** https://github.com/KhronosGroup/3DC-Asset-Creation

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
