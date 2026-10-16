# Tutorial 14 — Unreal: nível jogável a partir de cenário Blender

**Nível:** Avançado · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Aprender a executar o fluxo **Unreal: nível jogável a partir de cenário Blender**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Motor instalado, projeto Unreal, Blender.

**Entregável verificável:** Demo de movimentação e colisão em cena autoral.

## Como fazer — passo a passo

1. **Etapa 1:** Começar com template apropriado da Unreal.
2. **Etapa 2:** Criar blockout de nível no Blender com escala mensurável.
3. **Etapa 3:** Preparar materiais e pivôs, exportar FBX/glTF conforme engine.
4. **Etapa 4:** Importar Static Mesh e organizar Content Browser.
5. **Etapa 5:** Adicionar colisão simples a chão, paredes e objetos.
6. **Etapa 6:** Configurar personagem e câmera do template.
7. **Etapa 7:** Aplicar iluminação e materiais adequados ao device alvo.
8. **Etapa 8:** Executar Play In Editor e verificar rotas e colisões.
9. **Etapa 9:** Analisar profiler e refazer estruturas que custam muito.
10. **Etapa 10:** Empacotar demo e registrar versão e requisitos.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Preview no editor não demonstra desempenho de build de produção.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://dev.epicgames.com/documentation/en-us/unreal-engine

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
