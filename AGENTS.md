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


## Missão educacional transversal — ECP + Coliseu + Owners

- OWNER de pedagogia: exige explicação para leigos, uma tarefa prática e indicação da fonte oficial por conceito ou tutorial.
- OWNER Blender: revisa geometria, UV, shader, rig, animação, bake, tracking e exportação.
- OWNER Unreal/Meta: revisa SDK Meta XR, VR/MR, templates, integração e métricas no headset.
- OWNER AR social: separa Lens Studio/Camera Kit, TikTok Effect House e legado Meta Spark.
- OWNER Web3D: valida HTML, glTF, WebXR, Scene Viewer, Quick Look, CSP, autorização de câmera e fallback.
- REVIEWER Red Team: detecta premissas irreais de portabilidade, formatos, orçamento, direitos, políticas e versões.

Papéis são responsabilidades metodológicas, não agentes autônomos comprovadamente executados. A entrega deve incluir evidência de revisão real para declarar aprovação humana.

## Regras dos módulos novos

1. Sem apagar glossário ou FAQs anteriores em uma atualização corretiva; revisão precisa de diff e justificativa.
2. FAQ começa com uma pergunta de usuário e termina com procedimento verificável, URL primária e limite explícito.
3. Tutorial precisa: nível, pré-requisitos, objetivo, passos executáveis, entregável, checklist e erro comum.
4. A matriz de dependências deve declarar requisitos, opcionais, destino, fonte e status; não presumir que GLB se publica diretamente como Lens.
5. Rode `python3 scripts/validar.py` + `python3 scripts/validar-academia.py`.
6. Em projetos Meta/Snap/TikTok, documentação atual substitui tutoriais antigos de marketing; registre mudanças de produtos encerrados.
