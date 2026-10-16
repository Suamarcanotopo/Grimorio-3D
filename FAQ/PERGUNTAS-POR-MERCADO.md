# FAQ profissional por mercado — 26 perguntas com provas reais

Estas perguntas complementam as 80 perguntas da [FAQ original](README.md). O valor de cada resposta é oferecer orientação executável e fonte primária, não apenas siglas.

## 1. Como criar produto virtual sem enganar o consumidor?

**Mercado:** Publicidade.

**Resposta e importância:** Mostre as características reais, mantenha medidas, textura e cor coerentes com documentação do fabricante.

**Como fazer / testar:** Compare modelo com fotos autorizadas e registre diferenças.

**Onde estudar:** https://www.blender.org/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 2. Como usar 3D no funil comercial?

**Mercado:** Publicidade.

**Resposta e importância:** Use 3D quando ele esclarecer escala, variantes, encaixe ou funcionamento.

**Como fazer / testar:** Estabeleça métrica de interação, integre GLB e CTA e teste baseline sem 3D.

**Onde estudar:** https://modelviewer.dev/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 3. Por que nem sempre animação 3D melhora anúncios?

**Mercado:** Publicidade.

**Resposta e importância:** Pode aumentar carregamento, distrair do CTA e consumir orçamento sem ganho demonstrável.

**Como fazer / testar:** Faça teste comparativo de página ou peça com e sem 3D.

**Onde estudar:** https://www.w3.org/WAI/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 4. Como planejar uma tomada que receberá VFX?

**Mercado:** Cinema.

**Resposta e importância:** Capture referência de câmera, lente, iluminação e escala antes de filmar.

**Como fazer / testar:** Filme 5s com parallax e anote distância focal e referências espaciais.

**Onde estudar:** https://docs.blender.org/manual/en/latest/movie_clip/tracking/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 5. Por que filmar sem tracking markers pode gerar retrabalho?

**Mercado:** Cinema.

**Resposta e importância:** Cena lisa e sem parallax dificulta reconstrução de câmera.

**Como fazer / testar:** Grave tomada de teste e faça solve antes do set definitivo.

**Onde estudar:** https://docs.blender.org/manual/en/latest/movie_clip/tracking/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 6. Qual a função de EXR na pós-produção?

**Mercado:** Cinema.

**Resposta e importância:** Guarda passes HDR e canais úteis para composição sem destruir dados de luz cedo demais.

**Como fazer / testar:** Renderize 1 frame EXR e compare com PNG em compositor.

**Onde estudar:** https://www.openexr.com/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 7. O que preciso para filmar com LED Volume?

**Mercado:** Cinema.

**Resposta e importância:** Render em tempo real, tracking, sincronismo, nDisplay e teste de palco.

**Como fazer / testar:** Estude ICVFX oficial e simule arquitetura antes de alugar equipamentos.

**Onde estudar:** https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-overview-in-unreal-engine

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 8. Como revisar se o personagem realmente atua?

**Mercado:** Animação.

**Resposta e importância:** Observe intenção, timing, leitura da silhueta e força de poses.

**Como fazer / testar:** Crie animatic sem som e peça a outra pessoa para narrar o que entendeu.

**Onde estudar:** https://studio.blender.org/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 9. Por que rig precisa ser testado antes de texturizar tudo?

**Mercado:** Animação.

**Resposta e importância:** Pesos e loops incorretos podem exigir reestruturar a malha.

**Como fazer / testar:** Teste poses extremas de ombro, boca, joelho e mãos com material neutro.

**Onde estudar:** https://docs.blender.org/manual/en/latest/animation/armatures/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 10. Como saber se o game está divertido antes dos assets finais?

**Mercado:** Games.

**Resposta e importância:** Valide a mecânica central com geometria simples e jogadores reais.

**Como fazer / testar:** Crie nível blockout com vitória/derrota e registre dificuldades observadas.

**Onde estudar:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 11. Como escolher orçamento de triângulos?

**Mercado:** Games.

**Resposta e importância:** Não existe valor universal: depende de câmera, resolução, shaders, CPU/GPU e público.

**Como fazer / testar:** Faça perfil com três versões de asset no dispositivo-alvo.

**Onde estudar:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 12. O que otimizar primeiro em cenário pesado?

**Mercado:** Games.

**Resposta e importância:** Meça draw calls, sombras, texturas, CPU/GPU e overdraw antes de mexer.

**Como fazer / testar:** Remova uma variável por vez e compare frame time.

**Onde estudar:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 13. Como escolher entre model-viewer e Three.js?

**Mercado:** Web3D.

**Resposta e importância:** model-viewer é adequado à exibição direta de modelos; Three.js para interação mais profunda.

**Como fazer / testar:** Prototipe no model-viewer e migre só se houver requisito não atendido.

**Onde estudar:** https://modelviewer.dev/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 14. Como não prejudicar SEO com 3D?

