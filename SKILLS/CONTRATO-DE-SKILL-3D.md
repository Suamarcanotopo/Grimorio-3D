# Template de contrato — competência de Skills 3D

> Exemplo didático. Este arquivo NÃO é uma SKILL.md instalada e não ativa ferramentas externas.

```yaml
skill_name: sin-3d-example
status: CANDIDATE_ONLY
mission: "Domínio específico e verificável — por exemplo validar GLB para web."
owners:
  controller: engineering-control-plane
  reviewer: coliseum
  specialist: sin-motion-expertise-council
triggers:
  positive: ["Validar modelo GLB próprio para web"]
  negative: ["Gerar conteúdo protegido sem autorização"]
inputs:
  required: ["arquivo de origem", "destino alvo", "restrições de licença"]
capabilities:
  analyze: ["identificar topologia, material, escala e formatos"]
  design: ["propor pipeline e orçamentos"]
  build: ["gerar relatório ou um asset permitido se houver ferramenta"]
  execute: ["somente ações com ferramenta real, permissão e registro"]
  verify: ["testes reais de importação, performance e licenças"]
forbidden:
  - "afirmar que GLB sozinho garante AR em todos dispositivos"
  - "aprovar licença comercial sem termos do item"
  - "editar fonte de terceiros sob licença restritiva"
dependencies:
  knowledge:
    - "../CURRICULO/ETAPAS-DA-PRODUCAO.md"
    - "../GOVERNANCA/FONTES-ATEMPORAIS-E-ATUAIS.md"
  tooling:
    - "declaração de versões e disponibilidade, sem auto-instalação"
  runtime:
    - "dispositivo e engine indicados pelo usuário"
evidence:
  - "teste no software de destino"
  - "arquivo nativo e checksum"
  - "capturas e métricas"
  - "registro de licença"
red_team: "../SKILLS/casos-red-team.json"
rollback: "reversão do PR/versionamento sem perder arquivos nativos"
```

## Como validar uma Skill dessa família

1. Pegue um único caso de uso e uma fonte oficial.
2. Faça 3 casos de sucesso, 3 falhas previsíveis e um caso adversarial legal/performance.
3. Teste o mesmo fluxo em versões e dispositivos declarados; marque `NÃO TESTADO` quando inacessíveis.
4. Peça revisão independente do Coliseu e preserve baseline.
5. Só promova no repositório canônico de Skills com protocolo próprio.

**Não apagar competências existentes** para adicionar conhecimento de 3D; especialize contratos de referência e adapte ao destino.
