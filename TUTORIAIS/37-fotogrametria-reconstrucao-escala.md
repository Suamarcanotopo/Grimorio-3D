# Tutorial 37 — Fotogrametria — reconstrução 3D com escala real

**Nível:** Intermediário · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

O resultado de **Objeto digitalizado com malha, textura, escala e relatório de reconstrução** mostra como ligar uma técnica a um produto verificável, preservando desempenho, segurança e arquivos de origem.

**Antes de começar:** Câmera, objeto próprio e software fotogramétrico autorizado.

**Entregável verificável:** Objeto digitalizado com malha, textura, escala e relatório de reconstrução.

## Como fazer — passo a passo

1. **Etapa 1:** Escolha objeto próprio com superfície não reflexiva.
2. **Etapa 2:** Coloque referência de escala mensurada ao lado.
3. **Etapa 3:** Capture fotos com sobreposição e iluminação constante.
4. **Etapa 4:** Carregue imagens no COLMAP ou ferramenta equivalente.
5. **Etapa 5:** Execute alinhamento e inspecione câmeras reconstruídas.
6. **Etapa 6:** Gere nuvem e malha por fluxo disponível.
7. **Etapa 7:** Remova artefatos de fundo e ajuste orientação.
8. **Etapa 8:** Faça UV, textura e reduza densidade conforme destino.
9. **Etapa 9:** Compare dimensão com régua real e documente o erro.

## Como saber se deu certo

- [ ] O projeto tem arquivo original editável e exportação/relatório.
- [ ] Resultados e limitações testados na plataforma específica, ou declarados como não testados.
- [ ] Conteúdo autoral, licenças e dados pessoais devidamente controlados.
- [ ] Uma pessoa iniciante consegue reproduzir os passos após estudar os pré-requisitos.
- [ ] O projeto tem evidência do antes/depois e rollback quando houve atualização.

## Armadilha a evitar

Imagens e modelos de pessoas/objetos podem exigir direitos; resultados não são medição metrológica certificada.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://colmap.github.io/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Governança](../GOVERNANCA/MISSION-LOCK.md).

**Observação:** esta documentação não instala ferramentas nem homologa dispositivo ou publicação externa.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se ajudar, deixe uma estrela no GitHub.
