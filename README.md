# Filtro de Kalman 1D — Estimativa de Posição com Ruído

Este repositório contém um exemplo didático do **Filtro de Kalman** aplicado à estimativa da posição de um objeto em movimento retilíneo uniforme em uma dimensão, considerando medições ruidosas. O projeto foi desenvolvido em Python com visualização gráfica usando `matplotlib`.

## 📁 Estrutura

```

kalman/
├── main.py         # Código principal com simulação e filtro de Kalman
├── README.md       # Este arquivo

````

## 🚀 Execução

1. **Clone o repositório**:

```bash
git clone https://github.com/vitor-souza-ime/kalman.git
cd kalman
````

2. **Instale os pacotes necessários** (se ainda não tiver):

```bash
pip install matplotlib numpy
```

3. **Execute o script**:

```bash
python main.py
```

## 📈 Resultado Esperado

O gráfico gerado mostra:

* **Posição real** (linha contínua azul): representa o movimento ideal do objeto.
* **Medições ruidosas** (linha pontilhada laranja): simula um sensor com erros.
* **Estimativas do Filtro de Kalman** (linha contínua verde): aproximação mais precisa da posição real ao longo do tempo.

## 📚 Conceitos Envolvidos

* **Filtro de Kalman**: técnica recursiva de estimação baseada em predição e correção, utilizada em diversas áreas como robótica, navegação, controle e rastreamento.
* **Modelo do sistema**: movimento uniforme com velocidade constante.
* **Simulação de ruído**: ruído gaussiano adicionado às medições.

## 🔍 Detalhes Técnicos

* Inicialização:

  * Posição estimada inicial: `0`
  * Incerteza inicial: `P = 1`
  * Variância do processo: `Q = 1e-5`
  * Variância da medição: `R = 0.25`

* O algoritmo realiza:

  * **Predição** da posição com base na velocidade.
  * **Correção** usando a medição ruidosa ponderada com o **ganho de Kalman**.

## 📌 Autor

**Vitor Amadeu Souza**
