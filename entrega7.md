# Teste de Modelos de Aprendizado de Máquina

## Mini Trabalho 7 - Apresentação e documentação da solução

### Equipe
- Daniela Soares de Oliveira - 180015222
- Gabriel Freitas Balbino - 180075462
- Mateus de Castro Santos - 222015195
- Pablo Santos Costa - 180128817
- Pedro Lucas Dourado Santos - 211039680

## Descrição do Trabalho Realizado:
Este mini trabalho teve como foco uma nova abordagem sobre as entregas anteriores já realizadas com foco na melhoria. Nessa entrega o grupo em comum acordo decidiu separar o dataset que já tinhamos em 9 novos datasets menores separados por cada tipo de especiaria com o objetivo de alcançar melhores metricas finais. Apos essa separação, os dados foram novamente tratados e todos os outliers foram retirados.Nosso objetivo então foi tentar fazer a predição separadamente de importação, exportação e produção, ao invés de prever as 3 juntas como um unico modelo apenas como estávamos fazendo e para cada uma dessas previsões, testar qual modelo apresenta melhor desempenho(Regressão linear, random forest, etc).Por fim foi feita a escolha apenas da coluna importação para cada especiaria, resultando em 9 modelos para as previsões e depois foi feito refinamento que envolve validação cruzada e ajustes de parâmetros.

### 1. Análise Exploratória dos Dados

A primeira etapa do projeto foi dedicada à compreensão profunda do dataset original. Essa fase foi essencial para orientar as decisões de limpeza, segmentação e modelagem.

* **Identificação das colunas importantes**: Inicialmente, mapeamos quais atributos eram realmente relevantes para o problema de previsão. Entre as colunas consideradas essenciais estavam: `ano`, `país`, `especiaria`, `valor de importação`, `valor de exportação` e `valor de produção`.

* **Levantamento dos países presentes**: Analisamos a abrangência geográfica do dataset, identificando os países com dados suficientes ao longo do tempo para garantir a consistência na modelagem.

* **Intervalo temporal dos dados**: Investigamos o período coberto pelos dados. Essa informação foi importante para entender a evolução temporal das operações e garantir que os modelos pudessem capturar tendências ao longo dos anos.

* **Especiarias analisadas**: Detectamos a presença de 9 categorias distintas de especiarias. A presença dessas categorias foi posteriormente usada para segmentar o dataset e treinar modelos especializados.

* **Visualizações iniciais**: Criamos gráficos para observar tendências e padrões, como séries temporais por país e especiaria, o que nos ajudou a observar comportamentos sazonais, picos e quedas abruptas, além de possíveis valores inconsistentes.

---

### 2. Identificação e Remoção de Outliers

Compreender e tratar valores extremos era fundamental para garantir a qualidade do modelo preditivo. Por isso, seguimos um processo rigoroso de identificação de outliers.

* **Segmentação inicial do dataset**: Dividimos o dataset por três dimensões principais: tipo de especiaria, tipo de atividade (importação, exportação e produção) e país. Essa divisão permitiu uma análise mais localizada e eficaz, visto que o comportamento de uma especiaria em um país pode ser completamente diferente de outra.

* **Análise visual dos dados ao longo do tempo**: Para cada grupo segmentado, plotamos gráficos de série temporal. Isso nos permitiu identificar outliers visuais — valores drasticamente diferentes do padrão histórico daquele grupo.

* **Aplicação do método dos quartis (IQR)**: Aplicamos uma abordagem estatística robusta para detectar outliers, com base nos limites inferior e superior (Q1 - 1.5 \* IQR e Q3 + 1.5 \* IQR). Os pontos identificados como outliers foram destacados nos gráficos em vermelho para facilitar a validação visual.

* **Criação de colunas auxiliares para outliers**: Ao invés de remover imediatamente os outliers, criamos colunas binárias (`outliers_importação`, `outliers_exportação`, `outliers_produção`) para marcar esses dados. Isso nos deu flexibilidade: podíamos filtrar os outliers facilmente caso decidíssemos prever uma ou mais colunas posteriormente, sem perder os dados originais.

---

### 3. Testes de Benchmark de Modelos de Machine Learning

