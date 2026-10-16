# FAQ 16 — Games, Unreal, Unity e performance avançada

**13 perguntas**, respostas práticas e critérios verificáveis. [Voltar ao FAQ](README.md).

## 1. Como iniciar um jogo sem criar um mundo imenso?

**Resposta:** Defina uma única mecânica divertida e faça blockout jogável antes da arte.

**Por que isso importa?** Escopo pequeno permite aprender o loop de jogo.

**Como fazer:**

1. Escolha objetivo.
2. Configure personagem e câmera.
3. Faça colisão.
4. Teste vitória.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 2. Como criar interação sem programar C++?

**Resposta:** Blueprints Unreal e ferramentas visuais permitem muitos protótipos sem código textual.

**Por que isso importa?** Reduz barreira de entrada e acelera validação de ideias.

**Como fazer:**

1. Crie Actor.
2. Evento de input.
3. Altere material ou posição.
4. Teste.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 3. Quando vale usar Nanite?

**Resposta:** Quando geometria, plataforma e materiais se adequam às capacidades documentadas do Unreal.

**Por que isso importa?** Nanite não elimina todos limites, especialmente de plataforma/XR.

**Como fazer:**

1. Confira suporte.
2. Faça teste com asset.
3. Compare frame time.
4. Decida.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 4. Por que Lumen tem resultado ruim em meu projeto mobile?

**Resposta:** Recursos e caminhos de renderização variam por hardware, API e versão da Unreal.

**Por que isso importa?** Configuração desktop pode não ser viável no celular.

**Como fazer:**

1. Cheque matriz de suporte.
2. Troque iluminação.
3. Rode build mobile.
4. Compare.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 5. Como projetar um material que funcione em VR?

**Resposta:** Simplifique recursos caros, confira render path e orçamento do headset.

**Por que isso importa?** Frames instáveis podem causar desconforto.

**Como fazer:**

1. Crie material básico.
2. Teste VR.
3. Meça GPU.
4. Ajuste shading.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 6. Como reduzir custo de vegetação em Unreal?

**Resposta:** Instancing, culling, LOD/HLOD e sombras podem ajudar conforme cena.

**Por que isso importa?** Folhas transparentes causam overdraw e custo GPU.

**Como fazer:**

1. Perfil vegetação.
2. Reduza translucência.
3. Ajuste instâncias.
4. Compare.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 7. O que é o primeiro profiler que devo usar?

**Resposta:** Escolha ferramenta da engine capaz de separar CPU, GPU, tempo de quadro e memória.

**Por que isso importa?** A otimização correta depende do gargalo real.

**Como fazer:**

1. Execute build.
2. Colete frame time.
3. Isole efeito pesado.
4. Refaça medição.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 8. Como evitar erro de colisão em objeto importado?

**Resposta:** Configure geometria simples de colisão e valide pivôs e escala após importação.

**Por que isso importa?** Colisões complexas podem pesar ou impedir movimento.

**Como fazer:**

1. Importe mesh.
2. Adicione collider.
3. Teste caminhar/empurrar.
4. Revise física.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 9. Qual a diferença de gameplay Blueprint e animação?

**Resposta:** Blueprint de gameplay reage a eventos; animação controla poses e movimento visual do objeto.

**Por que isso importa?** Misturar as duas responsabilidades pode dificultar manutenção.

**Como fazer:**

1. Crie evento de salto.
2. Dispare estado de animação.
3. Teste transição.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 10. Posso usar modelos de qualquer marketplace num jogo?

**Resposta:** Depende de licença específica, uso comercial, redistribuição de fontes e limitações de motor.

**Por que isso importa?** Compra de asset não implica propriedade total.

**Como fazer:**

1. Leia EULA do item.
2. Registre recibo/licença.
3. Integre em projeto.
4. Proteja fonte.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 11. Como preparar um nível para mobile?

**Resposta:** Controle tamanho dos assets, texturas, shaders, sombras e interação por perfil do dispositivo.

**Por que isso importa?** Mobile tem restrições de energia, memória e GPU.

**Como fazer:**

1. Defina aparelho básico.
2. Faça build.
3. Meça.
4. Ajuste e reteste.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 12. Como comparar Unreal e Unity para um mesmo projeto?

**Resposta:** Teste protótipos equivalentes com mesmo asset, câmera, efeitos e alvo.

**Por que isso importa?** Ranking geral de engines não substitui requisitos concretos.

**Como fazer:**

1. Faça POC nas duas.
2. Meça build/performance.
3. Compare treinamento.
4. Escolha.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 13. Por que minha animação importada parece diferente?

**Resposta:** Rig, pose base, escala, import flags e compressão podem mudar o resultado.

**Por que isso importa?** Incompatibilidade na entrega pode destruir acting.

**Como fazer:**

1. Revise skeleton.
2. Compare pose.
3. Ajuste retarget.
4. Observe motion curves.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
