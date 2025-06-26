# Modelo de Machine Learning para predição de Importação, Exportação ou Produão de Especeiarias

## Aprendizado de Máquina

### Equipe
- Daniela Soares de Oliveira - 180015222
- Gabriel Freitas Balbino - 180075462
- Mateus de Castro Santos - 222015195
- Pablo Santos Costa - 180128817
- Pedro Lucas Dourado Santos - 211039680

## Descrição do Dataset

Este projeto apresenta uma análise abrangente do consumo global de especiarias, compilada utilizando dados da FAOSTAT, coletados do Kaggle [aqui](https://www.kaggle.com/datasets/harishthakur995/global-spice-consumption). O consumo de especiarias é estimado aplicando a fórmula:

```
Consumo = Produção + Importação - Exportação
```

Esta abordagem garante uma estimativa precisa do uso doméstico real de especiarias, considerando os balanços comerciais entre diferentes países.

### Especiarias Incluídas

O dataset cobre nove especiarias principais amplamente consumidas e comercializadas globalmente:

1. Anis, Badiano, Coentro, Cominho, Alcaravia, Funcho e Bagas de Zimbro
2. Pimentas e Pimentões, Secos (Capsicum spp., Pimenta spp.)
3. Pimentas e Pimentões, Verdes (Capsicum spp. e Pimenta spp.)
4. Canela e Flores de Caneleira
5. Cravo (Talos Inteiros)
6. Gengibre (Cru)
7. Noz-moscada, Macis e Cardamomos
8. Pimenta (Piper spp.)
9. Baunilha (Crua)

Cada especiaria é rastreada em diferentes países para analisar tendências de produção, fluxo comercial e padrões de consumo.

### Características dos Dados

O dataset inclui os seguintes atributos principais:

- **País** – O país onde os dados de produção e comércio são registrados.
- **Ano** – O ano da coleta de dados (ex.: 2000–2023).
- **Produção (toneladas)** – A quantidade total de especiarias produzidas em um país.
- **Importação (toneladas)** – A quantidade importada para o país.
- **Exportação (toneladas)** – A quantidade exportada do país.
- **Consumo Estimado (toneladas)** – O consumo doméstico final calculado.

## Relevância para o Projeto de ML

Este dataset é valioso para:
- **Análise de Mercado** – Compreensão das tendências globais no consumo de especiarias.
- **Comércio e Economia** – Análise da dinâmica de importação e exportação de especiarias.
- **Indústria Alimentícia** – Identificação da demanda e cadeias de suprimentos para as principais especiarias.
- **Previsões e Projeções** – Uso de modelos estatísticos (ex.: ARIMA, Holt-Winters) para prever a demanda futura de especiarias.

## Fonte dos Dados

- **Fonte**: FAOSTAT (Organização das Nações Unidas para Agricultura e Alimentação)
- **Processamento de Dados**: O dataset foi limpo e refinado ajustando valores ausentes e garantindo consistência nos cálculos de fluxo comercial.

## Considerações Éticas e Legais

Os dados utilizados neste projeto são de domínio público, fornecidos pela FAO para uso em pesquisa e análise. Não há questões de privacidade envolvidas, pois os dados referem-se a estatísticas agregadas de produção e comércio por país, sem informações pessoais.

## Objetivo

Ao longo da disciplina, nossa equipe discutiu diversas abordagens possíveis para o desenvolvimento do projeto de aprendizado de máquina com dados de especiarias. Inicialmente, nosso objetivo era mais abrangente: queríamos explorar a previsão de três variáveis principais — **importação**, **exportação** e **produção** — de maneira simultânea. No entanto, ao aprofundarmos a análise dos dados e realizarmos os primeiros testes, percebemos que trabalhar com todas essas dimensões ao mesmo tempo poderia comprometer a qualidade das previsões e a clareza da metodologia.

Diante disso, decidimos adotar uma estratégia mais focada e escalável: **começar prevendo apenas uma das colunas**, e, a partir dos aprendizados e da estrutura construída, **expandir o projeto futuramente para as outras variáveis**. Essa abordagem nos permitiria consolidar uma base sólida de desenvolvimento, com menor complexidade inicial e maior controle sobre as variáveis envolvidas.

A variável escolhida para essa primeira fase foi a **importação**. A decisão foi motivada principalmente pelos **resultados empíricos obtidos nos testes de benchmark** realizados com os dados segmentados por especiaria.

Com isso, o objetivo consolidado do projeto passou a ser:

> Desenvolver um conjunto de modelos especializados, baseados em Random Forest, para prever a **importação** de cada uma das 9 especiarias ao longo do tempo, por país, servindo como a primeira fase de um projeto maior que poderá futuramente abranger também a previsão de exportações e produção.


## Instruções de Uso

1. **Requisitos de Ambiente**:
   - Python 3.8+
   - Pandas 1.3+
   - Matplotlib 3.4+
   - Seaborn 0.11+
   - Jupyter Notebook (opcional para execução do arquivo de análise)
   - MlFlow 

2. **Instalação de Dependências**:
   ```
   pip install -r requirements.txt
   pip install -r requirements_mlflow.txt
   ```

3. **Carregamento dos Dados**:
   ```bash
   mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001
   ```
   backend sendo hospedado em http://localhost:5001

4. **Executar experimentos**:
   ```bash
   python mlflow.py
   ```
5. **Iniciar interface web**:
   ```bash
   mlflow ui
   ```


## Links úteis relacionados ao projeto
**[Código de Conduta](https://github.com/mat054/Machine_learning_exportacoes/blob/main/CODE_OF_CONDUCT.md)**

**[Guia de contribuição](https://github.com/mat054/Machine_learning_exportacoes/blob/main/CONTRIBUTING.md)**

**[Linceça](https://github.com/mat054/Machine_learning_exportacoes/blob/main/LICENSE)**

**[Entregas Feitas](Entregas)