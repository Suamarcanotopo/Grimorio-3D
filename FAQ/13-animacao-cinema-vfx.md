# FAQ 13 — Animação, VFX e produção cinematográfica

**13 perguntas com resposta, justificativa e exercício.** [Voltar ao FAQ](README.md) · [Glossário](../GLOSSARIO/README.md).

## 1. Como faço um animatic rápido para cliente?

**Resposta:** Use poses e imagens simples com tempo aproximado e áudio temporário licenciado.

**Por que isso importa?** Alinhar narrativa antes do render evita retrabalho.

**Como fazer:**

1. Defina roteiro.
2. Faça 5 quadros.
3. Ajuste duração.
4. Valide entendimento.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 2. Como descobrir se uma animação está sem peso?

**Resposta:** Analise antecipação, aceleração, contato, trajetória e ação secundária.

**Por que isso importa?** Movimento sem peso parece artificial mesmo com modelo realista.

**Como fazer:**

1. Reveja poses.
2. Ajuste Graph Editor.
3. Compare com referência filmada autorizada.
4. Reteste.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 3. Posso transferir animação de um rig a outro sempre?

**Resposta:** Retargeting depende de poses, proporções, hierarquia e convenções do motor.

**Por que isso importa?** Transferência automática pode torcer membros ou deslizar pés.

**Como fazer:**

1. Confirme skeleton.
2. Ajuste pose de referência.
3. Retarget.
4. Teste articulações.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 4. O que faço se meu pé desliza no chão?

**Resposta:** Verifique contato, root motion, cinemática inversa e velocidade da animação.

**Por que isso importa?** Pé deslizando prejudica credibilidade de personagem.

**Como fazer:**

1. Marque contato.
2. Trave IK.
3. Revise curvas.
4. Teste no motor.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 5. Como criar expressão facial sem mocap?

**Resposta:** Shape Keys ou controles do rig podem animar boca e sobrancelhas manualmente.

**Por que isso importa?** Permite acting sem coletar rostos de terceiros.

**Como fazer:**

1. Crie duas expressões.
2. Configure controles.
3. Anime transição.
4. Avalie leitura.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 6. Como sincronizar áudio com personagem 3D?

**Resposta:** Use timecode/frame rate e marcadores consistentes entre animação e montagem.

**Por que isso importa?** Desalinhamento prejudica lip-sync e continuidade.

**Como fazer:**

1. Escolha FPS.
2. Importe áudio autorizado.
3. Marque fonemas.
4. Renderize e confira.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 7. Como fazer tracking de objeto em filmagem agitada?

**Resposta:** É preciso referências visuais estáveis, suficiente parallax e limpeza de track.

**Por que isso importa?** Câmera com blur pode dificultar solve.

**Como fazer:**

1. Escolha pontos bons.
2. Track forward/backward.
3. Remova outliers.
4. Resolva câmera.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 8. Por que a sombra CG não combina com o vídeo?

**Resposta:** Direção de luz, HDRI, distância ao chão, material e color science podem divergir.

**Por que isso importa?** Mesmo modelo bom parece artificial sem contato coerente.

**Como fazer:**

1. Estime luz do take.
2. Posicione sombra.
3. Ajuste roughness.
4. Compare frames.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 9. Qual a diferença de composição 2D e deep?

**Resposta:** Composição tradicional mistura camadas 2D; deep preserva múltiplas amostras de profundidade.

**Por que isso importa?** Volumes e sobreposições complexas podem exigir deep.

**Como fazer:**

1. Monte cena de fumaça.
2. Estude EXR deep.
3. Compare oclusão.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 10. O que devo registrar numa filmagem para VFX?

**Resposta:** Lente, câmera, escala, iluminação, HDRI, cor, timecode e referências de set.

**Por que isso importa?** Esses dados reduzem tentativa e erro na pós.

**Como fazer:**

1. Crie ficha do take.
2. Fotografe referências autorizadas.
3. Salve medidas.
4. Vincule ao projeto.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 11. Quando usar OpenEXR em vez de PNG?

**Resposta:** EXR ajuda com alta faixa dinâmica, passes e ajustes de composição.

**Por que isso importa?** PNG pronto pode perder informação de iluminação necessária.

**Como fazer:**

1. Renderize 1 frame EXR.
2. Extraia passes.
3. Compare pós-produção.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 12. Unreal funciona para render de cinema final?

**Resposta:** Sim para workflows adequados, mas é necessário configurar Movie Render Pipeline e testar fidelidade.

**Por que isso importa?** Preview em tempo real não é automaticamente qualidade de entrega cinematográfica.

**Como fazer:**

1. Crie Sequence.
2. Configure export.
3. Renderize frames.
4. Faça controle de qualidade.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 13. Como impedir que o render final mude de cor?

**Resposta:** Fixe transformações, espaço de trabalho, monitor de referência e exportações compatíveis.

**Por que isso importa?** Color management inconsistente gera reprovação.

**Como fazer:**

1. Documente OCIO.
2. Renderize cor-teste.
3. Confira compositor.
4. Registre versões.

**Onde aprender / boas práticas:** https://www.aswf.io/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