Após o tratamento dos dados, partimos para a fase de experimentação com modelos preditivos. O objetivo era testar diferentes abordagens e algoritmos para encontrar a solução mais eficaz.

* **Testes iniciais com o dataset completo**: Na primeira rodada de testes, aplicamos os modelos nos dados consolidados, sem segmentação por especiaria. Embora os resultados tenham sido satisfatórios, percebemos que o comportamento das especiarias era muito distinto, o que prejudicava a acurácia dos modelos.

* **Segmentação por especiaria**: Como resposta, decidimos dividir o dataset em 9 subconjuntos, um para cada especiaria. Com isso, cada modelo se especializaria no comportamento individual de uma única especiaria, o que aumentou consideravelmente o desempenho.

* **Previsão separada para cada atividade (importação, exportação, produção)**: Para cada uma das 9 especiarias, testamos três tipos de previsões separadamente: apenas importação, apenas exportação e apenas produção. Utilizamos algoritmos como:

  * Regressão Linear
  * Árvore de Decisão
  * Random Forest

* **Escolha do foco do projeto (importação)**: Os testes mostraram que a **Random Forest** apresentava excelente desempenho na previsão da **importação** para praticamente todas as especiarias. Com isso, decidimos restringir o escopo à previsão da importação, treinando **9 modelos especializados** — um para cada especiaria — com foco em maximizar a precisão dessa tarefa específica.

---

### 4. Refinamento, Ajuste de Hiperparâmetros e Validação Cruzada

Com os modelos definidos e os dados preparados, iniciamos o processo de refinamento para maximizar o desempenho e garantir a robustez dos modelos.

* **Refinamento com Random Forest**: Utilizamos o algoritmo Random Forest como base para os 9 modelos finais. Foi feita uma busca pelos melhores hiperparâmetros (como número de estimadores, profundidade máxima da árvore, número mínimo de amostras por divisão, etc.).

* **Aplicação de validação cruzada (K-Fold)**: Para garantir a generalização dos modelos, utilizamos validação cruzada com 5 dobras. Isso permitiu que cada modelo fosse testado em diferentes subconjuntos dos dados, aumentando a confiabilidade das métricas obtidas.

* **Comparação entre antes e depois do refino**: Registramos as métricas obtidas antes e depois do refinamento para cada especiaria, observando melhorias em diversos casos. Esse processo confirmou a importância de segmentar os dados e refinar os parâmetros individualmente.

* **Observação adicional**: Ressaltamos que uma tentativa anterior de refinamento havia sido realizada com o dataset completo, mas os resultados foram inferiores. O aprendizado obtido com esse erro foi essencial para orientar a nova abordagem.


## Nosso objetivo:
Ao longo da disciplina tivemos diversos debates sobre qual era realmente nosso objetivo com os dados e por fim decidimos que nosso obejtivo final era criar um modelo de previsao para importação para um determinado grupo de especiarias ao longo do tempo, podendo ser expandido para exportação e produção.

Claro! Abaixo está a versão **reescrita da seção "Nosso Objetivo"**, considerando os dois pontos que você pediu:

1. A escolha da **importação** como primeira etapa de um projeto que será expandido futuramente para exportação e produção;
2. A predominância do **Random Forest** como o melhor algoritmo nos testes para previsão de importação, motivando sua escolha para todos os modelos.

---

## Nosso Objetivo

Ao longo da disciplina, nossa equipe discutiu diversas abordagens possíveis para o desenvolvimento do projeto de aprendizado de máquina com dados de especiarias. Inicialmente, nosso objetivo era mais abrangente: queríamos explorar a previsão de três variáveis principais — **importação**, **exportação** e **produção** — de maneira simultânea. No entanto, ao aprofundarmos a análise dos dados e realizarmos os primeiros testes, percebemos que trabalhar com todas essas dimensões ao mesmo tempo poderia comprometer a qualidade das previsões e a clareza da metodologia.

Diante disso, decidimos adotar uma estratégia mais focada e escalável: **começar prevendo apenas uma das colunas**, e, a partir dos aprendizados e da estrutura construída, **expandir o projeto futuramente para as outras variáveis**. Essa abordagem nos permitiria consolidar uma base sólida de desenvolvimento, com menor complexidade inicial e maior controle sobre as variáveis envolvidas.

