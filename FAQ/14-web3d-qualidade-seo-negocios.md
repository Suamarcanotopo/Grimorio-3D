# FAQ 14 — Web3D e negócios — qualidade, SEO e interação

**13 perguntas com resposta, justificativa e exercício.** [Voltar ao FAQ](README.md) · [Glossário](../GLOSSARIO/README.md).

## 1. Por que meu GLB demora tanto para carregar?

**Resposta:** Pode haver malha densa, texturas grandes, rede lenta e falta de compactação.

**Por que isso importa?** Página lenta perde interação e pode prejudicar experiência comercial.

**Como fazer:**

1. Meça bytes por recurso.
2. Faça versão 2K.
3. Teste compressão.
4. Compare celular.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 2. Como montar comparação de versões com 3D?

**Resposta:** Tenha baseline estático e variante interativa com mesma mensagem e preço.

**Por que isso importa?** Atribuir ganho comercial ao 3D exige comparação justa.

**Como fazer:**

1. Defina métricas.
2. Prepare A/B controlado.
3. Colete dados suficientes.
4. Analise.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 3. Meu configurador de cores muda apenas a imagem?

**Resposta:** Pode trocar materiais ou texturas; é preciso validar todas as variantes no destino.

**Por que isso importa?** Prometer variação inexistente gera frustração na compra.

**Como fazer:**

1. Crie variantes em GLB.
2. Conecte seletor.
3. Revise labels.
4. Teste mobile.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 4. Como iniciar 3D apenas quando usuário quiser?

**Resposta:** Lazy loading e interação explícita evitam custo inicial alto.

**Por que isso importa?** Reduz carga sem prejudicar usuário que só quer ler.

**Como fazer:**

1. Mostre poster.
2. Adicione botão Ver em 3D.
3. Carregue GLB sob clique.
4. Meça.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 5. Preciso de Three.js em todo site 3D?

**Resposta:** Não; um componente como model-viewer atende muitos casos de produto simples.

**Por que isso importa?** Escolha ferramenta mais leve com requisitos reais.

**Como fazer:**

1. Prototipe HTML.
2. Meça necessidade de interação.
3. Escolha model-viewer ou Three.js.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 6. Como fazer site 3D acessível por teclado?

**Resposta:** Mantenha botões HTML, foco visível, descrição do objeto e modo não-3D.

**Por que isso importa?** Canvas sem alternativa pode excluir usuários.

**Como fazer:**

1. Navegue usando Tab.
2. Inspecione foco.
3. Teste CTA sem WebGL.
4. Corrija.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 7. Qual melhor fallback para falta de WebGL?

**Resposta:** Imagem autorizada, descrição, preço, instruções e CTA funcionais.

**Por que isso importa?** O cliente não deve perder o conteúdo central.

**Como fazer:**

1. Simule desativar WebGL.
2. Exiba poster.
3. Tente comprar.
4. Verifique sucesso.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 8. Como detectar perda de contexto gráfico?

**Resposta:** Escute eventos específicos de context lost/restored e reconstrua recursos.

**Por que isso importa?** Pode haver travamento em dispositivos móveis.

**Como fazer:**

1. Simule evento.
2. Mostre feedback.
3. Libere/recrie recursos.
4. Reavalie.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 9. Como otimizar Three.js em smartphone básico?

**Resposta:** Reduza resolução de render, texturas, número de materiais e draw calls conforme profiling.

**Por que isso importa?** Desktop potente não representa o público final.

**Como fazer:**

1. Meça frame time.
2. Ajuste DPR.
3. Minimize materiais.
4. Compare.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 10. Minha cena atrapalha o botão de comprar; como evitar?

**Resposta:** Separe canvas e elementos HTML, mantenha hierarquia de foco e toque.

**Por que isso importa?** 3D nunca deve bloquear conversão ou acessibilidade.

**Como fazer:**

1. Teste toque no CTA.
2. Ajuste pointer events.
3. Confirme teclado.
4. Meça.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 11. Como implementar 3D em WordPress sem trocar todo tema?

**Resposta:** Use área isolada, staging e script de viewer com versão conhecida.

**Por que isso importa?** Evita conflitos de plugin e perda de site já publicado.

**Como fazer:**

1. Faça backup.
2. Crie página de teste.
3. Insira model-viewer.
4. Verifique cache.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 12. Qual o formato certo para e-commerce com AR?

**Resposta:** GLB atende muitos fluxos web/Android, enquanto USDZ/Quick Look cobre casos Apple.

**Por que isso importa?** Não há garantia universal em um só arquivo.

**Como fazer:**

1. Defina públicos.
2. Exporte formatos.
3. Teste Android/iPhone.
4. Ofereça alternativa.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 13. Onde encontro norma oficial para 3D Commerce?

**Resposta:** A Khronos mantém diretrizes de criação em tempo real para comércio, com exemplos técnicos.

**Por que isso importa?** Permite produzir modelos consistentes para múltiplos viewers.

**Como fazer:**

1. Leia 3D Commerce.
2. Aplique escala e PBR.
3. Rode validador glTF.
4. Compare resultado.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/index.html

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
