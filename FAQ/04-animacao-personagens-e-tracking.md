# FAQ — Animação, personagens e tracking

**8 dúvidas com resposta, importância, passo a passo e documentação.** [Voltar ao índice](README.md).

## 1. Como animar um objeto em 5 minutos?

**Resposta:** Insira quadros-chave de localização/rotação em instantes diferentes.

**Por que isso importa?** Ensina timeline sem depender de rig.

**Como fazer:**

1. Crie cubo.
2. Quadro 1 insira Location.
3. Quadro 48 mova.
4. Insira novo keyframe.
5. Reproduza.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 2. Como evitar pés deslizando na caminhada?

**Resposta:** Confira root motion, pose base, contato do pé e sincronização entre deslocamento e ciclo.

**Por que isso importa?** Deslizamento quebra a credibilidade da animação.

**Como fazer:**

1. Observe foot contact.
2. Revise curvas.
3. Trave IK quando útil.
4. Teste no motor.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 3. Como colocar ossos em personagem?

**Resposta:** Crie uma armature com hierarquia coerente, vincule a malha e pinte pesos.

**Por que isso importa?** Sem pesos corretos braços e joelhos deformam errado.

**Como fazer:**

1. Crie armature.
2. Nomeie ossos.
3. Faça bind.
4. Ajuste Weight Paint.
5. Teste poses extremas.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 4. Qual a diferença entre IK e FK?

**Resposta:** IK posiciona extremidade e resolve juntas; FK gira cada osso da cadeia.

**Por que isso importa?** Cada estratégia facilita movimentos distintos.

**Como fazer:**

1. Anime braço com FK.
2. Repita com alvo IK.
3. Compare naturalidade e controle.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 5. Como importar animação do Mixamo?

**Resposta:** Obtenha animação permitida, confira FBX, rig e retargeting no destino.

**Por que isso importa?** Personagens e animações nem sempre têm skeleton idêntico.

**Como fazer:**

1. Escolha animação.
2. Leia licença.
3. Baixe FBX.
4. Importe.
5. Confirme escala.
6. Retarget se necessário.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 6. Como fazer tracking de câmera de vídeo?

**Resposta:** Use marcadores estáveis e movimento com parallax para resolver posição da câmera.

**Por que isso importa?** Permite compor 3D no mundo filmado.

**Como fazer:**

1. Importe tomada.
2. Marque features.
3. Track.
4. Solve Camera.
5. Calibre chão/escala.
6. Teste objeto.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 7. Posso rastrear rosto de qualquer pessoa?

**Resposta:** Não é prudente; identifique base legal, consentimento/autorização e destino de gravação.

**Por que isso importa?** Rosto e expressão podem envolver dados pessoais e riscos de imagem.

**Como fazer:**

1. Defina finalidade.
2. Peça autorização.
3. Minimize retenção.
4. Teste em ambiente controlado.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 8. Como juntar render 3D com filmagem?

**Resposta:** Faça matchmove, compatibilize luz/lente e use máscaras de oclusão.

**Por que isso importa?** Sem correspondência de perspectiva o objeto parece colado.

**Como fazer:**

1. Resolva câmera.
2. Renderize passes.
3. Ajuste cor/sombra.
4. Faça composição.
5. Revise frame a frame.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/animation/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

