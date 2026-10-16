# Tutorial 12 — Snap Camera Kit: Lens em website com câmera

**Nível:** Avançado · **Pipeline:** [D04](../DEPENDENCIAS/PIPELINES.md#d04)

## Objetivo e por que importa

Aprender a executar o fluxo **Snap Camera Kit: Lens em website com câmera**, não apenas conhecer a interface: o resultado permite comparar compatibilidade, qualidade e custo no destino. Conteúdo demonstrativo não substitui as licenças e os testes da plataforma.

**Antes de começar:** Lens autorizada, acesso Snap Developer e conhecimento de JavaScript.

**Entregável verificável:** Prova controlada de sessão de AR por webcam, com consentimento e encerramento.

## Como fazer — passo a passo

1. **Etapa 1:** Solicitar e confirmar acesso ao Camera Kit Web.
2. **Etapa 2:** Ler SDK Web e verificar compatibilidade da Lens criada.
3. **Etapa 3:** Criar projeto de desenvolvimento separado do site em produção.
4. **Etapa 4:** Configurar pacote e restrições de domínio/token segundo guia atual.
5. **Etapa 5:** Abrir sessão Camera Kit e canvas; exibir solicitação de câmera antes de iniciar.
6. **Etapa 6:** Conectar fonte MediaStream permitida à sessão.
7. **Etapa 7:** Carregar Lens e Lens Group IDs autorizados e aplicar efeito.
8. **Etapa 8:** Implementar botão Parar que pausa sessão e encerra tracks de câmera.
9. **Etapa 9:** Tratar exceções, revogações de permissão e fallback não AR.
10. **Etapa 10:** Testar browsers suportados, CSP e orçamento de desempenho.

## Como saber se deu certo

- [ ] Cada etapa executada num arquivo próprio ou autorizado.
- [ ] Resultado salvo em formato nativo e de entrega, quando aplicável.
- [ ] Modelo em escala coerente, materiais e orientação conferidos.
- [ ] Teste feito na plataforma/dispositivo de destino; se não for possível, marcar **não testado**.
- [ ] Autoria, versões e licenças de cada asset/documentação registradas.
- [ ] Capturas e observações guardadas para reproduzir e melhorar o trabalho.

## Armadilha a evitar

SDK pode requerer ajustes delicados de CSP; não relaxe política indiscriminadamente.

## Onde aprender e conferir boas práticas

**Fonte primária:** https://developers.snap.com/camera-kit/integrate-sdk/web/web-configuration

**Apoio:** [Glossário](../GLOSSARIO/README.md) · [FAQ](../FAQ/README.md) · [Matriz de dependências](../DEPENDENCIAS/README.md) · [Checklist de qualidade](../GUIAS/06-QUALIDADE-PERFORMANCE.md)

**Próxima etapa:** revise o resultado com uma pessoa mais experiente ou compare com referências técnicas oficiais; a conclusão deste tutorial não equivale a homologação comercial ou autorização do provedor.
