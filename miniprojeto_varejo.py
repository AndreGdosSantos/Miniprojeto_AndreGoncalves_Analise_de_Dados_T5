# Miniprojeto de Análise de Dados - T05
# Aluno: André Gonçalves dos Santos
# Data: 13/08/2026
# link da base de dados utilizado: https://www.kaggle.com/datasets/namespaiva/base-varejo/data


# --- Etapa 1: Carregamento a base de dados ---

import csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open('Base Varejo.csv','r', encoding='utf-8') as arquivo:
    todas_vendas = list(csv.DictReader(arquivo, delimiter=';'))

print(todas_vendas[0])  # Exibe o primeiro registro do arquivo CSV como um dicionário
    
# --- Etapa 1: Leitura dos dados ---  
df = pd.read_csv('Base Varejo.csv', sep=';', encoding='utf-8')

print(f'Número de linhas: {df.shape[0]}') # df.shape[0] retorna o número de linhas do DataFrame
print(f'Número de colunas: {df.shape[1]}')  # df.shape[1] retorna o número de colunas do DataFrame
print(f'\nColunas e tipos de dados: \n{df.dtypes}')  # df.dtypes exibe as colunas e seus tipos de dados
print(f'\nPrimeiras linhas: \n{df.head()}') # df.head() Exibe as primeiras linhas do DataFrame
print(f'\nÚltimas linhas: \n{df.tail()}')  # df.tail() Exibe as últimas linhas do DataFrame

# --- Etapa 2: Limpeza e Tratamento dos Dados ---   

colunas_validas = [c for c in df.columns if 'Unnamed' not in c]  # Remove colunas com 'unnamed' que estão vazias
df = df[colunas_validas]  # Mantém apenas as colunas válidas

print(df.columns)   # Exibe as colunas do DataFrame após a limpeza
print(df.head())  

df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria') # Preenche valores nulos na coluna PR_CAT com 'Sem Categoria'
print(f'Valores nulos na coluna PR_CAT: {df["PR_CAT"].isnull().sum()}')  # Verifica se ainda existem valores nulos na coluna PR_CAT

df = df.drop_duplicates() # Remove linhas duplicadas do DataFrame
print("Linhas duplicadas removidas!")

df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y') # Converte a coluna 'DATA' para o tipo datetime
print("Coluna DATA convertida para datetime!")

df = df.rename(
    columns={'DATA': 'Data',
        'CO_ID': 'id_compra',
        'CL_ID': 'id_cliente',
        'CL_GENERO': 'genero',
        'CL_EC': 'estado_civil',
        'CL_FHL': 'numero_filhos',
        'CL_SEG': 'segmento_cliente',
        'PR_ID': 'id_produto',
        'PR_CAT': 'categoria_produto',
        'PR_NOME': 'nome_produto',
    }
) # Renomeia as colunas do DataFrame para nomes mais entendíveis
print(df.columns)

