# Convenções, truques e erros que valem na prática

Uma referência técnica só é útil quando ajuda a tomar decisões e corrigir erros. Estas convenções são **adaptações didáticas**, não regras universais de um software. Sempre confira o destino e a documentação versionada.

## E01 · Briefing, finalidade e limites

**Quando usar:** Brief de uma página com mercado, público, hardware, licença e objetivo mensurável
**Convenção:** Convenção: nomeie arquivos por projeto_versao_destino; registre unidades e uso comercial já no briefing.
**Truque:** Truque: faça uma frase de aceite verificável antes de abrir Blender; evita retrabalho estético.
**Diagnóstico / erro comum:** Erro típico: começar por software ou efeito da moda sem saber onde será executado.
**Prova mínima:** O briefing especifica resultado, dono, limitação e critério observável.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E02 · Repertório e fontes comprováveis

**Quando usar:** Moodboard técnico com três fontes, autor e condições de uso
**Convenção:** Convenção: documento oficial ≠ licença do asset; inclua autor, URL, data e direitos de cada peça.
**Truque:** Truque: compare duas fontes independentes e documente por que uma é mais adequada ao destino.
**Diagnóstico / erro comum:** Erro típico: considerar asset gratuito comercialmente reutilizável sem ler termos.
**Prova mínima:** Cada referência possui URL íntegra, aplicação e direito de reutilização identificado ou pendente.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E03 · Conceito, storyboard e mensagem

**Quando usar:** Storyboard com três planos, objetivo narrativo e tempo
**Convenção:** Convenção: identifique planos SH010, SH020, SH030 e anote enquadramento/FPS.
**Truque:** Truque: teste os três quadros sem áudio; se a mensagem não for compreendida, corrija antes de renderizar.
**Diagnóstico / erro comum:** Erro típico: investir em detalhe antes de validar narrativa ou composição.
**Prova mínima:** A sequência comunica ação e objetivo em poucos segundos sem explicação extra.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E04 · Blockout, unidades e pivôs

**Quando usar:** Cena blockout medida, com origem e proporções corretas
**Convenção:** Convenção: use metros/unidades declaradas e origem no ponto de interação, não no centro arbitrário.
**Truque:** Truque: teste uma dobradiça com pivô na borda antes de animar a porta.
**Diagnóstico / erro comum:** Erro típico: exportar escala não aplicada e ter produto fora do tamanho real em AR.
**Prova mínima:** A dimensão de um objeto de referência permanece igual após exportar e reimportar.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E05 · Geometria, retopologia e escultura

**Quando usar:** Versões high e low-poly comparáveis e malha sem erros críticos
**Convenção:** Convenção: mantenha high-poly editável e low-poly de runtime em arquivos distintos.
**Truque:** Truque: verifique silhueta com material cinza e rotação de câmera antes de esculpir detalhes.
**Diagnóstico / erro comum:** Erro típico: confundir grande contagem de polígonos com maior qualidade no destino.
**Prova mínima:** A malha não apresenta buracos inesperados, sombras invertidas nem erros de escala.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E06 · UV, materiais e baking

**Quando usar:** Malha com UV, checker sem deformação e materiais PBR testados
**Convenção:** Convenção: trate Base Color em sRGB e mapas de dados como Non-Color quando a documentação pedir.
**Truque:** Truque: deixe padding em ilhas UV para evitar vazamento de mipmaps nas costuras.
**Diagnóstico / erro comum:** Erro típico: normal map com convenção de canal verde incorreta ou AO/Metal/Roughness trocados.
**Prova mínima:** Checker sem distorção relevante e PBR visualmente coerente em duas iluminações.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E07 · Lookdev e consistência de cor

**Quando usar:** Comparativo de material sob duas luzes com espaço de cor documentado
**Convenção:** Convenção: fixe View Transform e espaço de trabalho; não faça comparação baseada em screenshots de monitores diferentes.
**Truque:** Truque: confira metal em HDRI e gradiente de roughness para identificar plasticidade falsa.
**Diagnóstico / erro comum:** Erro típico: tratar diferenças de tone mapping como defeitos do mapa Base Color.
**Prova mínima:** Dois renders do mesmo material preservam aparência justificável dentro do pipeline declarado.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E08 · Rig, skinning e retarget

**Quando usar:** Rig autoral com poses extremas e pesos revistos
**Convenção:** Convenção: documente T-pose/A-pose, nomes de ossos e direção dos eixos antes de exportar.
**Truque:** Truque: teste ombro, joelho e punho com material neutro antes de trabalhar texturas finas.
**Diagnóstico / erro comum:** Erro típico: assumir que rigs de diferentes softwares têm hierarquia compatível sem retarget.
**Prova mínima:** Personagem completa poses extremas sem deformações graves e com esqueleto rastreável.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E09 · Animação, acting e movimento

**Quando usar:** Animação curta com poses, curvas e intenção reconhecível
**Convenção:** Convenção: fixe FPS e mantenha nomes de clips/ações ao exportar.
**Truque:** Truque: avalie silhueta e contato de pés com imagem sem textura; use stepped no blocking.
**Diagnóstico / erro comum:** Erro típico: foot sliding por falta de contato/IK ou mudança de root motion.
**Prova mínima:** Outra pessoa consegue identificar ação; pés e articulações permanecem coerentes.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E10 · Tracking e captura de referência

