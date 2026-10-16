# Tutorial 05 — Personagem: rig, pesos e animação curta

**Nível:** Intermediário · **Pipeline:** [D10](../DEPENDENCIAS/PIPELINES.md#d10)

## Objetivo e por que importa

Aprender a executar o fluxo **Personagem: rig, pesos e animação curta**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Malha com articulações e projeto Blender.

**Entregável verificável:** Personagem que faz um gesto sem deformação crítica.

## Como fazer — passo a passo

1. **Etapa 1:** Definir pose base neutra e nomes para esqueleto.
2. **Etapa 2:** Adicionar armature com ossos correspondentes ao corpo.
3. **Etapa 3:** Configurar hierarquia e evitar bones duplicados ou ambíguos.
4. **Etapa 4:** Associar malha ao rig e pintar pesos nas articulações.
5. **Etapa 5:** Testar rotação extrema em cotovelo e joelho; corrigir deformação.
6. **Etapa 6:** Escolher FK para gesto simples e IK para contato fixo quando necessário.
7. **Etapa 7:** Gravar keyframes para levantar braço e voltar à pose.
8. **Etapa 8:** Exportar FBX com rig e animação, testar retargeting no motor.
9. **Etapa 9:** Salvar vídeo de teste e registrar problemas conhecidos.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

Não publicar antes de conferir pesos, poses e root motion.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://docs.blender.org/manual/en/latest/animation/armatures/

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
