# Tutorial 22 — Cinema — passes EXR e consistência de cor

**Nível:** Avançado · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Produzir **Conjunto EXR com dois passes, PNG final e registro de color management** ajuda a aplicar fundamentos 3D a um problema real, distinguir preview de runtime e documentar qualidade e direitos.

**Antes de começar:** Cena renderizável em Blender e compositor de imagens.

**Entregável verificável:** Conjunto EXR com dois passes, PNG final e registro de color management.

## Como fazer — passo a passo

1. **Etapa 1:** Escolha cena pequena e fixe unidades e câmera.
2. **Etapa 2:** Configure gestão de cor na origem e registre versão.
3. **Etapa 3:** Separe ao menos duas Render Passes relevantes.
4. **Etapa 4:** Renderize EXR preservando informação de alta faixa dinâmica.
5. **Etapa 5:** Abra EXR em compositor suportado e confira canais.
6. **Etapa 6:** Componha sombra ou máscara com correções reversíveis.
7. **Etapa 7:** Renderize PNG e compare com preview em monitor calibrado quando possível.
8. **Etapa 8:** Documente transformação de cor e artefatos observados.
9. **Etapa 9:** Salve projeto nativo, EXR e relatório antes/depois.

## Como saber se deu certo

- [ ] Cada etapa executada em arquivo autoral ou licenciado.
- [ ] Projeto de origem editável e exportação final preservados.
- [ ] Resultado e falhas registrados com captura e contexto da versão.
- [ ] Teste no destino realizado, ou status marcado como **não testado**.
- [ ] Direitos, compatibilidade, performance e acessibilidade revisados conforme projeto.

## Armadilha a evitar

PNG final não substitui EXR para todas as etapas de composição.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://www.openexr.com/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Dependências](../DEPENDENCIAS/README.md).

**Nota:** este tutorial documental não comprova execução de software ou aprovação comercial por si só.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Contribua com uma estrela no GitHub.
