# Registro transversal de dependências — sem multiplicar ferramentas

## Dependência 1: saber onde aprender

URL de referência, sem executar scripts. Exemplos: `Blender Manual`, `OpenColorIO`, `Unreal ICVFX`. Esta classe pertence ao Grimório.

## Dependência 2: dominar técnica

Exercício e prova: geometria, animação, rig, UV, PBR, tracking, render, AR. Esta classe pertence ao currículo de 18 etapas e às trilhas de mercado.

## Dependência 3: software instalado

Blender, Unreal, Maya, Houdini, Nuke, Effect House, Lens Studio. A versão deve ser fixada **no projeto onde for usada**, não como dependência global do repositório textual.

## Dependência 4: SDK, conta ou serviço

Camera Kit, Meta XR, ARCore, Quick Look, WebXR, hardware e plataformas. Exige matriz de compatibilidade, contas, termos, políticas de câmera e teste real. A dependência só fica ativa no **projeto específico**.

## Dependência 5: asset ou dataset de terceiro

Licença e direitos por item, captura/reutilização, autor e versão. Nunca depender de URL para substituir cópia autorizada nem redistribuir pacotes sem direito.

## Regras

- **Fonte canônica:** `FONTES/catalogo.json` e espelho CSV, ambos revisados por CI.
- **Currículo:** `CURRICULO/ETAPAS-DA-PRODUCAO.md` define sequência e testes.
- **Mercado:** `NICHOS/` define resultado específico, não duplica informação cadastral.
- **Plataformas voláteis:** `DEPENDENCIAS/` detalha handoffs; `ATUALIDADES/` observa mudanças datadas.
- **Skill:** `SKILLS/` define capabilities, evals e interlocks; **não instala skill**.
- **Não há pip install, npm install, plugin zip ou auto-download exigido pelo Grimório**: use o projeto do consumidor.