**Mercado:** Web3D.

**Resposta e importância:** Preserve HTML semântico, texto, CTA, layout estável, performance e fallback.

**Como fazer / testar:** Meça LCP, INP, CLS e usabilidade mobile com e sem 3D.

**Onde estudar:** https://web.dev/learn/performance

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 15. Qual a diferença entre glTF e arquivo BLEND?

**Mercado:** Web3D.

**Resposta e importância:** BLEND guarda edição específica do Blender; glTF é intercâmbio para render em runtime.

**Como fazer / testar:** Exporte GLB, reimporte e compare materiais e animações.

**Onde estudar:** https://www.khronos.org/gltf/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 16. Por que AR não funciona em todo celular?

**Mercado:** AR.

**Resposta e importância:** Depende de hardware, navegador, SDK, permissões e formatos.

**Como fazer / testar:** Faça matriz Android/iOS com modelos e versões reais e fallback.

**Onde estudar:** https://developers.google.com/ar

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 17. Como garantir escala correta de móvel na sala?

**Mercado:** AR.

**Resposta e importância:** Modele em unidades reais e teste medidas no dispositivo durante ancoragem.

**Como fazer / testar:** Coloque cadeira virtual junto de uma régua ou móvel medido.

**Onde estudar:** https://developers.google.com/ar/develop/anchors

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 18. Como diferenciar Lens Snapchat, TikTok e Meta Quest?

**Mercado:** AR.

**Resposta e importância:** São runtimes e canais distintos com SDKs, editor e políticas próprios.

**Como fazer / testar:** Escolha canal antes de modelar e leia a matriz de handoffs.

**Onde estudar:** https://developers.snap.com/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 19. Como começar âncoras compartilhadas?

**Mercado:** AR.

**Resposta e importância:** ARCore Cloud Anchors requer sessão, serviço e compartilhamento de ID.

**Como fazer / testar:** Siga documentação em dois aparelhos e revise privacidade/quotas.

**Onde estudar:** https://developers.google.com/ar/develop/cloud-anchors

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 20. Posso usar render para validar peça mecânica?

**Mercado:** Indústria.

**Resposta e importância:** Não; engenharia exige tolerância, material, cargas e revisão habilitada.

**Como fazer / testar:** Compare medidas STEP/IFC com malha triangulada, documente limitações.

**Onde estudar:** https://www.freecad.org/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 21. Por que não modelar tudo apenas em triangulos?

**Mercado:** Indústria.

**Resposta e importância:** CAD paramétrico e BIM preservam intenção e propriedades que uma malha simples não mantém.

**Como fazer / testar:** Crie peça paramétrica, altere dimensão e compare com OBJ exportado.

**Onde estudar:** https://www.freecad.org/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 22. Como transformar fonte inglesa em tutorial útil em português?

**Mercado:** Estudo.

**Resposta e importância:** Traduza conceito e método, conserve termos de interface e reproduza exercício original.

**Como fazer / testar:** Faça exercício com screenshot autoral e link fonte; não copie o curso.

**Onde estudar:** https://docs.blender.org/manual/en/latest/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 23. Como saber que aprendi mesmo uma técnica?

**Mercado:** Estudo.

**Resposta e importância:** Explique em linguagem simples, reproduza sem vídeo e corrija um defeito criado de propósito.

**Como fazer / testar:** Use rubrica, revise com pessoa experiente e registre evidências.

**Onde estudar:** https://www.siggraph.org/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 24. Como tornar esse conhecimento útil para uma Skill de IA?

**Mercado:** Skills.

**Resposta e importância:** Declare capabilities, gatilhos, inputs, limites, fontes atuais, tests e interlocks.

**Como fazer / testar:** Escolha uma única competência e faça dez casos positivos/adversariais.

**Onde estudar:** https://github.com/Suamarcanotopo/grimorio-skills

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 25. Uma biblioteca gratuita pode ser usada na publicidade?

**Mercado:** Segurança.

**Resposta e importância:** Grátis para baixar não confirma licença comercial, imagem/marca ou redistribuição.

**Como fazer / testar:** Leia termos por item e arquive versão e autor antes de usar.

**Onde estudar:** https://creativecommons.org/licenses/

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.

## 26. Como processar GLB enviado por terceiros com segurança?

**Mercado:** Segurança.

**Resposta e importância:** Arquivos externos exigem validação de formato, tamanho, metadados, licença e isolamento.

**Como fazer / testar:** Limite upload e armazene em quarentena antes de abrir em ferramenta automatizada.

**Onde estudar:** https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

**Critério de evidência:** arquivo próprio, versão, plataforma, observação e status; sem teste = não verificado.


[Voltar aos dez mercados](../NICHOS/README.md) · [Currículo de 18 etapas](../CURRICULO/ETAPAS-DA-PRODUCAO.md) · [Política de fontes](../GOVERNANCA/FONTES-ATEMPORAIS-E-ATUAIS.md)
