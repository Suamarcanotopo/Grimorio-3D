# FAQ 15 — Realidade aumentada, Snapchat, TikTok e Meta Quest

**13 perguntas**, respostas práticas e critérios verificáveis. [Voltar ao FAQ](README.md).

## 1. Como começo AR com produto sem aplicativo instalado?

**Resposta:** Use visualizador web com GLB e modos AR compatíveis ao dispositivo.

**Por que isso importa?** Evita iniciar SDK complexo sem validar valor.

**Como fazer:**

1. Prepare GLB.
2. Publique HTTPS.
3. Teste Scene Viewer/Quick Look.
4. Mantenha fallback.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 2. Qual a diferença entre WebAR e Camera Kit Web?

**Resposta:** WebAR de produto pode exibir objeto no ambiente; Camera Kit oferece efeitos de câmera da Snap por SDK específico.

**Por que isso importa?** São integrações diferentes com contratos e custos.

**Como fazer:**

1. Defina experiência.
2. Leia SDK apropriado.
3. Faça protótipo.
4. Teste permissões.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 3. Como saber se uma Lens Snap pode ir ao meu site?

**Resposta:** Consulte critérios Camera Kit, disponibilidade de conta/Lens, licença e suporte Web SDK.

**Por que isso importa?** Lens publicada no Snapchat não está automaticamente liberada em terceiros.

**Como fazer:**

1. Confirme Lens ID.
2. Verifique acesso SDK.
3. Monte staging.
4. Teste câmera.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 4. Preciso pagar para distribuir filtro TikTok?

**Resposta:** Os planos, regras e serviços podem mudar; é preciso conferir políticas oficiais vigentes.

**Por que isso importa?** Prometer publicação gratuita permanente é inseguro.

**Como fazer:**

1. Leia condições atuais.
2. Revise direitos do efeito.
3. Submeta teste.
4. Registre custos.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 5. Como importar personagem animado no Effect House?

**Resposta:** Prepare rig e clipes suportados, reduza geometria e siga formato/limites do guia da versão.

**Por que isso importa?** Rigs de desktop não são sempre portáveis para filtros móveis.

**Como fazer:**

1. Valide skeleton.
2. Faça export compatível.
3. Importe animação.
4. Rode profiler.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 6. Meu filtro perde contato com o rosto; como melhoro?

**Resposta:** Tracking pode depender de iluminação, oclusões, pose e referência de câmera.

**Por que isso importa?** Um efeito instável pode causar reprovação ou má experiência.

**Como fazer:**

1. Teste diferentes luzes.
2. Reduza acessórios pesados.
3. Ajuste landmarks.
4. Reteste.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 7. AR de objetos na rua requer internet?

**Resposta:** Algumas âncoras ou serviços geoespaciais dependem de rede e cobertura; local anchors podem ter requisitos distintos.

**Por que isso importa?** Disponibilidade muda entre sistemas e regiões.

**Como fazer:**

1. Escolha tipo de âncora.
2. Leia quotas.
3. Teste offline/online.
4. Documente fallback.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 8. Posso colocar uma Lens TikTok diretamente num site?

**Resposta:** Effect House é voltado à plataforma TikTok; para sites, escolha WebAR ou SDK que ofereça integração documentada.

**Por que isso importa?** Não existe embed universal entre redes sociais.

**Como fazer:**

1. Defina público web.
2. Pesquise SDK suportado.
3. Faça protótipo próprio.
4. Valide termos.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 9. Quais dados de câmera posso armazenar numa experiência AR?

**Resposta:** A coleta depende de base legal, finalidade, permissão e políticas; em muitos casos não é necessário armazenar frames.

**Por que isso importa?** Reduz risco de privacidade e proteção de dados.

**Como fazer:**

1. Liste dados necessários.
2. Solicite permissão contextual.
3. Evite gravação.
4. Revise retenção.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 10. Como medir conforto numa experiência Meta Quest?

**Resposta:** Avalie estabilidade do frame time, orientação, locomoção, controles e duração com dispositivos reais.

**Por que isso importa?** Conforto XR não pode ser inferido de preview desktop.

**Como fazer:**

1. Selecione headset.
2. Rode app.
3. Registre FPS/frame time.
4. Peça feedback seguro.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 11. Como criar objeto que fique fixo na sala?

**Resposta:** Use tracking de ambiente e âncora espacial suportada, com medidas coerentes.

**Por que isso importa?** Objetos soltos ou tremendo comprometem credibilidade da AR.

**Como fazer:**

1. Identifique plano.
2. Adicione âncora.
3. Teste mudança de posição.
4. Recalibre se necessário.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 12. É possível criar AR compartilhada entre dois celulares?

**Resposta:** Sim com serviços/SDKs que ofereçam âncoras compartilhadas e sincronismo.

**Por que isso importa?** Experiência colaborativa exige estado comum e privacidade.

**Como fazer:**

1. Teste dois aparelhos.
2. Gere Cloud Anchor autorizada.
3. Compartilhe ID.
4. Verifique alinhamento.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 13. Como escolher entre Snap, TikTok e Quest para uma campanha?

**Resposta:** Snap e TikTok focam experiências em canais sociais; Quest é headset com outra distribuição e público.

**Por que isso importa?** Escolher pelo hype pode elevar custo sem alcançar o consumidor.

**Como fazer:**

1. Especifique público e ação.
2. Compare SDK e termos.
3. Prototipe.
4. Meça engajamento.

**Onde aprender / boas práticas:** https://developers.snap.com/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