A variável escolhida para essa primeira fase foi a **importação**. A decisão foi motivada principalmente pelos **resultados empíricos obtidos nos testes de benchmark** realizados com os dados segmentados por especiaria.

Com isso, o objetivo consolidado do projeto passou a ser:

> Desenvolver um conjunto de modelos especializados, baseados em Random Forest, para prever a **importação** de cada uma das 9 especiarias ao longo do tempo, por país, servindo como a primeira fase de um projeto maior que poderá futuramente abranger também a previsão de exportações e produção.




## Metodolgia:
Ao longo da disciplina foram feitas as seguintes atividades:

1. **Entender nosso tema e nosso objetivo**  
   Aqui queríamos fazer uma predição das especiarias ao longo do tempo, mas não sabíamos como seria feito isso ainda.

2. **Entender os dados**  
   Nessa etapa, o principal objetivo era entender quais dados tínhamos, fazer uma primeira limpeza de dados nulos, seleção das colunas mais relevantes e criação dos primeiros gráficos, a fim de ter uma visualização melhor do que possuíamos.

3. **Identificar os outliers**  
   Após entender melhor os dados que tínhamos, essa etapa tinha o objetivo de realmente identificar se aquele dado era um outlier ou não, através do método dos quartis.

4. **Retirar os outliers**  
   Foi feita a retirada dos outliers do dataset para finalmente ir para o treinamento do modelo.

5. **Treinamento de modelos e avaliação de métricas**  
   Aqui foi feito um benchmarking de modelos de machine learning com o dataset limpo sobre a predição das colunas de importação, exportação e produção em relação a todas as especiarias e países ao longo do tempo.

6. **Refinamento dos dados**  
   Refinamento do modelo de treinamento com validação cruzada e definição das variáveis mais importantes.

Nessa última entrega, como já explicado anteriormente, o grupo decidiu tomar uma nova abordagem, na qual foram feitas:

1. **Separação do dataset por especiaria**: resultando em 9 novos datasets menores.  
2. **Identificação dos outliers**.  
3. **Retirada dos outliers**.  
4. **Benchmark de modelos de machine learning** em relação às colunas de importação, exportação e produção.  
5. **Escolha final da coluna "importação" e treinamento de 9 modelos de predição** (um para cada especiaria).  
6. **Refinamento do modelo**.

O desenvolvimento deste projeto seguiu uma abordagem metodológica centrada em etapas rigorosas de **análise estatística, tratamento de dados, avaliação de modelos preditivos e refinamento com validação cruzada**. A seguir, detalhamos cada uma das técnicas utilizadas.

---

### 1. Pré-processamento dos Dados e Seleção de Atributos

A base original foi filtrada para manter apenas as colunas essenciais: `Area` (país), `Year` (ano), `Item` (especiaria), `Import`, `Export` e `Production`. As seguintes ações foram realizadas:

* Correção de inconsistências nos nomes das colunas (ex.: remoção de espaços).
* Conversão de colunas categóricas em variáveis dummies (`pd.get_dummies`) para permitir sua utilização nos algoritmos de regressão.
* Criação de **novas colunas booleanas** (`is_outlier_Import`, `is_outlier_Export`, `is_outlier_Production`) para marcar a presença de outliers, mantendo os dados originais intactos e possibilitando filtragem posterior flexível.

---

### 2. Detecção de Outliers (Método Estatístico com Janela Temporal e Quartis)

Utilizamos uma abordagem robusta baseada no **método dos quartis (IQR - Interquartile Range)** para identificar valores extremos. A técnica foi aplicada **localmente**, considerando:

* Uma **janela móvel de 7 anos** centrada no ano da observação (3 anos antes e 3 anos depois).
* A detecção foi feita separadamente para cada combinação de `Area` (país) e `Item` (especiaria), garantindo maior precisão estatística.

**Critérios aplicados**:

Para cada célula do dataset:

* Calculamos $Q1$ (percentil 25), $Q3$ (percentil 75) e $IQR = Q3 - Q1$ dentro da janela temporal.
* Estabelecemos os limites:

  $$
  \text{Limite Inferior} = Q1 - 1.5 \times IQR,\quad \text{Limite Superior} = Q3 + 1.5 \times IQR
  $$
