# Tutorial 26 — Unreal — primeiro efeito Niagara otimizado

**Nível:** Avançado · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Produzir **Efeito de partículas com perfis antes/depois na engine** ajuda a aplicar fundamentos 3D a um problema real, distinguir preview de runtime e documentar qualidade e direitos.

**Antes de começar:** Unreal Engine instalado e projeto de teste.

**Entregável verificável:** Efeito de partículas com perfis antes/depois na engine.

## Como fazer — passo a passo

1. **Etapa 1:** Crie um projeto de demonstração Unreal com versão registrada.
2. **Etapa 2:** Abra sistema Niagara e identifique emitter e system.
3. **Etapa 3:** Escolha efeito simples como poeira de chão.
4. **Etapa 4:** Configure taxa de emissão e duração limitada.
5. **Etapa 5:** Ajuste material de partícula com transparência mínima.
6. **Etapa 6:** Crie controle Blueprint para ligar e desligar efeito.
7. **Etapa 7:** Meça baseline CPU/GPU com efeito desativado.
8. **Etapa 8:** Ative Niagara e compare frame time no alvo de teste.
9. **Etapa 9:** Reduza overdraw e registre antes/depois.

## Como saber se deu certo

- [ ] Cada etapa executada em arquivo autoral ou licenciado.
- [ ] Projeto de origem editável e exportação final preservados.
- [ ] Resultado e falhas registrados com captura e contexto da versão.
- [ ] Teste no destino realizado, ou status marcado como **não testado**.
- [ ] Direitos, compatibilidade, performance e acessibilidade revisados conforme projeto.

## Armadilha a evitar

Niagara pode ter custo alto em GPU móvel; não confundir preview com build.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Dependências](../DEPENDENCIAS/README.md).

**Nota:** este tutorial documental não comprova execução de software ou aprovação comercial por si só.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Contribua com uma estrela no GitHub.
