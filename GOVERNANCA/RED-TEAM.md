# Coliseu adversarial — casos que bloqueiam uma contribuição

| Ataque / falha plausível | Como testar | Resultado seguro |
|---|---|---|
| Link de catálogo imita site oficial | Comparar domínio, HTTPS e documentação do fornecedor | Rejeitar ou colocar em quarentena |
| Pack gratuito com proibição comercial | Examinar licença do **item**, não só home da plataforma | Impedir uso comercial até autorização |
| Asset com marca/rosto sem cessão | Revisão de direitos conexos e privacidade | Recusar redistribuição |
| Plugin solicita execução de código desconhecido | Auditar dependências e executar em sandbox | Não executar por padrão |
| Asset GLB gigante trava celular | Testar download, CPU, GPU e memória em aparelho-alvo | Fallback, compressão ou recusa |
| Shader ou efeito induz desconforto | Testar movimento reduzido e keyboard-only | Alternativa estática/usável |
| Pipeline perde projeto nativo | Comparar entregas e backup por commit | Preservar origem, versionar export |
| CSV com fórmula maliciosa | Procurar células iniciadas por operadores de fórmula | Bloquear ingestão |
| Fontes duplicadas para inflar contagem | Comparar URLs normalizadas e IDs | Recusar duplicata |
| Mudança de plano/licença | Conferir termos vigentes no download e publicação | Marcar como não homologado até reconfirmação |
| Captura 3D de ambiente restrito | Verificar autorização e eliminação de dados pessoais | Não distribuir nem publicar |
| AI-generated 3D com proveniência obscura | Ler termos, revisão de saída e direitos de imagem | Não presumir exclusividade ou uso comercial |

**Não são testes executados automaticamente nesta matriz.** A validação automática cobre apenas regras do dataset e a presença documental; integração exige execução e evidência externa.