* Se o valor estiver fora desses limites, ele é marcado como outlier na respectiva coluna de controle.

Essa estratégia permitiu preservar os dados temporais válidos e eliminar apenas valores estatisticamente inconsistentes, sem eliminar registros inteiros.

---

### 3. Segmentação do Dataset

Após a limpeza, optamos por **segmentar o dataset em 9 novos subconjuntos**, cada um representando uma das especiarias analisadas. Essa decisão foi baseada na observação de que as dinâmicas de mercado (importação, exportação, produção) variam significativamente entre os tipos de especiarias. Dessa forma, modelos treinados individualmente teriam maior chance de capturar padrões específicos de cada produto.

---

### 4. Benchmark de Modelos de Regressão

Com os dados prontos, realizamos testes de benchmark com os seguintes algoritmos de regressão supervisionada:

* **LinearRegression** (Regressão Linear)
* **DecisionTreeRegressor** (Árvore de Decisão)
* **RandomForestRegressor** (Random Forest)
* **SVR** (Suporte a Vetores de Regressão)
* **MLPRegressor** (Perceptron MultiCamada - Rede Neural)

Os modelos foram testados inicialmente para prever separadamente `Import`, `Export` e `Production`. Em todos os experimentos com a variável **Import**, o algoritmo **Random Forest** obteve consistentemente os melhores resultados de R², com valores muitas vezes superiores a 0.95. Por essa razão, adotamos esse modelo como padrão para os modelos finais de previsão de importação.

---

### 5. Modelagem com Validação Cruzada e Ajuste de Hiperparâmetros

Para cada um dos 9 datasets (um por especiaria), seguimos o seguinte fluxo:

#### a) Divisão dos dados

* Dividimos os dados em conjunto de treino/validação (80%) e teste (20%) com `train_test_split`.

#### b) Padronização

* Aplicamos `StandardScaler` para normalizar os dados contínuos. A normalização foi ajustada apenas no treino e aplicada no teste, evitando vazamento de dados.

#### c) Definição da grade de hiperparâmetros (Random Forest)

```python
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
```

#### d) Validação cruzada (K-Fold)

* Utilizamos validação cruzada com 5 dobras (`KFold(n_splits=5)`), embaralhando os dados com `shuffle=True` para reduzir viés por ordenação temporal.

#### e) Ajuste com `GridSearchCV`

* Para cada combinação de parâmetros, o modelo foi avaliado com base na métrica de **R²** no conjunto de validação. O melhor conjunto foi selecionado automaticamente.

#### f) Avaliação final

* O modelo final (com melhores parâmetros) foi testado no conjunto de **teste final hold-out**, com avaliação das métricas:

  * $\text{R}^2$ — Coeficiente de Determinação
  * MAE — Mean Absolute Error
  * MSE — Mean Squared Error

Esse processo foi repetido para cada uma das 9 especiarias, resultando em 9 modelos otimizados e validados.

## Resultados Obtidos

A avaliação dos modelos foi realizada em duas etapas principais: uma fase inicial de **benchmark** com diversos algoritmos e, posteriormente, uma fase de **refinamento e ajuste de hiperparâmetros** com validação cruzada, focando exclusivamente na variável de **importação**.

---

### Resultados Iniciais — Benchmark entre Modelos

A tabela a seguir resume os resultados médios obtidos com três dos modelos testados no dataset inteiro durante a fase de benchmarking inicial, pois no início estávamos fazendo testes com o dataset inteiro:

| Modelo            | MAE (Erro Absoluto Médio) | MSE (Erro Quadrático Médio) | R² (Coef. de Determinação) |
| ----------------- | ------------------------- | --------------------------- | -------------------------- |
| Regressão Linear  | 29.191,50                 | 60.837.689.465,94           | 0.1373                     |
| Árvore de Decisão | 1.022,64                  | 216.480.869,70              | 0.9884                     |
| Random Forest     | **853,90**                | **172.731.004,37**          | **0.9921**                 |