**Quando usar:** Plano rastreado com objeto virtual ancorado e erro observado
**Convenção:** Convenção: mantenha metadados de câmera e timecode ligados ao ID do plano.
**Truque:** Truque: grave uma régua ou objeto de medida conhecida para recuperar escala.
**Diagnóstico / erro comum:** Erro típico: solve aparente em um único frame, com deslizamento ao longo do vídeo.
**Prova mínima:** O objeto mantém posição relativa durante todo o plano, e falhas estão documentadas.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E11 · VFX, procedural, volumes e simulação

**Quando usar:** Cena procedural ou efeito com seed/cache, antes e depois de performance
**Convenção:** Convenção: versionar parâmetros e caches; não incorporar binários de terceiros no Grimório.
**Truque:** Truque: instancie repetição de árvores e limite transparência de partículas antes de refinar.
**Diagnóstico / erro comum:** Erro típico: crescer a simulação sem medir VRAM, frame time ou tempo de render.
**Prova mínima:** Reexecução com a mesma configuração gera resultado comparável e medido.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E12 · Câmera, iluminação, render e passes

**Quando usar:** Render com câmeras, luzes, passes ou EXR apropriado ao destino
**Convenção:** Convenção: registre lente, HDRI, espaço de cor e versão de renderer junto do shot.
**Truque:** Truque: faça render de 1 frame em baixa amostragem e revise silhouette/sombra antes de render longo.
**Diagnóstico / erro comum:** Erro típico: render de alta qualidade no PC usado como prova de performance em Quest.
**Prova mínima:** Plano final atende enquadramento e o render pode ser reproduzido em ambiente equivalente.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E13 · Montagem, áudio e comunicação

**Quando usar:** Vídeo curto legível com direitos de áudio e mensagem clara
**Convenção:** Convenção: exporte cena e áudio em versões separadas para revisão; guarde FPS e timecode.
**Truque:** Truque: assista ao anúncio sem som e no tamanho real de smartphone antes de aprovar.
**Diagnóstico / erro comum:** Erro típico: legendas ilegíveis, licença de trilha não conferida ou áudio dessincronizado.
**Prova mínima:** Narrativa é compreendida sem áudio e licenças dos elementos visuais/sonoros estão registradas.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E14 · Otimização de runtime e testes

**Quando usar:** Matriz de bytes, texturas, memória e tempo de quadro antes/depois
**Convenção:** Convenção: informe FPS com hardware, resolução, versão, duração e cena; nunca use valor solto.
**Truque:** Truque: reduza primeiro a textura/overdraw que o profiler comprova pesada, não os triângulos por reflexo.
**Diagnóstico / erro comum:** Erro típico: usar FPS desktop como evidência de mobile/headset.
**Prova mínima:** Métrica comparável indica custo menor sem regressão funcional ou visual inaceitável.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E15 · Formatos, intercâmbio e versionamento

**Quando usar:** Arquivo nativo + export GLB/FBX/USD/3MF apropriado, hash e manifesto
**Convenção:** Convenção: BLEND não é substituído por GLB; mantenha origem, exportação e SHA-256 em separado.
**Truque:** Truque: compare material, escala e animação antes/depois do round-trip para detectar diferenças.
**Diagnóstico / erro comum:** Erro típico: usar STL para engenharia paramétrica ou esperar shader Blender idêntico na web.
**Prova mínima:** O arquivo reimportado cumpre campos requeridos e a origem permanece editável.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E16 · Distribuição — websites, apps, games e XR

**Quando usar:** Demo em destino declarado (ou status não testado) com fallback e permissões
**Convenção:** Convenção: WebAR/Scene Viewer, Lens Snap, Effect House e Meta XR são destinos distintos; nenhuma URL universal.
**Truque:** Truque: em páginas de venda, mantenha CTA e descrição HTML acessíveis mesmo sem 3D.
**Diagnóstico / erro comum:** Erro típico: assumir que um GLB ou efeito Snap roda automaticamente em todos os navegadores e headsets.
**Prova mínima:** Teste no dispositivo/conta real ou registre explicitamente NÃO TESTADO, sem simular homologação.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E17 · Direitos, segurança, privacidade e acesso

**Quando usar:** Manifesto de direitos por asset e avaliação de segurança/privacidade
**Convenção:** Convenção: licença MIT do repositório não licencia modelos, fotos, áudio ou marca de terceiros.
**Truque:** Truque: registre 'pendente' em vez de adivinhar permissões; use modelos próprios até regularizar direitos.
**Diagnóstico / erro comum:** Erro típico: interpretar asset gratuito como autorização para revenda ou reuso irrestrito.
**Prova mínima:** Nenhum asset externo sem direito esclarecido é tratado como aprovado.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

## E18 · Entrega, avaliação e evolução das Skills

**Quando usar:** Pacote de origem, resultado, métricas, evidências, riscos e rollback
**Convenção:** Convenção: status DOCUMENTADO, TESTADO e HOMOLOGADO são diferentes; não promova Skill sem evals.
**Truque:** Truque: crie um erro deliberado de escala/licença no teste para comprovar capacidade de diagnóstico.
**Diagnóstico / erro comum:** Erro típico: declarar 100% concluído por links e CI documental sem verificar runtime ou direitos.
**Prova mínima:** Outro profissional consegue reproduzir o resultado e auditar decisões, testes e limitações.
**Conexão:** [Manual de etapas](ETAPAS-CONECTADAS.md) · [Fontes da competência](../README.md#index-geral--368-fontes-e-urls-completas)

---

**Comunidade SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [Working Lab](https://chat.whatsapp.com/FcyMOdQqyW8Ci104P8i3Gg?s=cl&p=i&mlu=4&ilr=4) · [Comunidade 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5).