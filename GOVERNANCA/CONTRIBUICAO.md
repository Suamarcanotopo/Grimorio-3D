# Política de contribuições — atualização atemporal

1. **Pesquisar:** partir de fonte primária oficial e documentar URL, instituição, uso real e data de consulta.
2. **Classificar:** escolher nicho existente; novo nicho só quando a finalidade for distinta e justificável.
3. **Descrever:** fornecer título, descrição em português, URL HTTPS integral, para que serve, como começar e uma dica útil concreta.
4. **Licenciar:** não marcar 'uso comercial permitido' sem termos aplicáveis claros; se incerto, `não homologado`. Separar **acesso gratuito** de **direitos comerciais**.
5. **Preservar IDs:** IDs existentes são estáveis, mesmo que a URL mude por redirecionamento. Não reutilizar IDs excluídos.
6. **Testar:** executar `python3 scripts/validar.py`. Não alterar manualmente só um dos formatos sem atualizar o outro.
7. **Documentar:** explicar por que o novo recurso agrega valor e como testar; acrescente caso didático ou revisão de conteúdo se relevante.
8. **Revisar:** submissões de terceiros não introduzem scripts de instalação remota, credenciais, scraping abusivo ou redistribuição de modelos protegidos.
9. **Versionar:** usar branch, diff e Pull Request. Não reescrever histórico para criar falsa aprovação.
10. **Manter:** links, planos e licenças mudam; revisão periódica pode marcar uma entrada como desatualizada, nunca apagar silenciosamente histórico.

## Template de sugestão

```yaml
titulo: ""
descricao_ptbr: ""
url_completa: "https://"
nicho: ""
para_que_serve: ""
como_comecar: ""
dica_pratica: ""
modelo_acesso: "A confirmar"
licenca_especifica: "A confirmar"
fonte_oficial_de_termos: ""
data_consulta: "AAAA-MM-DD"
prova_teste: "Não realizado"
```

**Não usar** arte, scripts e datasets de terceiros no repositório sem licença de redistribuição.
