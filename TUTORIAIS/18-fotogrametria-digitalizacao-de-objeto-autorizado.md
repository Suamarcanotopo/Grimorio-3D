# Tutorial 18 — Fotogrametria: digitalização de objeto autorizado

**Nível:** Avançado · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Aprender a executar o fluxo **Fotogrametria: digitalização de objeto autorizado**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Objeto próprio, câmera e ferramenta fotogramétrica.

**Entregável verificável:** Nuvem de pontos, malha limpa e evidência de escala.

## Como fazer — passo a passo

1. **Etapa 1:** Escolher objeto que não exponha propriedade ou pessoas sem autorização.
2. **Etapa 2:** Montar iluminação difusa e fundo com referências suficientes.
3. **Etapa 3:** Capturar imagens cobrindo o objeto com sobreposição consistente.
4. **Etapa 4:** Importar imagens em COLMAP ou ferramenta equivalente.
5. **Etapa 5:** Executar alinhamento e revisar poses de câmera.
6. **Etapa 6:** Gerar reconstrução e remover ruído de fundo.
7. **Etapa 7:** Definir escala com referência mensurada.
8. **Etapa 8:** Executar retopologia se destinado a games ou web.
9. **Etapa 9:** Preparar UV e material e exportar em formato interoperável.
10. **Etapa 10:** Arquivar fotos originais conforme política de privacidade e licença.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Texturas reflexivas e superfícies lisas podem degradar reconstrução.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://colmap.github.io/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
