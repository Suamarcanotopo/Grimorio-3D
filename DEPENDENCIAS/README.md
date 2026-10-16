# Matriz transversal de dependências 3D, AR, XR e plataformas sociais

**10 pipelines documentados.** Cada fluxo indica ferramentas, ordem, destino, itens obrigatórios, itens opcionais, links primários e status. [Arquivo legível por máquina](matriz.json).

## Como ler

1. **Origem:** projeto nativo que você controla e preserva.
2. **Via:** formatos, ferramentas e permissões exigidos ao longo do pipeline.
3. **Destino:** plataforma que realmente executará o produto.
4. **Gate:** cada dependência obrigatória deve ter prova no dispositivo certo.
5. **Não homologado:** documentação escrita não substitui teste ou aprovação do fornecedor.

| ID | Pipeline | Estado | Detalhes |
|---|---|---|---|
| D01 | Blender → produto 3D no website | documentado / integração não executada | [Abrir](PIPELINES.md#d01) |
| D02 | Blender → WebAR Android/iOS | documentado / testes de dispositivos pendentes | [Abrir](PIPELINES.md#d02) |
| D03 | Blender → Lens Studio → Snapchat | documentado / publicação não realizada | [Abrir](PIPELINES.md#d03) |
| D04 | Lens Studio → Snap Camera Kit → website | documentado / credenciais e termos precisam homologação | [Abrir](PIPELINES.md#d04) |
| D05 | Blender → TikTok Effect House | documentado / publicação não realizada | [Abrir](PIPELINES.md#d05) |
| D06 | Blender → Unreal → Meta Quest XR/MR | documentado / hardware e plugin não validados em execução | [Abrir](PIPELINES.md#d06) |
| D07 | Unreal → AR nativa Android/iOS | documentado / build não realizado | [Abrir](PIPELINES.md#d07) |
| D08 | Blender / criação de mundos → Meta Horizon | em evolução / não confundir com Meta Spark encerrado | [Abrir](PIPELINES.md#d08) |
| D09 | Web3D imersivo → Meta Quest browser | documentado / testes reais pendentes | [Abrir](PIPELINES.md#d09) |
| D10 | Blender → Unity / Unreal games | documentado / dependências dependem de versão | [Abrir](PIPELINES.md#d10) |

## Escolha rapidamente

- **Quero mostrar um produto 3D no site:** D01. Se o consumidor quiser ver na sala: D02.
- **Quero filtro AR no Snapchat:** D03. Se também quero filtro no meu site: D04 com Camera Kit Web.
- **Quero filtro AR para TikTok:** D05 (Effect House, não Lens Studio).
- **Quero uma experiência Meta Quest:** D06 ou D09. **Quero um mundo Horizon:** D08, conforme acesso.
- **Quero AR num app Unreal:** D07. **Quero um jogo tradicional:** D10.

## Aviso crítico: 'Snapshot', Snapchat e Meta Spark

**Snapshot** é termo genérico e pode referir-se a capturas de estado de um projeto; neste Grimório, o ecossistema de filtros citado pelo usuário é explicitado como **Snap / Snapchat / Lens Studio**. **Meta Spark (efeitos de terceiros)** está encerrado desde 14/01/2025 e é tratado somente como legado, jamais dependência ativa. **Meta Horizon Create/Studio** pertence a outro fluxo e disponibilidade por conta deve ser conferida.

## Contrato de segurança por integração

- Lista de SDKs, versões suportadas e licenças antes de desenvolver.
- Segredos e tokens fora do Git; token de cliente somente se recomendado pelo fornecedor, com restrição de escopo/origem.
- HTTPS + solicitações de permissão somente quando necessárias; encerrar câmera ao terminar a sessão.
- Direitos de uso verificados por modelo, som, textura e autoria da Lens.
- Alternativa funcional sem AR, baixo desempenho ou falta de compatibilidade.
- Sem dependências globais de código que sejam instaladas automaticamente por este repositório.

[Detalhes dos fluxos](PIPELINES.md) · [Portais oficiais](PORTAIS-OFICIAIS.md) · [Governança](../GOVERNANCA/MISSION-LOCK.md)
