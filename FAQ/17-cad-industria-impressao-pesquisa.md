# FAQ 17 — CAD, indústria, impressão 3D e pesquisa técnica

**13 perguntas**, respostas práticas e critérios verificáveis. [Voltar ao FAQ](README.md).

## 1. Qual diferença entre STL e STEP?

**Resposta:** STL descreve triângulos da superfície; STEP pode preservar entidades CAD e geometria precisa.

**Por que isso importa?** Uma peça industrial não deve perder intenção paramétrica na entrega.

**Como fazer:**

1. Modele peça CAD.
2. Exporte STEP e STL.
3. Compare edição.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 2. Por que IFC é importante em arquitetura?

**Resposta:** IFC descreve elementos e propriedades BIM além de uma simples cena visual.

**Por que isso importa?** Permite interoperabilidade em obras e instalações.

**Como fazer:**

1. Crie porta com propriedades.
2. Exporte IFC.
3. Reimporte em viewer.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 3. Como verificar escala de modelo BIM?

**Resposta:** Compare sistema de unidades, referência geográfica e dimensões de objetos conhecidos.

**Por que isso importa?** Erro de unidade pode criar prejuízo operacional.

**Como fazer:**

1. Escolha parede conhecida.
2. Meça na origem.
3. Exporte.
4. Meça no destino.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 4. Meu STL não imprime; o que procuro?

**Resposta:** Geometria non-manifold, paredes finas, interseções e orientação podem impedir o slicing.

**Por que isso importa?** Ter render bonito não prova viabilidade de fabricação.

**Como fazer:**

1. Rode inspeção de malha.
2. Repare superfície.
3. Faça slice.
4. Revise preview.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 5. Qual altura de camada usar numa primeira impressão?

**Resposta:** Depende de bico, material, acabamento e capacidade da máquina; use o perfil oficial como baseline.

**Por que isso importa?** Valores fixos sem dispositivo não são recomendação segura.

**Como fazer:**

1. Selecione impressora.
2. Abra perfil fornecedor.
3. Faça peça de teste.
4. Compare.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 6. Como reduzir suportes de impressão 3D?

**Resposta:** Reoriente peça, altere geometria de overhang e configure suporte conforme material.

**Por que isso importa?** Suporte demais desperdiça material e causa marcas.

**Como fazer:**

1. Teste três orientações.
2. Analise slicer.
3. Compare acabamento.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 7. Como criar um encaixe mecânico que funcione?

**Resposta:** Determine tolerâncias, material, processo e expansão/contração da fabricação.

**Por que isso importa?** Folga zero digital pode impedir montagem real.

**Como fazer:**

1. Modele encaixe.
2. Defina tolerância.
3. Faça amostra.
4. Ajuste projeto.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 8. O que é digital twin além de modelo bonito?

**Resposta:** Gêmeo digital relaciona representação com dados/estados relevantes do sistema real.

**Por que isso importa?** Sem atualização e sem dados, normalmente é apenas visualização digital.

**Como fazer:**

1. Defina variável física.
2. Vincule dado de demonstração.
3. Atualize estado 3D.
4. Teste.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 9. Como levar uma cidade grande para um website?

**Resposta:** Tecnologias como 3D Tiles possibilitam streaming por níveis de detalhe.

**Por que isso importa?** Carregar todo município em um GLB geralmente é inviável.

**Como fazer:**

1. Classifique datasets.
2. Gere tiles permitidos.
3. Carregue região.
4. Meça rede.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 10. Como escolher dados geográficos para cena 3D?

**Resposta:** Verifique CRS, precisão espacial, atualização, direitos e área de cobertura.

**Por que isso importa?** Um mapa visualmente bonito pode estar em coordenadas erradas.

**Como fazer:**

1. Baixe dataset autorizado.
2. Identifique CRS.
3. Converta terreno.
4. Confira escala.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 11. Posso usar imagens médicas em projetos 3D públicos?

**Resposta:** É necessário observar autorização, privacidade, finalidade e condições dos datasets.

**Por que isso importa?** Imagens médicas frequentemente contêm dados sensíveis.

**Como fazer:**

1. Escolha dataset público anonimizado.
2. Revise termos.
3. Faça segmentação.
4. Não inclua dados pessoais.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 12. Qual ferramenta é apropriada à impressão paramétrica gratuita?

**Resposta:** FreeCAD ou OpenSCAD são opções, dependendo de preferência por interface ou código.

**Por que isso importa?** Parametrização facilita revisão de medidas.

**Como fazer:**

1. Crie mesma peça em dois fluxos.
2. Ajuste uma dimensão.
3. Compare resultados.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

## 13. Por que não usar arquivo de game como projeto de engenharia?

**Resposta:** Malhas de games podem carecer de precisão, atributos e propriedades requeridas em CAD/BIM.

**Por que isso importa?** Renderizador e sistema técnico possuem contratos diferentes.

**Como fazer:**

1. Revise requisitos de tolerância.
2. Preserve STEP/IFC.
3. Gere GLB apenas para visualização.

**Onde aprender / boas práticas:** https://technical.buildingsmart.org/standards/IFC/

**Teste de aceitação:** guarde resultado, versão e limitações; nunca declare teste real sem executar.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D no WhatsApp](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Apoie o projeto com uma estrela no GitHub.
