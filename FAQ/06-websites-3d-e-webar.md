# FAQ — Websites 3D e WebAR

**8 dúvidas com resposta, importância, passo a passo e documentação.** [Voltar ao índice](README.md).

## 1. Como colocar produto 3D no meu site?

**Resposta:** Comece com model-viewer, arquivo GLB próprio, poster e descrição alternativa.

**Por que isso importa?** É o caminho mais simples para testar valor comercial.

**Como fazer:**

1. Exporte GLB.
2. Hospede com MIME correto.
3. Use model-viewer.
4. Ative câmera.
5. Teste mobile.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 2. Como ativar AR no Android pelo site?

**Resposta:** Use model-viewer com ar e modo Scene Viewer em dispositivo ARCore compatível.

**Por que isso importa?** O cliente pode experimentar o produto no ambiente.

**Como fazer:**

1. Publique GLB HTTPS.
2. Ative ar.
3. Teste aparelho ARCore.
4. Ofereça visualização 3D alternativa.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 3. Como ativar AR no iPhone pelo site?

**Resposta:** Use Quick Look com USDZ ou conversão suportada por model-viewer em Safari compatível.

**Por que isso importa?** Ecossistemas usam formatos e fluxos diferentes.

**Como fazer:**

1. Prepare modelo com escala real.
2. Verifique USDZ ou opção model-viewer.
3. Abra em iPhone.
4. Teste no espaço.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 4. AR do navegador funciona em todo celular?

**Resposta:** Não: depende de hardware, navegador, permissões e runtime.

**Por que isso importa?** Prometer compatibilidade universal cria frustração.

**Como fazer:**

1. Liste dispositivos alvo.
2. Teste Android/iOS.
3. Detecte suporte.
4. Mostre fallback.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 5. O que é Three.js e quando escolher?

**Resposta:** Biblioteca de cenas 3D em JavaScript para experiências altamente personalizadas.

**Por que isso importa?** Oferece mais controle do que visualizador simples.

**Como fazer:**

1. Crie scene.
2. Adicione camera.
3. Adicione mesh.
4. Configure renderer.
5. Anime sob demanda.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 6. React Three Fiber é obrigatório?

**Resposta:** Não; é uma abstração para projetos React, não requisito para todo Web3D.

**Por que isso importa?** Evita complexidade desnecessária em WordPress ou HTML.

**Como fazer:**

1. Teste model-viewer.
2. Determine necessidades interativas.
3. Adote Three.js/R3F somente se compensar.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 7. Como impedir que 3D deixe o site lento?

**Resposta:** Use carregamento progressivo, compressão, limites de render e fallback, medindo em aparelhos reais.

**Por que isso importa?** Conversão e SEO podem piorar com página pesada.

**Como fazer:**

1. Reserve espaço.
2. Exiba poster.
3. Lazy load GLB.
4. Meça LCP e INP.
5. Otimize.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 8. Como criar cena 3D em WordPress?

**Resposta:** Insira componente web ou módulo isolado e evite scripts conflitantes do tema/plugins.

**Por que isso importa?** Mantém WordPress gerenciável e reversível.

**Como fazer:**

1. Crie backup/staging.
2. Carregue GLB autorizado.
3. Incorpore model-viewer com script fixado.
4. Teste mobile e cache.

**Onde aprender / boas práticas:** https://modelviewer.dev/docs/

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

