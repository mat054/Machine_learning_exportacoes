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
Nessa entrega, os membros do grupo realizaram a exclusão dos dados nulos(O dataset já estava limpo com a ausência desses dados), Seleção de colunas mais relevantes para o trabalho e identificação de outliers baseado em um pais e especiaria ao longo do tempo (1999 ate 2022) em relaçao com a Importação, Exportação. Produção ou Consumo

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

### Colunas Selecionadas

As colunas que o grupo selecionou foram:

- **País** – O país onde os dados de produção e comércio são registrados.
- **Ano** – O ano da coleta de dados (ex.: 2000–2023).
- **Item** - Podendo ser uma dos 9 tipos de especiarias descritas anteriormente.
- **Produção (toneladas)** – A quantidade total de especiarias produzidas em um país.
- **Importação (toneladas)** – A quantidade importada para o país.
- **Exportação (toneladas)** – A quantidade exportada do país.
- **Consumo Estimado (toneladas)** – O consumo doméstico final calculado.



## Estrutura de Arquivos

- `dados_especiarias.csv` - Dataset principal com todos os dados de consumo de especiarias
- `analise_preliminar.ipynb` - Notebook Jupyter com análise exploratória inicial dos dados
- `processamento.py` - Script Python utilizado para limpeza e preparação dos dados
- `visualizacoes/` - Diretório contendo gráficos e visualizações gerados a partir dos dados
- `miniTrabalho4.ipynb` - Trabalho realizado para a mini entrega 4
- 
## Explicação do código

O código fornecido realiza a detecção de outliers em um conjunto de dados de especiarias, considerando as colunas de produção, importação, exportação e consumo. Para cada país e especiaria, o código:

1. Filtra os dados para os 10 países com mais registros e para cada tipo de especiaria.
2. Para cada coluna numérica (exceto o ano), calcula os outliers usando o método de quartis com uma janela de 3 anos para cada lado do ano central.
3. Marca os valores como outliers se estiverem fora dos limites calculados (1.5 vezes o intervalo interquartil além dos quartis).
4. Armazena os dataframes processados e visualiza os dados, destacando os outliers em vermelho.
5. Finalmente, concatena todos os dataframes processados e salva o resultado em um arquivo CSV, se houver dados processados.



