# Tutorial 10 — Web3D avançado: cena Three.js sem React

**Nível:** Intermediário · **Pipeline:** [D01](../DEPENDENCIAS/PIPELINES.md#d01)

## Objetivo e por que importa

Aprender a executar o fluxo **Web3D avançado: cena Three.js sem React**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Conhecimento básico de HTML e JavaScript.

**Entregável verificável:** Objeto 3D controlado com teclado e fallback estático.

## Como fazer — passo a passo

1. **Etapa 1:** Criar página HTML sem frameworks com contêiner de tamanho fixo.
2. **Etapa 2:** Adicionar import JavaScript Three.js na versão escolhida e documentada.
3. **Etapa 3:** Instanciar Scene, PerspectiveCamera e WebGLRenderer.
4. **Etapa 4:** Criar mesh básico e iluminação, mantendo texto/CTA fora de canvas.
5. **Etapa 5:** Adicionar controles de movimento apenas por interação explícita.
6. **Etapa 6:** Parar loop quando aba não estiver visível ou não houver animação.
7. **Etapa 7:** Detectar ausência de WebGL e mostrar imagem/texto de fallback.
8. **Etapa 8:** Medir performance em browser mobile e reduzida capacidade.
9. **Etapa 9:** Fixar versão do pacote e registrar compatibilidade.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Não usar render loop infinito para cena totalmente estática.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://threejs.org/docs/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
