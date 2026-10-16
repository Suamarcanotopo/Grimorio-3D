# Tutorial 04 — Game prop: malha leve e LOD

**Nível:** Intermediário · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Aprender a executar o fluxo **Game prop: malha leve e LOD**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Projeto 01, Blender e uma engine de teste.

**Entregável verificável:** Prop optimizado com versões de detalhe e collider.

## Como fazer — passo a passo

1. **Etapa 1:** Definir a distância que o jogador verá o objeto e dispositivo alvo.
2. **Etapa 2:** Fazer silhueta principal com menos faces, evitando superfícies invisíveis.
3. **Etapa 3:** Revisar e corrigir normais, triangulação e UV.
4. **Etapa 4:** Criar variantes de qualidade conforme distância e tela.
5. **Etapa 5:** Preparar texturas em resolução proporcional ao tamanho na tela.
6. **Etapa 6:** Nomear meshes, collider e pivot de acordo com convenção do jogo.
7. **Etapa 7:** Exportar FBX/glTF conforme motor, com escala validada.
8. **Etapa 8:** Importar no Unreal/Unity, configurar colisão e LOD conforme suporte.
9. **Etapa 9:** Medir draw calls, tempo de quadro e qualidade visual.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Quantidade de triângulos isolada não identifica todo gargalo.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
