# AGENTS.md — contrato de agentes e revisores Grimório 3D

> Instruções de contribuição **documental**, não execução automática de skills ou garantia de revisão real.

## Missão
Servir como livro técnico vivo de 3D, em português do Brasil, com fontes verificáveis, exemplos autorais e dados reproduzíveis.

## Papéis inspirados no SIN
- **OWNER de arquitetura:** protege categorias, schemas e compatibilidade.
- **OWNER de produção 3D:** verifica workflows de modelagem, UV, texturing, rig, animação, render e tracking.
- **OWNER de Web3D:** revisa engine/GLB, acessibilidade, performance, SEO e fallback.
- **OWNER de licenciamento e segurança:** atua em links, licenças, plugins, captura de pessoas e integração segura.
- **REVIEWER Red Team:** procura URLs enganosas, conteúdo inventado, licença comercial presumida, categorias erradas e exemplos inseguros.
- **CONTRIBUTOR:** propõe ficha em PT-BR e fornece evidências; não autodeclara homologação.

## Autoridade e limites
1. Ler `GOVERNANCA/MISSION-LOCK.md` antes de editar.
2. Não reescrever `LICENSE` ou remover dados anteriores sem justificativa documentada e revisão.
3. Nunca aplicar a licença MIT deste repositório a assets de terceiros.
4. Não afirmar execução de um conselho ou skill por apenas escrever seu nome.
5. Nunca inserir credenciais, imagens privadas, rostos identificáveis ou material sem autorização.
6. Se impossível verificar fonte ou licença, marcar como pendente; falhar fechado para redistribuição comercial.
7. Produzir mudanças pequenas, auditar diff e manter branch + PR.
8. Sempre rodar `python3 scripts/validar.py`; teste de integração 3D real é separado.
9. Não usar `curl | bash`, exec de scripts externos ou download automático como parte do catálogo.

## Anti-regressão
Não perder campos de catálogo, IDs, conteúdo didático, links, histórico, fontes ou controles de segurança. Um arquivo presente não prova sistema implantado; verifique CI e revisão humana.
