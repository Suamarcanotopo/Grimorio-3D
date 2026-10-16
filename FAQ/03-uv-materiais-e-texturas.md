# FAQ — UV, materiais e texturas

**8 dúvidas com resposta, importância, passo a passo e documentação.** [Voltar ao índice](README.md).

## 1. Por que minha textura aparece esticada?

**Resposta:** Em geral porque as ilhas UV não representam bem a geometria ou têm densidade desigual.

**Por que isso importa?** Afeta leitura visual mesmo com textura premium.

**Como fazer:**

1. Aplique checkerboard.
2. Inspecione estiramento.
3. Ajuste seams.
4. Faça unwrap novamente.
5. Reavalie.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 2. Como faço UV Mapping pela primeira vez?

**Resposta:** Marque cortes lógicos na malha e abra as faces em uma imagem 2D.

**Por que isso importa?** Permite pintar e repetir materiais com controle.

**Como fazer:**

1. Selecione malha.
2. Marque seams.
3. Unwrap.
4. Abra UV Editor.
5. Use checker.
6. Faça pack.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 3. Como saber qual textura baixar?

**Resposta:** Busque materiais PBR com Base Color, Normal, Roughness e, se pertinente, Height/AO.

**Por que isso importa?** Mapas coerentes evitam resultado artificial.

**Como fazer:**

1. Escolha material.
2. Confira licença.
3. Baixe mapas.
4. Ligue nos sockets corretos.
5. Compare sob duas luzes.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 4. Por que meu normal map está invertido?

**Resposta:** Pode haver convenção DirectX/OpenGL diferente ou espaço de cor incorreto.

**Por que isso importa?** O relevo parece iluminar pelo lado errado.

**Como fazer:**

1. Defina textura como dados.
2. Confira canal verde.
3. Teste inversão se exigida.
4. Valide no destino.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 5. O que é baking e quando faço?

**Resposta:** É transferir detalhes high-poly para mapas de textura sobre a malha final.

**Por que isso importa?** Reduz polígonos sem perder grande parte do detalhe percebido.

**Como fazer:**

1. Prepare high e low.
2. Faça UV low.
3. Configure imagem de bake.
4. Gere normal/AO.
5. Teste material.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 6. Quero deixar metal realista; o que mudar?

**Resposta:** Ajuste Metallic, Roughness, iluminação refletida e escala do objeto.

**Por que isso importa?** Metal sem ambiente de reflexão parece plástico escuro.

**Como fazer:**

1. Ative material PBR.
2. Metallic 1.
3. Ajuste Roughness.
4. Adicione HDRI.
5. Compare resultado.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 7. Posso usar textura 4K em qualquer celular?

**Resposta:** Não; qualidade e memória devem ser medidas no dispositivo e distância de observação.

**Por que isso importa?** Texturas grandes aumentam download e consumo de VRAM.

**Como fazer:**

1. Teste 4K.
2. Gere 2K/1K/512.
3. Compare na tela real.
4. Retenha menor aceitável.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 8. Como montar materiais reutilizáveis?

**Resposta:** Crie um material mestre parametrizado com nomes consistentes e instâncias quando houver suporte.

**Por que isso importa?** Economiza tempo e reduz divergências.

**Como fazer:**

1. Monte material PBR.
2. Exponha parâmetros.
3. Salve como asset.
4. Crie variações.
5. Documente condições de exportação.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/meshes/uv/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

