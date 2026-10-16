# FAQ 11 — Blender e modelagem — problemas de produção

**13 perguntas com resposta, justificativa e exercício.** [Voltar ao FAQ](README.md) · [Glossário](../GLOSSARIO/README.md).

## 1. Meu modelo está com faces invisíveis; o que verifico?

**Resposta:** Ordem das faces e normais invertidas podem fazê-las sumir pelo backface culling.

**Por que isso importa?** Faces orientadas incorretamente atrapalham render e exportação.

**Como fazer:**

1. Ative Face Orientation.
2. Selecione faces suspeitas.
3. Recalcule normais.
4. Valide no destino.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 2. Como corrigir uma malha non-manifold?

**Resposta:** Localize arestas soltas, faces internas e buracos na superfície.

**Por que isso importa?** Malha inválida pode quebrar física, baking e impressão.

**Como fazer:**

1. Ative verificação non-manifold.
2. Selecione região.
3. Refaça faces ou feche buracos.
4. Reavalie topologia.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 3. Por que minhas dimensões mudam quando exporto?

**Resposta:** Unidades, escala não aplicada e eixos do destino podem divergir.

**Por que isso importa?** Produto/AR com medida incorreta perde credibilidade.

**Como fazer:**

1. Registre dimensão conhecida.
2. Aplique escala quando apropriado.
3. Exporte com preset documentado.
4. Importe e meça.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 4. Quando vale aplicar modificadores definitivamente?

**Resposta:** Aplique somente quando o destino não puder interpretar o modificador e houver cópia original preservada.

**Por que isso importa?** Aplicação destrutiva remove flexibilidade e pode afetar rig.

**Como fazer:**

1. Duplique versão da origem.
2. Exporte malha avaliada.
3. Compare superfície.
4. Registre o modificador.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 5. Como criar um objeto espelhado sem duplicação pesada?

**Resposta:** Use Mirror Modifier ou instâncias conforme necessidade e suporte.

**Por que isso importa?** Economiza edição e reduz inconsistências.

**Como fazer:**

1. Defina origem/centro.
2. Adicione Mirror.
3. Ajuste clipping.
4. Inspecione seam.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 6. Por que a malha arredondada ficou irregular?

**Resposta:** Polos, loops mal distribuídos ou subdivisão excessiva podem criar ondulações.

**Por que isso importa?** Shading defeituoso aparece em renders e normal maps.

**Como fazer:**

1. Inspecione wireframe.
2. Reveja loops de suporte.
3. Compare subdivisão.
4. Corrija superfícies.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 7. Como escolher escala para um ambiente AR?

**Resposta:** Use medidas reais e unidade definida antes de esculpir detalhes.

**Por que isso importa?** AR de produto exige tamanho físico confiável.

**Como fazer:**

1. Escolha item com medidas conhecidas.
2. Configure sistema de unidades.
3. Modele.
4. Meça após exportar.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 8. Meu Bevel ficou feio; como arrumar?

**Resposta:** Considere escala, número de segmentos, largura e interseções com outras faces.

**Por que isso importa?** Bordas arredondadas ajudam realismo mas podem distorcer peça.

**Como fazer:**

1. Aplique escala de teste.
2. Reduza largura.
3. Compare segmentos.
4. Corrija geometria.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 9. Como usar instâncias numa floresta?

**Resposta:** Mantenha poucas geometrias-base e varie transformações em pontos distribuídos.

**Por que isso importa?** A repetição de malha evita custo elevado.

**Como fazer:**

1. Modele três árvores.
2. Instancie por Geometry Nodes.
3. Varie rotação.
4. Meça consumo.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 10. Preciso modelar o verso de toda peça?

**Resposta:** Depende de câmera, sombras, colisão e possibilidade de inspeção do usuário.

**Por que isso importa?** Faces invisíveis podem desperdiçar triângulos, mas removê-las pode causar falhas.

**Como fazer:**

1. Defina câmeras possíveis.
2. Teste giro completo.
3. Mantenha faces necessárias.
4. Compare custo.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 11. Como corrigir objetos importados com origem errada?

**Resposta:** Ajuste a origem ao pivô funcional antes de animar ou configurar física.

**Por que isso importa?** Pivô incorreto faz objetos girarem fora da posição.

**Como fazer:**

1. Identifique função da peça.
2. Posicione cursor.
3. Ajuste origem.
4. Teste rotação.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 12. Qual é o primeiro teste de retopologia?

**Resposta:** O importante é deformar ou subdividir a malha e ver se ela mantém volume e superfície.

**Por que isso importa?** Uma topologia bonita em wireframe pode falhar em uso.

**Como fazer:**

1. Crie versão leve.
2. Faça bake ou rig.
3. Aplique pose extrema.
4. Compare com high-poly.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

## 13. Como fazer backup de projeto Blender sem perder materiais?

**Resposta:** Guarde origem e recursos vinculados em pasta versionada, considerando bibliotecas externas.

**Por que isso importa?** Links quebrados de textura atrapalham manutenção e entrega.

**Como fazer:**

1. Organize pasta de projeto.
2. Empacote recursos permitidos.
3. Salve versão.
4. Reabra em outra máquina.

**Onde aprender / boas práticas:** https://docs.blender.org/manual/en/latest/modeling/

**Teste de aceitação:** documentar resultado com arquivo próprio, versão e limitações; sem teste real, classificar como não verificado.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
