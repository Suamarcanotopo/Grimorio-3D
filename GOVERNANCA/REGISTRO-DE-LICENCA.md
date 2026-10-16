# Registro de proveniência e licença por asset

Este template é destinado a **cada asset usado num produto**, e não a cada plataforma listada.

```json
{
  "asset_id": "projeto-asset-001",
  "fonte": "https://dominio-oficial.exemplo/item",
  "autor_publicador": "identificacao",
  "data_download": "AAAA-MM-DD",
  "licenca_url": "https://dominio-oficial.exemplo/licenca",
  "licenca_tipo": "identificador ou nome concreto",
  "licenca_versao": "versao, se houver",
  "permissao_uso_comercial": "comprovado | restrito | desconhecido",
  "permissao_redistribuicao_isolada": "comprovado | proibido | desconhecido",
  "permissao_edicao": "comprovado | proibido | desconhecido",
  "atribuicao_necessaria": "sim | nao | desconhecido",
  "evidencia_guardada": ["arquivo de termos", "captura datada", "comprovante"],
  "sha256_download": "checksum real",
  "decisao_revisor": "liberado | bloqueado | pendente",
  "motivo": "explicacao"
}
```

## Regras
- Licença **MIT** do repositório não vale para assets externos.
- Grátis ≠ freemium ≠ domínio público ≠ uso comercial liberado.
- **CC0** e **CC BY** têm obrigações distintas; há direitos de pessoas, marcas e patentes independentes.
- **CC BY-NC** não autoriza uso comercial.
- CC BY-SA e outras condições podem gerar deveres no uso derivado e redistribuição.
- Licenças de modelos IA e datasets podem divergir da licença do serviço que os gerou.
- Diante de conflito, **bloquear uso comercial** até confirmação.

**Fonte:** https://creativecommons.org/licenses/ e https://spdx.org/licenses/
