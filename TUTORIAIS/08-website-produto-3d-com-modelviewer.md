# Tutorial 08 — Website: produto 3D com model-viewer

**Nível:** Intermediário · **Pipeline:** [D01](../DEPENDENCIAS/PIPELINES.md#d01)

## Objetivo e por que importa

Aprender a executar o fluxo **Website: produto 3D com model-viewer**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** GLB próprio e hospedagem HTTPS.

**Entregável verificável:** Página 3D responsiva com CTA acessível e fallback.

## Como fazer — passo a passo

1. **Etapa 1:** Preparar GLB com textura e câmera central, validado no viewer externo.
2. **Etapa 2:** Criar HTML com texto claro e poster de fallback de direitos próprios.
3. **Etapa 3:** Adicionar model-viewer de versão fixa compatível com projeto.
4. **Etapa 4:** Apontar src ao arquivo GLB via HTTPS e reservar altura.
5. **Etapa 5:** Ativar camera-controls, ar apenas quando necessário e descrição alt.
6. **Etapa 6:** Adicionar CTA HTML utilizável mesmo se o canvas falhar.
7. **Etapa 7:** Testar keyboard-only, erro de download, reduced motion e smartphone.
8. **Etapa 8:** Analisar LCP/INP e transferências, reduzir textura se necessário.
9. **Etapa 9:** Guardar HTML, GLB, resultados do teste e licenças.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Não implemente hero 3D que bloqueie leitura e conversão.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://modelviewer.dev/docs/index.html

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
