# AQUISIÇÃO DE DADOS: CONSUMO GLOBAL DE ESPECIARIAS

## Mini Trabalho 4 - Aprendizado de Máquina

### Equipe
- Daniela Soares de Oliveira - 180015222
- Gabriel Freitas Balbino - 180075462
- Giovanni Alvissus Camargo Giampauli - 211043647
- Mateus de Castro Santos - 222015195
- Pablo Santos Costa - 180128817
- Pedro Lucas Dourado Santos - 211039680

## Descrição do Trabalho Realizado
Nessa entrega, os membros do grupo realizaram os primeiros testes em modelos que mais se adequam ao nosso objetivo de prever o consumo de uma especiaria, dado um país em relação ao tempo. Com isso podemos analisar e escolher o modelo com um melhor desempenho dado as métricas (MAE - Mean Absolute Error, MSE - Mean Squared Error e R² - Coeficiente de Determinação), tempo de inferência, facilidade na manutenção e maior interpretabilidade dos resultados.

### Nossos objetivos com a ecolha do modelo
Depois de entender nosso problema, seguimos os seguintes passos:

1. Entender o nosso problema(Já realizado em tarefas anteriores)
2. Preparação dos dados(Já realizado em tarefas anteriores)
3. Separação dos dados para treino/validação(80% treino, 20% validação ou validação cruzada)
4. Modelo Base(Regressao Linear ou media dos valores)
5. Teste de diferentes modelos:
    *5.1. Regressão Linear
    *5.2. Árvore de Decisão
    *5.3. Random Forest
    *5.4. SVM
    *5.5. Rede Neural (MLP)
6. Avaliação do desempenho
7. Comparação de modelos


### Modelos Selecionados

Explicar porque escolhemos cada modelo, codigo, etc

### Processo e Resultados

No nosso projeto, inicialmente particionamos os conjuntos de dados por país e especiaria, conforme mostrado no primeiro trecho de código. Essa abordagem nos permitiu gerar um resultado de modelo de aprendizado de máquina para cada um desses conjuntos de dados. O código itera sobre diferentes dataframes, cada um representando uma combinação específica de país e especiaria, e aplica vários modelos, como Regressão Linear, Árvore de Decisão, Random Forest, SVM e MLP Regressor. Os resultados de cada modelo foram avaliados usando métricas como MAE, MSE e R².

No segundo trecho de código, optamos por usar o conjunto de dados inteiro sem particionamento. Essa abordagem foi escolhida por sua simplicidade e eficiência. O conjunto de dados foi pré-processado removendo espaços dos nomes das colunas e convertendo variáveis categóricas em variáveis dummy. Em seguida, dividimos os dados em conjuntos de treinamento e teste e aplicamos o mesmo conjunto de modelos. Os resultados desses modelos, conforme mostrado na imagem, foram avaliados usando as mesmas métricas.

Os resultados da segunda abordagem foram mais consistentes e fáceis de gerenciar, levando-nos a escolher esse método para nossa análise final. As métricas de desempenho para cada modelo são exibidas na imagem, fornecendo uma comparação clara de sua eficácia na previsão do consumo de especiarias.

### Resultados Obtidos

Os resultados obtidos dos modelos são os seguintes:

- **Regressão Linear**
  - MAE: 29176.33
  - MSE: 60836985523.53
  - R²: 0.137

- **Árvore de Decisão**
  - MAE: 1022.64
  - MSE: 216480869.70
  - R²: 0.985

- **Random Forest**
  - MAE: 863.49
  - MSE: 188633299.79
  - R²: 0.991

- **Rede Neural (MLP)**
  - MAE: 2229.01
  - MSE: 5661595289.33
  - R²: 0.188

Esses resultados destacam a eficácia dos modelos de Árvore de Decisão e Random Forest em nossa análise.




