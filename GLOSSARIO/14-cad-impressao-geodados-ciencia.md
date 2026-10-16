# 14 · CAD, impressão 3D, geodados e ciência

**18 conceitos**. Cada verbete explica a técnica, sua importância e um teste que pode ser reproduzido com material próprio.

[Índice do Glossário](README.md) · [Trilhas profissionais](../NICHOS/README.md)

### 1. Parametric CAD (CAD paramétrico)

**O que é:** Modelagem orientada por medidas, relações e restrições editáveis.

**Por que importa:** Permite alterações dimensionais sem reconstruir a peça.

**Como praticar:** Faça um furo de diâmetro parametrizado.

**Onde aprender:** https://3mf.io/spec/

### 2. Sketch Constraint (restrição de esboço)

**O que é:** Regra geométrica ou dimensional aplicada ao sketch CAD.

**Por que importa:** Mantém relações de design durante edição.

**Como praticar:** Fixe paralelismo e dimensão de retângulo.

**Onde aprender:** https://3mf.io/spec/

### 3. Tolerance (tolerância dimensional)

**O que é:** Faixa aceitável de variação de uma medida física.

**Por que importa:** É essencial em encaixe e fabricação.

**Como praticar:** Modele duas peças com folga controlada.

**Onde aprender:** https://3mf.io/spec/

### 4. Watertight Mesh (malha estanque)

**O que é:** Malha fechada que delimita volume sem aberturas indevidas.

**Por que importa:** Ajuda impressão 3D e cálculos volumétricos.

**Como praticar:** Teste non-manifold e corrija buracos.

**Onde aprender:** https://3mf.io/spec/

### 5. G-code (código de movimento de máquina)

**O que é:** Instruções de movimento e controle para impressoras CNC/3D.

**Por que importa:** Liga modelo digital ao processo de fabricação.

**Como praticar:** Inspecione preview do slicer antes da impressão.

**Onde aprender:** https://3mf.io/spec/

### 6. Slicer (fatiador)

**O que é:** Software que transforma modelo em camadas e instruções de impressão.

**Por que importa:** Determina suporte, preenchimento e tempo estimado.

**Como praticar:** Fatie peça e compare infill.

**Onde aprender:** https://3mf.io/spec/

### 7. Infill (preenchimento)

**O que é:** Estrutura interna impressa que ocupa parte do volume.

**Por que importa:** Afeta rigidez, material e duração de impressão.

**Como praticar:** Compare 10% e 30% em teste não estrutural.

**Onde aprender:** https://3mf.io/spec/

### 8. Support Structures (estruturas de suporte)

**O que é:** Geometrias auxiliares para sustentar saliências na impressão.

**Por que importa:** Pode evitar falhas de impressão.

**Como praticar:** Teste orientação da mesma peça.

**Onde aprender:** https://3mf.io/spec/

### 9. Layer Height (altura de camada)

**O que é:** Espessura vertical de cada camada depositada.

**Por que importa:** Muda acabamento, tempo e resistência.

**Como praticar:** Compare peça com duas alturas.

**Onde aprender:** https://3mf.io/spec/

### 10. BIM Property Set (conjunto de propriedades BIM)

**O que é:** Atributos normalizados associados a elementos de construção.

**Por que importa:** Permite consultar dados além da geometria.

**Como praticar:** Associe propriedades a porta IFC.

**Onde aprender:** https://3mf.io/spec/

### 11. IFC Schema (esquema IFC)

**O que é:** Modelo padronizado de entidades e relações de construção.

**Por que importa:** Ajuda interoperabilidade entre plataformas BIM.

**Como praticar:** Verifique versão IFC em arquivo de exemplo.

**Onde aprender:** https://3mf.io/spec/

### 12. GeoReference (georreferência)

**O que é:** Associação de dados a um sistema de coordenadas espacial.

**Por que importa:** Mantém posição correta entre terreno e modelo.

**Como praticar:** Registre CRS do arquivo GIS.

**Onde aprender:** https://3mf.io/spec/

### 13. CRS — Coordinate Reference System (sistema de referência)

**O que é:** Padrão que interpreta posições geográficas e projeções.

**Por que importa:** Evita deslocamento e deformação de dados.

**Como praticar:** Compare WGS84 e CRS projetado.

**Onde aprender:** https://3mf.io/spec/

### 14. DTM — Digital Terrain Model (modelo digital do terreno)

**O que é:** Representação da superfície do solo sem vegetação/edificações.

**Por que importa:** Apoia cenários urbanos e engenharia.

**Como praticar:** Gere terreno a partir de dados licenciados.

**Onde aprender:** https://3mf.io/spec/

### 15. DSM — Digital Surface Model (modelo digital de superfície)

**O que é:** Modelo de altitude incluindo elementos sobre o solo.

**Por que importa:** Serve a visualização de cidades e copas.

**Como praticar:** Compare DSM e DTM para mesmo setor.

**Onde aprender:** https://3mf.io/spec/

### 16. 3D Tiles (tiles espaciais 3D)

**O que é:** Estrutura de streaming hierárquico de modelos geoespaciais volumosos.

**Por que importa:** Permite cidades de grande escala no navegador.

**Como praticar:** Teste tile com LOD em Cesium.

**Onde aprender:** https://3mf.io/spec/

### 17. DICOM (padrão de imagem médica)

**O que é:** Conjunto de formatos e protocolos de imagem em saúde.

**Por que importa:** Permite visualizar exames e volumes, com dados sensíveis.

**Como praticar:** Use apenas dataset anonimizado e autorizado.

**Onde aprender:** https://3mf.io/spec/

### 18. Volume Segmentation (segmentação volumétrica)

**O que é:** Separação de regiões 3D em imagens científicas ou médicas.

**Por que importa:** Produz superfícies e medidas de regiões.

**Como praticar:** Segmente volume de demonstração no 3D Slicer.

**Onde aprender:** https://3mf.io/spec/

---

**Ecossistema SIN:** [Website](https://sistemaimersivonarrativo.com.br/) · [Instagram](https://www.instagram.com/suamarcanotopo/) · [YouTube](https://www.youtube.com/@suamarcanotopo?sub_confirmation=1) · [Comunidade Grimório 3D](https://chat.whatsapp.com/F6cfNhh2Fx31VJ74KMpbk5). Se este material ajudar, deixe uma estrela no repositório.
