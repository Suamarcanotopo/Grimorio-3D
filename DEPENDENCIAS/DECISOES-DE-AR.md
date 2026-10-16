# Decisões de AR — evite escolher a plataforma errada

## Primeiro responda: onde o público acessará?

| Público / experiência | Stack preferencial de protótipo | O que ela NÃO é |
|---|---|---|
| Cliente vê móvel ou produto em sua casa pelo navegador | GLB + model-viewer + Scene Viewer/Quick Look conforme aparelho | Não é um filtro social de TikTok ou Snap |
| Pessoa usa máscara/filtro no Snapchat | Lens Studio + publicação Snap | Não vira website automaticamente |
| Pessoa usa lente no website com câmera Snap | Lens Studio + Camera Kit Web SDK + credenciais e revisão | Não é um embed HTML sem SDK |
| Pessoa usa efeito em vídeo TikTok | Effect House + diretrizes TikTok | Não é publicar no Instagram |
| Usuário explora Quest e objetos na sala | Unreal + Meta XR ou SDK suportado / headset | Não é Meta Spark |
| Usuários constroem mundos sociais Horizon | Ferramenta Meta Horizon realmente liberada à conta | Não é substituto automático de filtros antigos |
| Usuário entra em VR pelo navegador Quest | WebXR / runtime web compatível e fallback | Não garante rodar em todos os navegadores |
| Aplicativo mobile personalizado de AR | Unreal Handheld AR, ARCore ou ARKit conforme app | Não é website hospedado sem app |

## Estados de plataforma que não podem ser omitidos

- **Meta Spark de terceiros:** ENCERRADO (14 de janeiro de 2025). Não oferecer publicação por ele. Referência histórica: https://www.reuters.com/technology/meta-shut-augmented-reality-studio-used-by-third-party-creators-2024-08-27/
- **Meta Horizon Create/Studio:** anunciado em 2026; ferramentas, acesso e recursos específicos devem ser confirmados na conta e na documentação atual: https://developers.meta.com/blog/meta-connect-recap/
- **Snap Lens Studio / Camera Kit:** documentados como soluções ativas, mas exigem conta, formatos, acessos, política e compatibilidade. https://developers.snap.com/
- **TikTok Effect House:** documentado como solução ativa, porém todo efeito depende de QA, políticas e capacidade do aparelho. https://effecthouse.tiktok.com/

## Preferência estratégica de engenharia

1. Modelagem **autoral e editável** no Blender.
2. Definição de destino e orçamento antes de comprar asset/licença.
3. Entrega em arquivo intermediário interoperável quando suportado.
4. Integração no **editor/SDK específico** sem prometer portabilidade perfeita.
5. Teste em dispositivo real, conformidade comercial e fallback.
6. Versionamento e evidência para poder migrar de plataforma.

**Proteção comercial:** não vender a um cliente experiência que exige aprovação ou SDK não contratado como se fosse recurso nativo garantido.
