# cinema pipeline aberto — Grimório 3D

**10 referências oficiais ou institucionais.** Este nicho reúne fontes para pesquisar e praticar, não assets redistribuíveis por padrão.

[Voltar ao catálogo](../../INDEX.md) · [Glossário](../../GLOSSARIO/README.md) · [FAQ](../../FAQ/README.md)

## Academy Software Foundation

- **O que é:** Fundação de projetos abertos adotados por estúdios de animação e efeitos visuais.
- **URL completa:** https://www.aswf.io/
- **Para que serve:** Aprender padrões de produção e integração entre aplicativos.
- **Como começar:** Explore projetos por finalidade e adote apenas padrões necessários.
- **Truque e alerta:** Priorize padrões de arquivo e cor antes de automatizar pipelines.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenColorIO

- **O que é:** Padrão e biblioteca de gerenciamento de cor para cinema, animação e VFX.
- **URL completa:** https://opencolorio.org/
- **Para que serve:** Controlar conversões entre espaços de cor durante edição e composição.
- **Como começar:** Leia a documentação e crie projeto com configuração de cor explícita.
- **Truque e alerta:** Sem controle de espaço de cor o mesmo render pode parecer diferente em softwares distintos.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenEXR

- **O que é:** Formato profissional de imagem HDR e múltiplos canais para render e composição.
- **URL completa:** https://www.openexr.com/
- **Para que serve:** Entregar passes de render e imagens de alta faixa dinâmica.
- **Como começar:** Exporte um passe de render EXR e abra em compositor compatível.
- **Truque e alerta:** Não substitua EXR linear por PNG 8-bit quando precisar recuperar informação HDR.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenVDB

- **O que é:** Estrutura aberta para dados volumétricos esparsos como nuvens, fogo e fumaça.
- **URL completa:** https://www.openvdb.org/
- **Para que serve:** Transportar volumes de efeitos entre ferramentas.
- **Como começar:** Gere volume pequeno autorizado e compare importação no renderizador.
- **Truque e alerta:** Volumes pesados precisam medição de memória e compatibilidade por versão.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## MaterialX

- **O que é:** Padrão aberto para redes de materiais e intercâmbio de aparência.
- **URL completa:** https://materialx.org/
- **Para que serve:** Melhorar portabilidade de lookdev entre softwares.
- **Como começar:** Comece por material simples e teste import/export com versões fixas.
- **Truque e alerta:** Não assuma paridade de render sem comparar parâmetros suportados.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenTimelineIO

- **O que é:** Formato e API abertos para intercâmbio de estrutura de edição em linhas do tempo.
- **URL completa:** https://github.com/AcademySoftwareFoundation/OpenTimelineIO
- **Para que serve:** Conectar montagem, aprovação de plano e pós-produção.
- **Como começar:** Estude exemplos oficiais de timelines e confirme codecs/retiming no destino.
- **Truque e alerta:** Não carrega necessariamente mídia nem resolve todos os efeitos de edição.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenAssetIO

- **O que é:** API aberta para referenciar e gerenciar ativos de produção.
- **URL completa:** https://github.com/OpenAssetIO/OpenAssetIO
- **Para que serve:** Integrar asset management sem amarrar tudo a caminhos locais.
- **Como começar:** Explore o contrato de referência e teste com assets de exemplo próprios.
- **Truque e alerta:** API de gestão não transfere direitos sobre os assets vinculados.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenCue

- **O que é:** Sistema aberto de gerenciamento de tarefas de render em fazendas.
- **URL completa:** https://opencue.io/
- **Para que serve:** Planejar renderização distribuída de cenas extensas.
- **Como começar:** Leia arquitetura e execute apenas em ambiente isolado de teste.
- **Truque e alerta:** Fazenda exige orçamento de recursos, acesso e segurança.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## OpenImageIO

- **O que é:** Biblioteca profissional para leitura, escrita e processamento de imagens de produção.
- **URL completa:** https://openimageio.readthedocs.io/
- **Para que serve:** Automatizar inspeção de texturas, formatos e canais.
- **Como começar:** Estude ferramentas de linha de comando e valide uma imagem própria.
- **Truque e alerta:** Conversões de bit depth e espaço de cor podem perder informação.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão

## ACES Central

- **O que é:** Comunidade técnica e documentação associada ao Academy Color Encoding System.
- **URL completa:** https://acescentral.com/
- **Para que serve:** Estudar workflow de cores de aquisição até entrega.
- **Como começar:** Compare cenas com e sem fluxo de cor padronizado.
- **Truque e alerta:** Separar configuração de exibição do dado de imagem.
- **Acesso:** Documentação/portal público; serviços e eventos podem ser pagos
- **Freemium:** Conferir conforme produto ou plano
- **Uso comercial:** Não homologado para reutilização de assets; conteúdo referencial
- **Evidência:** Fonte primária/organização identificada em 2026-10-16; uso e disponibilidade sujeitos à revisão
