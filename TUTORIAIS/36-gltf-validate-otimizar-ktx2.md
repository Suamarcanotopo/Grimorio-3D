# Tutorial 36 — glTF — validação e otimização KTX2 para web

**Nível:** Avançado · **Pipeline:** [D01](../DEPENDENCIAS/PIPELINES.md#d01)

## Objetivo e por que importa

O resultado de **Duas versões GLB validadas com relatório de bytes, textura e aparência** mostra como ligar uma técnica a um produto verificável, preservando desempenho, segurança e arquivos de origem.

**Antes de começar:** GLB de modelo próprio com textura PBR.

**Entregável verificável:** Duas versões GLB validadas com relatório de bytes, textura e aparência.

## Como fazer — passo a passo

1. **Etapa 1:** Congele uma cópia do GLB original e registre SHA-256.
2. **Etapa 2:** Inspecione atributos de geometria e materiais.
3. **Etapa 3:** Execute o validador glTF e corrija erros relevantes.
4. **Etapa 4:** Registre tamanho total e dimensão das texturas.
5. **Etapa 5:** Gere variante comprimida com ferramenta oficial ou bem documentada.
6. **Etapa 6:** Se compatível, teste texturas KTX2/BasisU no viewer escolhido.
7. **Etapa 7:** Compare aparência, memória e tempo de decodificação.
8. **Etapa 8:** Abra em navegador mobile e desktop, verificando fallback.
9. **Etapa 9:** Arquive original, versão comprimida, relatórios e direitos.

## Como saber se deu certo

- [ ] O projeto tem arquivo original editável e exportação/relatório.
- [ ] Resultados e limitações testados na plataforma específica, ou declarados como não testados.
- [ ] Conteúdo autoral, licenças e dados pessoais devidamente controlados.
- [ ] Uma pessoa iniciante consegue reproduzir os passos após estudar os pré-requisitos.
- [ ] O projeto tem evidência do antes/depois e rollback quando houve atualização.

## Armadilha a evitar

Compressão reduz bytes mas pode alterar detalhes e suporte; não sobreescrever a fonte.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://github.com/KhronosGroup/glTF-Validator

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Governança](../GOVERNANCA/MISSION-LOCK.md).

**Observação:** esta documentação não instala ferramentas nem homologa dispositivo ou publicação externa.

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se ajudar, deixe uma estrela no GitHub.
