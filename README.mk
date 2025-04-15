# AQUISIÇÃO DE DADOS: CONSUMO GLOBAL DE ESPECIARIAS
## Mini Trabalho 2 - Aprendizado de Máquina

### Equipe
- [Nome do Membro 1]
- [Nome do Membro 2]
- [Nome do Membro 3]
- [Nome do Membro 4]

## Descrição do Dataset

Este projeto apresenta uma análise abrangente do consumo global de especiarias, compilada utilizando dados da FAOSTAT. O consumo de especiarias é estimado aplicando a fórmula:

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

## Estrutura de Arquivos

- `dados_especiarias.csv` - Dataset principal com todos os dados de consumo de especiarias
- `analise_preliminar.ipynb` - Notebook Jupyter com análise exploratória inicial dos dados
- `processamento.py` - Script Python utilizado para limpeza e preparação dos dados
- `visualizacoes/` - Diretório contendo gráficos e visualizações gerados a partir dos dados

## Instruções de Uso

1. **Requisitos de Ambiente**:
   - Python 3.8+
   - Pandas 1.3+
   - Matplotlib 3.4+
   - Seaborn 0.11+
   - Jupyter Notebook (opcional para execução do arquivo de análise)

2. **Instalação de Dependências**:
   ```
   pip install -r requirements.txt
   ```

3. **Carregamento dos Dados**:
   ```python
   import pandas as pd
   dados = pd.read_csv('dados_especiarias.csv')
   ```

4. **Exemplo de Análise Básica**:
   ```python
   # Visualizar estatísticas descritivas
   print(dados.describe())
   
   # Consumo por país (top 10)
   consumo_por_pais = dados.groupby('Pais')['Consumo_Estimado'].sum().sort_values(ascending=False).head(10)
   print(consumo_por_pais)
   ```

## Problemas Conhecidos e Limitações

- Alguns países podem ter dados incompletos para determinados anos
- A fórmula de consumo assume que não há armazenamento significativo entre anos
- Dados anteriores a 2000 podem ter menor confiabilidade devido a métodos de coleta menos precisos

## Futuras Melhorias

- Incorporação de dados demográficos para análise per capita
- Inclusão de dados de preço para análise econômica mais abrangente
- Expansão para incluir mais variedades de especiarias 