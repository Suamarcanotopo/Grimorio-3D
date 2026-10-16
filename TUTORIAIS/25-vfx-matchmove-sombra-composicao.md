# Tutorial 25 — VFX — matchmove, sombra e composição

**Nível:** Avançado · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Produzir **Plano de 5 s com modelo 3D encaixado e sombras testadas** ajuda a aplicar fundamentos 3D a um problema real, distinguir preview de runtime e documentar qualidade e direitos.

**Antes de começar:** Vídeo gravado por você com permissão, Blender Movie Clip Editor.

**Entregável verificável:** Plano de 5 s com modelo 3D encaixado e sombras testadas.

## Como fazer — passo a passo

1. **Etapa 1:** Grave tomada curta de ambiente bem iluminado e com parallax.
2. **Etapa 2:** Registre lente, FPS e escala de objeto conhecido.
3. **Etapa 3:** Escolha pontos estáveis e execute tracking.
4. **Etapa 4:** Remova trackers com muito erro e faça Camera Solve.
5. **Etapa 5:** Defina plano de chão e alinhamento dos eixos.
6. **Etapa 6:** Adicione modelo simples na posição correta.
7. **Etapa 7:** Configure luz, sombra de contato e render pass para composição.
8. **Etapa 8:** Exporte vídeo e revise se o objeto desliza frame a frame.
9. **Etapa 9:** Guarde source clip autorizado, projeto e estatísticas de solve.

## Como saber se deu certo

- [ ] Cada etapa executada em arquivo autoral ou licenciado.
- [ ] Projeto de origem editável e exportação final preservados.
- [ ] Resultado e falhas registrados com captura e contexto da versão.
- [ ] Teste no destino realizado, ou status marcado como **não testado**.
- [ ] Direitos, compatibilidade, performance e acessibilidade revisados conforme projeto.

## Armadilha a evitar

Sem parallax ou referência de escala, o solve pode falhar.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://docs.blender.org/manual/en/latest/movie_clip/tracking/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Dependências](../DEPENDENCIAS/README.md).

**Nota:** este tutorial documental não comprova execução de software ou aprovação comercial por si só.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Contribua com uma estrela no GitHub.
