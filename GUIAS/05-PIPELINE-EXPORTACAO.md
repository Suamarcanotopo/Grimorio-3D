# Pipeline profissional — arquivo nativo, intercâmbio e entrega

## Matriz de formatos

| Formato | Função principal | Atenção |
|---|---|---|
| BLEND | Projeto editável Blender | Não é entrega universal de runtime |
| FBX | Intercâmbio de mesh, rig e animação | Orientação, escala, bones e materiais variam |
| OBJ + MTL | Geometria e materiais simples | Não suporta rigging complexo como FBX |
| glTF / GLB | Entrega interoperável e eficiente | Nem todo nó/material autoral converte |
| USD / USDZ | Descrição/composição de cenas e AR | Converter usando pipeline testado |
| Alembic / ABC | Cache de geometria animada | Pesado; não é substituto de rig editável |
| VDB | Volumes como fumaça e campos | Suporte depende do renderizador |
| STL | Malha triangulada para fabricação | Não guarda materiais/semântica CAD |
| STEP | Geometria CAD interoperável | Conversão para runtime requer triangulação |
| IFC | Interoperabilidade BIM | Dados semânticos e propriedades precisam validação |
| KTX2 | Distribuição de texturas comprimidas | Teste transcodificação e qualidade no destino |

## Manifesto mínimo de entrega

```text
projeto/
├── origem/       # nativos editáveis, controlados por versão
├── intercambio/  # FBX/USD/ABC/STEP quando aplicável
├── runtime/      # GLB, animações, texturas compactadas
├── evidencias/   # previews, logs, métricas, licenças
└── manifesto.json
```

## Contrato de asset — exemplo

```json
{
  "id": "asset-exemplo-001",
  "titulo": "Modelo próprio de demonstração",
  "autor": "equipe",
  "origem_url": null,
  "licenca": "a confirmar",
  "direitos_comerciais_verificados": false,
  "arquivo_nativo": "origem/exemplo.blend",
  "arquivo_entrega": "runtime/exemplo.glb",
  "unidades": "metros",
  "destino": ["web"],
  "versao_pipeline": "v1",
  "sha256": "registrar no momento da entrega"
}
```

## Gates sem atalho

**G0 Fonte → G1 Direitos → G2 Segurança → G3 Integridade do arquivo → G4 Fidelidade visual → G5 Desempenho real → G6 Acessibilidade/privacidade → G7 Evidências → G8 Aprovação.** Um gate não comprovado permanece pendente, não aprovado.

**Referências:** [glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html), [OpenUSD](https://openusd.org/), [KTX2](https://registry.khronos.org/KTX/specs/2.0/ktxspec.v2.html), [SPDX](https://spdx.dev/specifications/).

[Índice geral](../INDEX.md)
