# Tutorial 06 — Tracking: integrar objeto 3D em filmagem

**Nível:** Intermediário · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Aprender a executar o fluxo **Tracking: integrar objeto 3D em filmagem**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Vídeo próprio com câmera em movimento e Blender.

**Entregável verificável:** Cena composta onde objeto virtual parece estacionário no vídeo.

## Como fazer — passo a passo

1. **Etapa 1:** Gravar 5 a 10 segundos com movimento lateral e referências estáveis.
2. **Etapa 2:** Importar vídeo no Movie Clip Editor.
3. **Etapa 3:** Escolher pontos com contraste e parallax, evitando pessoas privadas.
4. **Etapa 4:** Rastrear pontos e executar camera solve.
5. **Etapa 5:** Revisar erro residual e remover trilhas erradas.
6. **Etapa 6:** Calibrar chão, eixos, escala e posicionamento de câmera.
7. **Etapa 7:** Adicionar cubo e ajustar perspectiva/luz à tomada.
8. **Etapa 8:** Compor objeto no vídeo e observar oclusão e sombras.
9. **Etapa 9:** Exportar vídeo e salvar parâmetros do solve.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Planar tracking não é sempre uma reconstrução completa de câmera 3D.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://docs.blender.org/manual/en/latest/movie_clip/tracking/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
