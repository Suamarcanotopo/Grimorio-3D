# Política de fontes seguras — qualidade maior que volume

## Três camadas, responsabilidades distintas

1. **CORE ATEMPORAL:** geometria, topologia, UV, PBR, ritmo, luz, física, direito autoral, acessibilidade, documentação de projetos e testes. Mudança somente por revisão de método.
2. **FONTE OFICIAL VIVA:** documentação de Blender, Unreal, Khronos, ASWF, Meta, Snap, TikTok, W3C. Atualizável por evidência de fornecedor e versão.
3. **RADAR/EDITORIAL:** conferências, artigos, papers recentes, vídeos técnicos, cases, portais setoriais; **não** impor como regra antes de teste.

## Ficha mínima de uma fonte

| Campo | Obrigatório | Exemplo |
|---|---|---|
| título e descrição PT-BR | Sim | Tutorial de ICVFX — guia de camera tracking em tempo real |
| URL HTTPS integral | Sim | Site oficial |
| país/idioma e instituição | Sim quando conhecido | EUA, inglês, Epic |
| classe de evidência | Sim | DOCUMENTAÇÃO_FORNECEDOR |
| data de publicação e consulta | Sim quando disponível | Publicado em data X; consultado em data Y |
| tipo de licença do conteúdo | Sim para reutilização | Não homologada até leitura dos termos |
| status de verificação | Sim | FONTE_IDENTIFICADA vs TESTADA vs HOMOLOGADA |
| caso de uso e pré-requisito | Sim | Filme, Unreal compatível, LED volume |
| truque e risco | Sim | Requer teste físico; preview não prova desempenho |
| link do exercício | Preferível | Documento em NICHOS/CURRICULO |

## Priorização oficial

1. **Normas, especificações e órgão responsável.**
2. **Documentação técnica primária do editor/SDK**, versão vigente.
3. **Fundação acadêmica ou instituição industrial reconhecida**, com evidências.
4. **Artigo revisado ou experimento replicável.**
5. **Portal altamente relevante ou case de estúdio**, contextualizado.
6. Hype sem prova: somente no radar, fora dos tutoriais obrigatórios.

## Regras de segurança

- Não importar binários, projetos ou texturas protegidas junto de links de referência.
- Não executar instaladores e scripts sugeridos por páginas externas.
- Não permitir upload direto sem quarentena, tamanho máximo, antivírus aplicável e validação do formato.
- Não converter licença MIT do Grimório em licença de imagens ou personagens de terceiros.
- Não armazenar dados pessoais de pessoas filmadas para mocap ou AR sem legitimidade e minimização.
- Não usar textos editoriais como instruções de autopublicação de SDK.
- Não marcar recursos descontinuados como ativos. Ex.: Meta Spark de terceiros.
- Não assumir ranking de nações sem conjunto de dados e metodologia comparável.

## Governança do refresh

**Fonte crítica alterada:** abra Issue/PR, registre URL antiga/nova, delta, consequência, testes de regressão e decisão. Versões antigas continuam rastreáveis pelo Git. Status permitidos: `CURRENT`, `STALE`, `DELTA_FOUND`, `NEEDS_TEST`, `BLOCKED`, `DEPRECATED`.

**Interlock:** documentação de ECP e Coliseu não significa que agentes estejam executando em segundo plano. O conselho funciona como checklist de responsabilidades até existir execução registrada.