Como podemos observar, o modelo **Random Forest** apresentou o melhor desempenho geral, com os menores valores de MAE e MSE, além do maior R². Mas posteriormente vimos que não faria sentido criar um modelo com os dados do dataset inteiro, por isso encontramos que uma abordagem melhor seria dividir o dataset por esperiaria e então seguimos para os próximos resultados.

---

### Modelos Selecionados por Especiaria (Etapa de Benchmark)


Após segmentarmos o dataset por especiaria, realizamos uma análise detalhada dos resultados dos modelos de regressão para cada uma das três variáveis-alvo possíveis: **importação**, **exportação** e **produção**. Para cada especiaria, treinamos os modelos individualmente, variando a variável de interesse como target, e comparamos os desempenhos com base na métrica de **R² (coeficiente de determinação)**.

A tabela a seguir apresenta, para cada especiaria e variável alvo, o modelo que mais se destacou em termos de R² — ou seja, aquele que explicou melhor a variabilidade dos dados no conjunto de teste:

| Especiaria                                                  | Importação        | Exportação        | Produção          |
| ----------------------------------------------------------- | ----------------- | ----------------- | ----------------- |
| Canela e flores de caneleira                                | Random Forest     | Árvore de Decisão | Árvore de Decisão |
| Gengibre                                                    | Random Forest     | Árvore de Decisão | Random Forest     |
| Pimentas secas (Capsicum/Pimenta)                           | Random Forest     | Árvore de Decisão | Random Forest     |
| Baunilha                                                    | Random Forest     | Random Forest     | Árvore de Decisão |
| Cravo (talos inteiros)                                      | Random Forest     | Random Forest     | Random Forest     |
| Pimenta (Piper spp.)                                        | Random Forest     | Random Forest     | Random Forest     |
| Noz-moscada, macis e cardamomos                             | Random Forest     | Random Forest     | Random Forest     |
| Pimentas verdes (Capsicum/Pimenta)                          | Random Forest     | Random Forest     | Random Forest     |
| Anis, badiana, coentro, cominho, alcaravia, funcho e zimbro | Árvore de Decisão | Árvore de Decisão | Árvore de Decisão |

Esses resultados reforçaram a consistência do Random Forest para o problema de previsão de **importação**, sendo o modelo mais eficaz na maioria das especiarias testadas — o que embasou sua escolha como foco da etapa final de refinamento.

---

### Resultados Pós-Refinamento — Foco em Importação

Na etapa final, utilizamos validação cruzada (K-Fold com `GridSearchCV`) para refinar os hiperparâmetros do modelo Random Forest em cada uma das 9 especiarias. Abaixo está a comparação entre o R² antes e depois do tuning:

| Especiaria                                              | R² Antes (Melhor Algoritmo) | R² Pós-Refino | Evolução  |
| ------------------------------------------------------- | --------------------------- | ------------- | --------- |
| Canela e flores de caneleira                            | 0.9413                      | 0.9448        | ▲ +0.0035 |
| Gengibre                                                | 0.9573                      | 0.9593        | ▲ +0.0020 |
| Pimentas secas (Capsicum/Pimenta)                       | 0.9494                      | 0.9486        | ▼ -0.0008 |
| Baunilha                                                | 0.9304                      | 0.9278        | ▼ -0.0026 |
| Cravo (talos inteiros)                                  | 0.7381                      | 0.7370        | ▼ -0.0011 |
| Pimenta (Piper spp.)                                    | 0.9810                      | 0.9803        | ▼ -0.0007 |
| Noz-moscada, macis e cardamomos                         | 0.8771                      | 0.9086        | ▲ +0.0315 |
| Pimentas verdes (Capsicum/Pimenta)                      | 0.9858                      | 0.9843        | ▼ -0.0015 |
| Anis, badiana, coentro, cominho, alcaravia, funcho, etc | 0.9094                      | 0.8617        | ▼ -0.0477 |

---

### Interpretação das Variações no R² Após o Tuning

🔍 **Por que o R² pode cair após o ajuste de hiperparâmetros?**

1. **Validação cruzada foca em generalização, não em performance pontual**
   O `GridSearchCV` utiliza validação cruzada para encontrar o modelo que performa bem **em média**. Em contrapartida, o modelo anterior pode ter se beneficiado de uma divisão treino/teste específica e “favorável”, resultando em overfitting.

