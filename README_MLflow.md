# Integração MLflow - Experimentos de Machine Learning com Especiarias

Este projeto implementa uma integração completa com MLflow baseada no `miniTrabalho7.ipynb`, permitindo rastreamento, versionamento e comparação de experimentos de machine learning para predição de dados de especiarias.

## Estrutura do Projeto

```
Machine_learning_exportacoes/
├── mlflow.py                    # Script principal com integração MLflow
├── run_mlflow_experiments.py    # Script wrapper para facilitar execução
├── requirements_mlflow.txt      # Dependências necessárias
├── README_MLflow.md            # Este arquivo
├── datasets/                   # Datasets originais
├── datasets_tratados/          # Datasets pré-processados
└── mlflow.db                  # Banco de dados SQLite do MLflow (criado automaticamente)
```

## Como Executar

### Opção 1: Script Interativo (Recomendado)
```bash
python run_mlflow_experiments.py
```

Este script oferece um menu interativo com as seguintes opções:
1. **Instalar dependências** - Instala todas as bibliotecas necessárias
2. **Executar experimentos** - Roda todos os experimentos MLflow
3. **Iniciar MLflow UI** - Abre a interface web do MLflow
4. **Executar tudo** - Combina instalação + experimentos + UI
5. **Sair**

### Opção 2: Execução Direta
```bash
# Instalar dependências
pip install -r requirements_mlflow.txt

# Executar experimentos
python mlflow.py

# Iniciar interface web
mlflow ui
```

## Experimentos Implementados

### 1. Benchmark de Modelos
Para cada especiaria e target (Import, Export, Production), testa:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **Support Vector Regression (SVR)**

**Métricas rastreadas:**
- R² (Coeficiente de Determinação)
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

### 2. Refinamento com GridSearchCV
Para cada especiaria (target: Import), executa:
- **Random Forest** com otimização de hiperparâmetros
- **K-Fold Cross Validation** (5 folds)
- **Grade de hiperparâmetros:**
  - `n_estimators`: [100, 200]
  - `max_depth`: [None, 10, 20]
  - `min_samples_split`: [2, 5]

## Visualizando Resultados

### Interface Web MLflow
Após executar os experimentos, acesse: `http://localhost:5000`

**Recursos disponíveis:**
- Comparação de métricas entre experimentos
- Filtros por parâmetros e métricas
- Gráficos de evolução de métricas
- Download de modelos treinados
- Logs detalhados de cada execução

### Arquivo de Resultados
O script gera `mlflow_results.txt` com:
- Resumo dos melhores modelos por especiaria
- Comparação de performance antes/depois do refinamento
- Hiperparâmetros otimizados

## Estrutura dos Dados

### Pré-processamento
- Remoção de outliers (colunas `is_outlier_*`)
- Seleção de features relevantes
- One-hot encoding para variáveis categóricas
- Padronização com StandardScaler

### Features Utilizadas
- **Area**: País/região (one-hot encoded)
- **Year**: Ano dos dados
- **Item**: Tipo de especiaria (one-hot encoded)
- **Targets**: Import, Export, Production

## Especiarias Analisadas

1. **Canela e flores de caneleira**
2. **Gengibre**
3. **Pimentas secas (Capsicum/Pimenta)**
4. **Baunilha**
5. **Cravo (talos inteiros)**
6. **Pimenta (Piper spp.)**
7. **Noz-moscada, macis e cardamomos**
8. **Pimentas verdes (Capsicum/Pimenta)**
9. **Anis, badiana, coentro, cominho, alcaravia, funcho e zimbro**

## Principais Descobertas (do miniTrabalho7)

### Benchmark Results
- **Random Forest** foi o algoritmo mais consistente
- **SVR** apresentou desempenho inferior em todos os cenários
- **Árvore de Decisão** se destacou em alguns casos específicos

### Refinamento Results
- Melhora significativa para **Noz-moscada** (+0.0315 R²)
- Estabilidade para maioria das especiarias
- Hiperparâmetros otimizados variam por dataset

## Dependências

- `mlflow>=2.8.0` - Rastreamento de experimentos
- `pandas>=1.5.0` - Manipulação de dados
- `numpy>=1.24.0` - Computação numérica
- `scikit-learn>=1.3.0` - Algoritmos de ML
- `scipy>=1.10.0` - Funções científicas
- `matplotlib>=3.7.0` - Visualização
- `seaborn>=0.12.0` - Visualização estatística

## Configuração MLflow

- **Tracking URI**: `sqlite:///mlflow.db` (banco local)
- **Experiment**: `spice_prediction_models`
- **Runs**: Organizados por especiaria, target e modelo

## Logs e Rastreamento

Cada experimento registra:
- **Parâmetros**: Configurações do modelo e dados
- **Métricas**: Performance em tempo real
- **Artefatos**: Modelos treinados
- **Tags**: Metadados para organização

## Troubleshooting

### Erro: "Diretório 'datasets' não encontrado"
- Certifique-se de estar no diretório `Machine_learning_exportacoes/`
- Verifique se a pasta `datasets/` existe

### Erro: "ModuleNotFoundError: No module named 'mlflow'"
- Execute: `pip install -r requirements_mlflow.txt`

### MLflow UI não inicia
- Verifique se a porta 5000 está livre
- Tente: `mlflow ui --port 5001`

## Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme se os datasets estão no local correto
3. Execute o script com `python run_mlflow_experiments.py`

---

**Baseado no miniTrabalho7.ipynb** - Experimentos de Machine Learning para Predição de Dados de Especiarias 