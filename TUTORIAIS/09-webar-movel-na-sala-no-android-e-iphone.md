# Tutorial 09 — WebAR: móvel na sala no Android e iPhone

**Nível:** Intermediário · **Pipeline:** [D02](../DEPENDENCIAS/PIPELINES.md#d02)

## Objetivo e por que importa

Aprender a executar o fluxo **WebAR: móvel na sala no Android e iPhone**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Modelo com escala física e site HTTPS.

**Entregável verificável:** Botão visualizar em sua sala com alternativa para aparelho não suportado.

## Como fazer — passo a passo

1. **Etapa 1:** Definir dimensões reais e conferir unidade em metros.
2. **Etapa 2:** Exportar GLB e validá-lo em visualizador de terceiros.
3. **Etapa 3:** Preparar USDZ verificado ou conversão model-viewer para fluxo iOS suportado.
4. **Etapa 4:** Configurar model-viewer ar com modos suportados e fallback.
5. **Etapa 5:** Abrir site em Android ARCore e inspecionar Scene Viewer.
6. **Etapa 6:** Abrir em iPhone compatível e conferir Quick Look.
7. **Etapa 7:** Testar posicionamento em chão, escala e iluminação.
8. **Etapa 8:** Explicar acesso à câmera e não coletar imagens sem necessidade.
9. **Etapa 9:** Registrar aparelhos testados e oferecer prévia 2D a outros.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

AR não pode ser prometida como universal.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://developers.google.com/ar/develop/scene-viewer?hl=pt-BR

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
