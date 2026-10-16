# Matriz de qualidade — ativos e produtos 3D

## Critérios observáveis

| Gate | Pergunta de aceitação | Evidência |
|---|---|---|
| Proveniência | Sabemos de onde veio cada item? | URL, autor, versão, data |
| Licença | A permissão cobre uso proposto, edição e distribuição? | Termos aplicáveis arquivados e decisão |
| Segurança | O pack traz scripts, executáveis, macros ou dependências? | Inspeção e isolamento |
| Geometria | O modelo está livre de erros relevantes? | Inspeção de normais, non-manifold, UV e topologia |
| Materiais | Normal, roughness e color space funcionam no destino? | Captura comparativa |
| Animação | Rig e movimentos reproduzem corretamente? | Vídeo/teste de esqueleto e root motion |
| Performance | Atende aparelhos e limite definido pelo produto? | FPS, tempos, memória, bytes e perfil de hardware |
| Acessibilidade | Existe alternativa funcional sem render ou animação? | Teste de teclado e reduced-motion |
| Privacidade | Existem faces, pessoas ou propriedades capturadas? | Consentimento/finalidade/autorização |
| Reprodutibilidade | Dá para repetir exportação e gerar o mesmo pacote? | Versões, parâmetros, checksums e comandos |

**Estados:** `NÃO AVALIADO`, `EM TESTE`, `PASSOU`, `FALHOU`, `NÃO APLICÁVEL com justificativa`. Não use porcentagem 100% sem cada evidência. A licitude é avaliação específica, não automatizada por links do catálogo.

## Testes de estresse

1. Abra cenas com GPU integrada ou aparelho de menor capacidade.
2. Limite velocidade de rede, interrompa download e confira comportamento de erro.
3. Execute zoom extremo para encontrar texturas ausentes, clipping e normais invertidas.
4. Reduza motion no sistema e navegue sem mouse.
5. Simule troca de versão do Blender ou motor e faça importação de regressão.
6. Retire uma fonte externa temporariamente para conferir fallback.
7. Faça auditoria de assets duplicados, modelos com escala errada e URLs alteradas.
8. Separe pré-visualização de produto homologado e gravado em produção.

## Critério de parada

**Não publicar** caso direitos de uso não estejam claros, scripts desconhecidos sejam executados, dados de captura não estejam autorizados ou experiência essencial não possua fallback. Para itens não críticos, abra pendência explícita em vez de criar sinal falso de aprovação.

[Índice geral](../INDEX.md)
