# FAQ — Modelagem, cenários e geometria

**8 dúvidas com resposta, importância, passo a passo e documentação.** [Voltar ao índice](README.md).

## 1. Como criar uma sala 3D?

**Resposta:** Comece por chão e paredes dimensionados; adicione aberturas e móveis somente depois.

**Por que isso importa?** Escala e percurso corretos evitam retrabalho.

**Como fazer:**

1. Defina medidas.
2. Crie floor plane.
3. Extrude paredes.
4. Coloque portas.
5. Configure câmera.
6. Teste travessia.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 2. Como faço um personagem básico?

**Resposta:** Modele proporções com objetos simples, depois retopologia e rig quando necessário.

**Por que isso importa?** Personagem exige deformação diferente de produto estático.

**Como fazer:**

1. Crie silhueta com formas.
2. Separe articulações.
3. Faça malha coerente.
4. Adicione armature.
5. Teste poses.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 3. O que é low-poly e quando vale?

**Resposta:** É estilo ou estratégia com menos geometria; favorece tempo de carga e dispositivos menos potentes.

**Por que isso importa?** Ajuda games mobile e experiências sociais.

**Como fazer:**

1. Comece com silhueta mínima.
2. Ajuste materiais e luz.
3. Meça triângulos.
4. Teste movimento e aparência.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 4. Como conserto sombreamento estranho?

**Resposta:** Investigue normais invertidas, faces duplicadas, smooth shading e geometria não-manifold.

**Por que isso importa?** Sombras ruins podem parecer erro do material.

**Como fazer:**

1. Exiba orientação de faces.
2. Recalcule normais.
3. Remova duplicações.
4. Revise sharp edges.
5. Teste render.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 5. Quando usar escultura e quando modelagem poligonal?

**Resposta:** Escultura é boa para formas orgânicas detalhadas; poligonal facilita objetos controlados e modelos para rig.

**Por que isso importa?** Escolha evita converter escultura densa em asset pesado.

**Como fazer:**

1. Faça duas versões do mesmo objeto.
2. Compare edição.
3. Estime retopologia necessária.
4. Escolha processo.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 6. Como criar uma floresta sem travar o PC?

**Resposta:** Instancie árvores e vegetação, use variações e níveis de detalhe, limite sombras e materiais.

**Por que isso importa?** Duplicar malhas pesadas consome memória.

**Como fazer:**

1. Crie 3 modelos-base.
2. Distribua como instâncias.
3. Varie escala/rotação.
4. Use LOD.
5. Perfil de desempenho.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 7. Por que o objeto ficou enorme no motor?

**Resposta:** Possível divergência de unidades e escala na exportação/importação.

**Por que isso importa?** Em AR, tamanho errado compromete credibilidade.

**Como fazer:**

1. Inspecione unidades no Blender.
2. Aplique escala.
3. Exporte.
4. Compare com objeto de tamanho conhecido.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 8. Como encontro modelos prontos sem risco?

**Resposta:** Busque por finalidade e licença no catálogo; documente autor, URL, termos e uso pretendido.

**Por que isso importa?** Download gratuito não garante revenda ou uso em campanha.

**Como fazer:**

1. Filtre biblioteca.
2. Abra licença do item.
3. Baixe arquivo permitido.
4. Registre proveniência.
5. Teste importação isolada.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