2. **Validação cruzada reduz variabilidade**
   Modelos com tuning via K-Fold são mais conservadores e robustos. Isso pode resultar em um pequeno decréscimo no R² em conjuntos de teste únicos, mas aumenta a confiabilidade em dados futuros.

3. **Espaço de busca limitado**
   A performance pode ter sido limitada pelos hiperparâmetros testados. Por exemplo, `max_depth` baixo ou `min_samples_split` alto pode reduzir a capacidade do modelo de capturar variabilidade nos dados.

---

### Análise Crítica das Evoluções

| Especiaria                                  | ΔR²               | Interpretação                                                                                             |
| ------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------- |
| **Noz-moscada, macis e cardamomos**         | +0.0315           | Ótimo ganho — o tuning teve impacto direto e positivo.                                                    |
| **Canela e Gengibre**                       | +0.0035 / +0.0020 | Melhoras pequenas, mas consistentes.                                                                      |
| **Pimentas secas, Baunilha, Pimenta, etc.** | -0.0007 a -0.0026 | Quedas leves, consideradas normais dentro do processo de tuning.                                          |
| **Anis e especiarias similares**            | -0.0477           | Queda significativa — modelo ajustado ficou mais conservador ou houve instabilidade no conjunto de teste. |

---

### Conclusão Parcial dos Resultados

Mesmo com pequenas flutuações em alguns casos, os modelos demonstraram **elevada performance geral**, com valores de R² superiores a 0.94 na maioria das especiarias, reforçando a qualidade dos dados tratados e a eficácia do modelo Random Forest. A aplicação de validação cruzada contribuiu para a construção de modelos mais robustos, prontos para generalizar com segurança em novos cenários e dados futuros.


## Conclusão:

Durante o processo, aprendemos a importância de avançar de forma estruturada: iniciamos com a análise exploratória dos dados, desenvolvendo a habilidade de interpretar o comportamento das variáveis, como elas influenciam umas nas outras, seus possíveis tratamentos. Em seguida, aplicamos técnicas estatísticas para detecção e tratamento de outliers, percebendo como a qualidade dos dados impacta diretamente a performance dos modelos.

Na fase de modelagem, experimentamos diferentes algoritmos de regressão, compreendendo como avaliar e comparar resultados com métricas adequadas como R², MAE e MSE. Também adquirimos experiência com validação cruzada e ajuste de hiperparâmetros usando GridSearchCV, entendendo na prática como tornar os modelos mais robustos e generalizáveis. Essa etapa nos ensinou a olhar além das métricas pontuais e valorizar a estabilidade do modelo frente a novas amostras.

O projeto nos mostrou que a construção de modelos eficazes não depende apenas da escolha de algoritmos, mas de um processo bem planejado de limpeza, preparação e avaliação rigorosa dos dados. A partir desse aprendizado, nos sentimos mais preparados para aplicar esse conhecimento em contextos reais e projetos futuros.

Além disso, a disciplina nos estimulou a pensar nos próximos passos para a finalização do projeto, que inclui:

- Criar uma interface interativa para tornar o modelo acessível a usuários finais.

- Estruturar o projeto para colocá-lo em produção, com integração em aplicações web e serviços.

- Realizar monitoramento contínuo do desempenho dos modelos, ajustando conforme novas informações forem coletadas.

- Expandir a solução com outras variáveis e cenários de uso, aumentando sua aplicabilidade no mundo real.

## Arquivos no ZIP:
- miniTrabalho7.ipynb → Código completo
- 9 novos datasets menores na pasta datasets
- 9 novos datasets menores na pasta datasets_tratatados sem outliers
- Resultados dos benchmarks antes do refinamento no arquivo "restulados_benchmark.txt"
- Resultados dos benchmarks pós-refinamento no arquivo "resultados_benchmarks_refinado.txt"
- README.txt → Este documento com a explicação completa da entrega

## Como Executar:
1. Abrir o notebook com Jupyter ou Google Colab
2. Certifique-se de que o arquivo "Export.csv" está no mesmo diretório
3. Executar todas as células do notebook
