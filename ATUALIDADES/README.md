# Radar de atualidades 3D — informação volátil separada do núcleo técnico

**Atemporal não significa congelado.** Geometria, luz, UV, continuidade de cena e licenciamento pertencem ao conhecimento durável. **Versões, preços, termos comerciais, SDKs, novos recursos, políticas de publicação e hype** mudam e ficam neste radar, com data.

## Como funciona

1. Selecionar assunto e fonte primária: software, norma, plataforma, estudo ou setor.
2. Registrar **data do acontecimento** e **data da publicação**: não usar apenas data de indexação.
3. Separar **documentação oficial**, **estudo empírico**, **caso de uso**, **editorial especializado** e **rumor não verificado**.
4. Avaliar cinco perguntas: o que mudou? quem pode usar? preço/limitação? prova? aplicação didática?
5. Construir **um pequeno teste**, sem migrar projetos de produção imediatamente.
6. Se relevante, atualizar tutorial/adapter de plataforma por PR; nunca reescrever o Mission Lock sem decisão explícita.
7. Manter fotografia da informação anterior e identificar recurso extinto ou substituído.

**Não existe atualização automática ativa neste repositório.** Um arquivo de radar datado não comprova monitoramento recorrente.

## Grau de confiança para registrar

| Classe | Significado | Uso correto |
|---|---|---|
| PADRÃO_NORMATIVO | Especificação publicada por entidade responsável | Base estável, revisar versões |
| DOCUMENTAÇÃO_FORNECEDOR | Conteúdo técnico oficial da ferramenta | Guia de integração, exige teste por versão |
| PESQUISA_REVISADA | Artigo técnico com método e limitações | Experimentação antes de uso comercial |
| EVIDÊNCIA_DE_PRODUÇÃO | Resultado observado em projeto concreto | Válido no hardware e parâmetros registrados |
| PORTAL_SETORIAL | Organizações e editoriais especialistas | Panorama de mercado, não prova técnica |
| HYPE_A_VERIFICAR | Tendência/alegação sem execução comprovada | Não implementar automaticamente |

## Painel vivo — por assunto

- [Fotografia técnica de 16/10/2026](BOLETIM-2026-10-16.md)
- [Como cadastrar fontes seguras e lidar com hype](../GOVERNANCA/FONTES-ATEMPORAIS-E-ATUAIS.md)
- [Portais e padrões internacionais](../ECOSSISTEMA/README.md)
- [Matriz de dependências por projeto](../DEPENDENCIAS/README.md)

**Para automação futura:** um job agendado poderá verificar releases ou notícias de fornecedores. Não adicionar cron fictício: quando criado, declarar sistema real, frequência, logs, fontes, quotas e condições de alerta.
