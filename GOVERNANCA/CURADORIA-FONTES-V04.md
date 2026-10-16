# Curadoria v0.4 — expansão isolada de fontes 3D

**Data:** 16/10/2026 · **Etapa:** 1 — somente fontes; sem modificar glossário, FAQ, Skills ou runtime.

## Resultados

- Baseline GitHub: 238 fichas canônicas com IDs `SIN3D-001` a `SIN3D-238` preservados.
- Ampliação até **368 fontes** nos mesmos **38 nichos**, com **130 IDs novos**, sem duplicação de URL normalizada.
- Três commits de curadoria preservam o progresso incremental; apenas este checkpoint sincroniza README, INDEX, CSV e fichas dos nichos.
- Mecanismo de proteção: 5 validadores de CI, inclusive gerador idempotente do README e links internos.

## Critérios de proveniência

A expansão prioriza `docs.blender.org`, `dev.epicgames.com`, `khronos.org`, `sidefx.com`, `autodesk.com`, `apple.com`, `google.com`, `w3.org`, `3mf.io`, `buildingsmart.org`, documentação de Unity/Godot/Snap/TikTok e repositórios técnicos de entidades reconhecidas. Cada ficha contém URL integral, aplicação, exercício e advertência.

**Limites:** a inclusão **não prova teste de HTTP em todos os links nem direitos de redistribuição de modelos externos**. Algumas referências de versões podem mudar. Todas continuam sujeitas à revisão de acesso, preço e licença por item antes de uso comercial.

## Coisas deliberadamente inalteradas

- Identificadores e conteúdo das primeiras 238 fichas.
- 149 verbetes do glossário original (trabalho separado na etapa 2).
- 106 perguntas FAQ, 19 laboratórios e 10 pipelines existentes.
- Todos os links de comunidade SIN e as regras ML-01 a ML-19.
- Código executável e instalações externas; o repositório é documental.

**Rollback:** reverter o merge de v0.4/etapa1 por Git sem apagar versões anteriores. Novos IDs não são reutilizados em migrações.
