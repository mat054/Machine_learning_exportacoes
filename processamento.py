#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Processamento de Dados - Consumo Global de Especiarias
Este script realiza a limpeza e preparação dos dados brutos da FAOSTAT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados brutos da FAOSTAT
    
    Parameters:
    -----------
    caminho_arquivo : str
        Caminho para o arquivo CSV com os dados brutos
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame com os dados carregados
    """
    print(f"Carregando dados de: {caminho_arquivo}")
    return pd.read_csv(caminho_arquivo)

def limpar_dados(df):
    """
    Realiza limpeza e transformações básicas nos dados
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame com os dados brutos
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame com os dados limpos
    """
    print("Iniciando limpeza de dados...")
    
    # Cria cópia para não modificar os dados originais
    df_limpo = df.copy()
    
    # Renomeia colunas (se necessário)
    # df_limpo = df_limpo.rename(columns={'nome_antigo': 'nome_novo'})
    
    # Converte colunas para tipos apropriados
    colunas_numericas = ['Producao', 'Importacao', 'Exportacao', 'Consumo_Estimado']
    for col in colunas_numericas:
        if col in df_limpo.columns:
            df_limpo[col] = pd.to_numeric(df_limpo[col], errors='coerce')
    
    # Trata valores ausentes
    print(f"Valores nulos antes da limpeza: {df_limpo.isna().sum().sum()}")
    
    # Estratégia 1: Preencher valores ausentes com zero (para dados de comércio)
    for col in ['Importacao', 'Exportacao']:
        if col in df_limpo.columns:
            df_limpo[col] = df_limpo[col].fillna(0)
    
    # Estratégia 2: Remover linhas com valores ausentes em colunas críticas
    colunas_criticas = ['Pais', 'Ano', 'Producao']
    df_limpo = df_limpo.dropna(subset=[col for col in colunas_criticas if col in df_limpo.columns])
    
    print(f"Valores nulos após limpeza: {df_limpo.isna().sum().sum()}")
    
    # Calcula o consumo estimado (se não existir)
    if 'Consumo_Estimado' not in df_limpo.columns and all(col in df_limpo.columns for col in ['Producao', 'Importacao', 'Exportacao']):
        print("Calculando consumo estimado...")
        df_limpo['Consumo_Estimado'] = df_limpo['Producao'] + df_limpo['Importacao'] - df_limpo['Exportacao']
        
        # Corrige valores negativos no consumo (improvável na prática, pode indicar armazenamento)
        df_limpo['Consumo_Estimado'] = df_limpo['Consumo_Estimado'].clip(lower=0)
    
    print("Limpeza de dados concluída.")
    return df_limpo

def salvar_dados_processados(df, caminho_saida):
    """
    Salva os dados processados em um arquivo CSV
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame com os dados processados
    caminho_saida : str
        Caminho para salvar o arquivo CSV
    """
    diretorio = os.path.dirname(caminho_saida)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    df.to_csv(caminho_saida, index=False, encoding='utf-8')
    print(f"Dados processados salvos em: {caminho_saida}")

def gerar_visualizacoes_basicas(df, diretorio_saida='visualizacoes'):
    """
    Gera visualizações básicas dos dados processados
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame com os dados processados
    diretorio_saida : str
        Diretório para salvar as visualizações geradas
    """
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    
    print("Gerando visualizações básicas...")
    
    # Configurações para os gráficos
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    
    # 1. Consumo total por especiaria
    if all(col in df.columns for col in ['Item', 'Consumo_Estimado']):
        plt.figure()
        consumo_por_especiaria = df.groupby('Item')['Consumo_Estimado'].sum().sort_values(ascending=False)
        consumo_por_especiaria.plot(kind='bar', color='teal')
        plt.title('Consumo Total por Especiaria')
        plt.ylabel('Consumo Estimado (toneladas)')
        plt.xlabel('Especiaria')
        plt.tight_layout()
        plt.savefig(f"{diretorio_saida}/consumo_por_especiaria.png", dpi=300)
        plt.close()
    
    # 2. Tendência de consumo ao longo do tempo
    if all(col in df.columns for col in ['Ano', 'Consumo_Estimado']):
        plt.figure()
        tendencia_temporal = df.groupby('Ano')['Consumo_Estimado'].sum()
        tendencia_temporal.plot(kind='line', marker='o', color='darkorange')
        plt.title('Tendência de Consumo Global ao Longo do Tempo')
        plt.ylabel('Consumo Estimado (toneladas)')
        plt.xlabel('Ano')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{diretorio_saida}/tendencia_temporal.png", dpi=300)
        plt.close()
    
    # 3. Top 10 países consumidores
    if all(col in df.columns for col in ['Pais', 'Consumo_Estimado']):
        plt.figure()
        top_paises = df.groupby('Pais')['Consumo_Estimado'].sum().sort_values(ascending=False).head(10)
        top_paises.plot(kind='barh', color='seagreen')
        plt.title('Top 10 Países Consumidores de Especiarias')
        plt.xlabel('Consumo Estimado (toneladas)')
        plt.ylabel('País')
        plt.tight_layout()
        plt.savefig(f"{diretorio_saida}/top_paises_consumidores.png", dpi=300)
        plt.close()
    
    print(f"Visualizações salvas no diretório: {diretorio_saida}")

def main():
    """Função principal para execução do script"""
    # Definir caminhos
    caminho_entrada = 'dados_brutos/faostat_especiarias.csv'
    caminho_saida = 'dados_especiarias.csv'
    
    try:
        # Carregar dados
        dados_brutos = carregar_dados(caminho_entrada)
        
        # Processar dados
        dados_processados = limpar_dados(dados_brutos)
        
        # Salvar dados processados
        salvar_dados_processados(dados_processados, caminho_saida)
        
        # Gerar visualizações
        gerar_visualizacoes_basicas(dados_processados)
        
        print("Processamento concluído com sucesso!")
        
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado: {caminho_entrada}")
        print("Por favor, verifique se o arquivo existe e tente novamente.")
    except Exception as e:
        print(f"ERRO durante o processamento: {str(e)}")

if __name__ == "__main__":
    main() 