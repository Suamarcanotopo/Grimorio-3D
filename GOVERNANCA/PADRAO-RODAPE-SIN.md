# Padrão do rodapé e navegação SIN — Grimório 3D

O objetivo é **ajudar o leitor primeiro, convidar para a comunidade depois**, mantendo a documentação leve, com o CTA final no README e no índice principal.

## O que todo índice deve ter

1. Índice didático por intenção — "quero fazer" → módulo → ferramenta → fonte.
2. Links relativos para Glossário, FAQ, Trilhas, Tutoriais, Dependências e Governança.
3. Cada URL externa do catálogo canônico visível no bloco gerado do README, com descrição e acesso.
4. Aviso legal: acesso gratuito ou freemium não constitui licença comercial de assets.
5. Rodapé com convite a deixar estrela e links do SIN; nenhuma seção técnica depois dele.

## Links canônicos a preservar

- **Sistema Imersivo Narrativo:** <https://sistemaimersivonarrativo.com.br/>
- **Skills SIN no GitHub:** <https://github.com/Suamarcanotopo/grimorio-skills>
- **Instagram — Sua Marca no Topo:** <https://www.instagram.com/suamarcanotopo/>
- **YouTube — Coworking Lab:** <https://www.youtube.com/@suamarcanotopo?sub_confirmation=1>
- **Grupo gratuito — Dicas e Tutoriais:** <https://chat.whatsapp.com/F11omHqfI4KKCC0Sgbc4Vm?s=cl&p=i&mlu=4&ilr=4>
- **Grupo gratuito — Working Lab:** <https://chat.whatsapp.com/FcyMOdQqyW8Ci104P8i3Gg?s=cl&p=i&mlu=4&ilr=4>
- **Comunidade Grimório 3D:** <https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5>

## Regras de contribuição e automação

- Não embutir scripts ou instaladores de plataformas externas no README.
- Não reescrever à mão o bloco gerado de URLs: editar os dados JSON e executar `python3 scripts/gerar-indice-readme.py --write`.
- Evitar duplicar o catálogo integral em dezenas de páginas: use link ao índice do README.
- Nos novos tutoriais, escrever a referência técnica perto do passo e deixar promoção comunitária em rodapé proporcional.
- Se algum link de convite mudar, atualizar README, INDEX, política e as asserções do CI na mesma alteração; manter histórico via PR.
- A validade de convites WhatsApp e o acesso a páginas externas podem mudar, mesmo quando o arquivo do GitHub estiver correto.
