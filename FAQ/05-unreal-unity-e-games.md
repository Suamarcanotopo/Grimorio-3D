# FAQ — Unreal, Unity e games

**8 dúvidas com resposta, importância, passo a passo e documentação.** [Voltar ao índice](README.md).

## 1. Como levo modelo Blender ao Unreal?

**Resposta:** Exporte FBX ou glTF conforme conteúdo/versão; confira escala, orientação, UV e materiais.

**Por que isso importa?** O arquivo transferido raramente preserva 100% dos nós do Blender.

**Como fazer:**

1. Salve BLEND.
2. Organize nomes/UV.
3. Exporte.
4. Importe no Unreal.
5. Compare material e escala.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 2. O que são Blueprints no Unreal?

**Resposta:** São grafos de lógica visual para eventos, interação e sistemas.

**Por que isso importa?** Permitem prototipar sem começar por código C++.

**Como fazer:**

1. Crie Actor Blueprint.
2. Adicione Static Mesh.
3. Vincule evento de clique.
4. Troque material.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 3. Como começo um game 3D?

**Resposta:** Faça um protótipo jogável com movimento, câmera, colisão e objetivo simples.

**Por que isso importa?** Um cenário bonito sem regras não valida diversão.

**Como fazer:**

1. Escolha template do motor.
2. Adicione personagem.
3. Implemente meta simples.
4. Teste 3 minutos.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 4. Como adiciono colisão ao objeto?

**Resposta:** Defina malhas de colisão adequadas e valide comportamento físico.

**Por que isso importa?** Sem colisão o jogador atravessa paredes ou chão.

**Como fazer:**

1. Importe objeto.
2. Crie colisão simples.
3. Teste caminhada.
4. Ajuste complexidade.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 5. Qual a diferença entre Nanite e LOD tradicional?

**Resposta:** Nanite é solução de geometria virtualizada em cenários suportados pela Unreal; LOD são variantes discretas.

**Por que isso importa?** Escolha depende de motor, plataforma e efeitos usados.

**Como fazer:**

1. Consulte suporte da Unreal alvo.
2. Teste asset com Nanite.
3. Compare métricas e fallback.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 6. Por que meu FPS caiu depois de adicionar vegetação?

**Resposta:** Pode haver excesso de draw calls, sombras, transparência, overdraw e geometria.

**Por que isso importa?** Antes de reduzir polígonos é preciso localizar gargalo.

**Como fazer:**

1. Abra profiler.
2. Meça GPU/CPU.
3. Isole folhas/sombras.
4. Use instancing/LOD.
5. Meça novamente.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 7. Qual o papel do Level Design?

**Resposta:** Organiza circulação, orientação, dificuldade e experiências do ambiente.

**Por que isso importa?** O visual deve apoiar clareza e objetivos.

**Como fazer:**

1. Faça blockout com caixas.
2. Percorra com jogador.
3. Ajuste sinais.
4. Depois detalhe.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

## 8. Unreal é sempre melhor que Unity?

**Resposta:** Não: motores têm forças diferentes e o melhor depende da equipe, plataforma, compatibilidade, licenças e custo.

**Por que isso importa?** Evita migração por tendência sem avaliação.

**Como fazer:**

1. Especifique alvo.
2. Prototipe mesma cena em dois motores.
3. Meça tempo e tamanho.
4. Decida.

**Onde aprender / boas práticas:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Teste de aceitação:** execute o procedimento em um arquivo próprio, confira no destino e registre o que funcionou. Se a funcionalidade depender de plano ou dispositivo, mantenha o resultado como *não verificado* até testar.

