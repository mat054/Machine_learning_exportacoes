# Teste de Modelos de Aprendizado de Máquina

## Mini Trabalho 5 - Otimização e Ajuste Fino do Sistema

### Equipe
- Daniela Soares de Oliveira - 180015222
- Gabriel Freitas Balbino - 180075462
- Mateus de Castro Santos - 222015195
- Pablo Santos Costa - 180128817
- Pedro Lucas Dourado Santos - 211039680

Descrição do Trabalho Realizado:
Este mini trabalho teve como foco a otimização e ajuste fino do modelo de Machine Learning previamente escolhido — o Random Forest Regressor. O objetivo foi melhorar o desempenho do modelo por meio da calibração de hiperparâmetros e da aplicação de técnicas de validação cruzada, com vistas a evitar overfitting e obter melhores previsões.

## Processo e Resultados:
- Os dados foram inicialmente pré-processados: renomeação de colunas, aplicação de get_dummies em variáveis categóricas e normalização dos dados.
- Utilizamos o método GridSearchCV com validação cruzada (KFold com 5 splits) para encontrar os melhores hiperparâmetros do modelo Random Forest.
- Após o ajuste fino, o melhor modelo foi reavaliado com as métricas MAE, MSE e R².
- Também realizamos a validação cruzada para verificar a estabilidade do modelo e extraímos a importância das variáveis para análise de interpretabilidade.

## Resultados Obtidos:
- Hiperparâmetros otimizados: 'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200
  
- Desempenho do modelo otimizado:
  - MAE: 863.6892240025726
  - MSE: 183266260.5217053
  - R²: 0.9919004838885606
- R² médio da validação cruzada: 0.990460091003964

O modelo demonstrou um desempenho superior ao modelo inicial, confirmando a eficácia da otimização.

## Conclusão:

Mesmo que a diferença no MAE seja quase imperceptível, as vantagens do modelo novo no MSE e no R² (além da validação cruzada) sugerem que ele lida melhor com erros mais extremos e possui uma performance um pouco mais consistente. Em outras palavras, os erros de alta magnitude (potencialmente outliers) impactam menos o modelo novo, o que pode ser importante dependendo do contexto.

Diante desses pontos, o modelo apresenta uma leve eficiência superior ao anterior, principalmente por um MSE inferior e um R² um pouco mais alto, além de demonstrar consistência na validação cruzada. As diferenças são muito sutis, e na prática ambos os modelos podem ser considerados altamente eficientes.

Através da técnica de ajuste fino com GridSearchCV e validação cruzada, conseguimos melhorar o desempenho do modelo Random Forest para previsão de produção, importação e exportação de especiarias. O modelo final é mais robusto, generaliza melhor nos dados de teste e é capaz de capturar padrões relevantes com maior precisão. Isso o torna adequado para ser utilizado em análises preditivas e apoio à tomada de decisão em contextos comerciais ou agrícolas.

![grafico](importância%20das%20Variáveis.png)


## Arquivos no ZIP:
- miniTrabalho6.ipynb → Código completo com otimização e análise
- README.txt → Este documento

## Como Executar:
1. Abrir o notebook com Jupyter ou Google Colab
2. Certifique-se de que o arquivo "Export.csv" está no mesmo diretório
3. Executar todas as células do notebook
