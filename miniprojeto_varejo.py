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
    
# --- Etapa 2: Leitura dos dados ---  
df = pd.read_csv('Base Varejo.csv', sep=';', encoding='utf-8')

print(f'Número de linhas: {df.shape[0]}') # df.shape[0] retorna o número de linhas do DataFrame
print(f'Número de colunas: {df.shape[1]}')  # df.shape[1] retorna o número de colunas do DataFrame
print(f'\nColunas e tipos de dados: \n{df.dtypes}')  # df.dtypes exibe as colunas e seus tipos de dados
print(f'\nPrimeiras linhas: \n{df.head()}') # df.head() Exibe as primeiras linhas do DataFrame
print(f'\nÚltimas linhas: \n{df.tail()}')  # df.tail() Exibe as últimas linhas do DataFrame

# --- Etapa 3: Limpeza e Tratamento dos Dados ---   

print("\nValores nulos por coluna:") # Exibe a contagem de valores nulos por coluna
print(df.isnull().sum())

duplicatas = df.duplicated().sum() # .duplicated().sum() Conta o número de linhas duplicadas no DataFrame
print(f"\nLinhas duplicadas encontradas: {duplicatas}")

df = df.drop_duplicates() # Remove linhas duplicadas do DataFrame
print("Linhas duplicadas removidas com sucesso!")

inconsistencias = df['PR_CAT'].isin(['', '#N/D']).sum() # .isin(['', '#N/D']).sum() Conta o número de registros com categoria de produto vazia ou '#N/D'
print(f"\nRegistros com categoria de produto vazia ou '#N/D': {inconsistencias}")

colunas_validas = [c for c in df.columns if 'Unnamed' not in c]  # Remove colunas com 'unnamed' que estão vazias
df = df[colunas_validas]  # Mantém apenas as colunas válidas

print("\n--- Justificativa da Limpeza ---")
print("1. As colunas 'Unnamed' foram removidas pois eram nulas na base original.")
print("2. Os valores nulos e '#N/D' na categoria de produtos foram substituídos por 'Sem Categoria' para não perdermos os registros.")

print(f"\nColunas do DataFrame após a limpeza:\n{df.columns}")   # Exibe as colunas do DataFrame após a limpeza
print(f"\nPrimeiras 5 linhas após a limpeza:\n{df.head()}")  

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

if df['categoria_produto'].isnull().sum() > 0: # Verifica se existem valores nulos na coluna 'categoria_produto'
    df['categoria_produto'] = df['categoria_produto'].fillna('Sem Categoria')

df['categoria_produto'] = df['categoria_produto'].replace('#N/D', 'Sem Categoria') # Substitui valores '#N/D' na coluna 'categoria_produto' por 'Sem Categoria'

print("\nValores nulos por coluna:")
print(df.isnull().sum()) # Exibe a contagem de valores nulos por coluna após o tratamento

df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y') # Converte a coluna 'Data' para o tipo datetime
print("Coluna Data convertida para datetime!")

# --- Etapa 4: ESTATÍSTICA DESCRITIVA: NÚMERO DE FILHOS ---

print("Média de filhos:", round(df['numero_filhos'].mean(), 2)) # .mean() Calcula a média do número de filhos
print("Mediana:", df['numero_filhos'].median()) # .median() Calcula a mediana do número de filhos
print("Moda:", df['numero_filhos'].mode()[0]) # .mode()[0] Calcula a moda do número de filhos (o valor mais frequente)
print("Desvio Padrão:", round(df['numero_filhos'].std(), 2)) # .std() Calcula o desvio padrão do número de filhos
print("Mínimo:", df['numero_filhos'].min()) # .min() Calcula o valor mínimo do número de filhos
print("Máximo:", df['numero_filhos'].max()) # .max() Calcula o valor máximo do número de filhos
print("Total de registros:", df['numero_filhos'].count()) # .count() Calcula o total de registros do número de filhos
print("\nQuartis (25%, 50%, 75%):\n", df['numero_filhos'].quantile([0.25, 0.50, 0.75])) # .quantile() Calcula os quartis do número de filhos

# --- Etapa 5: Agrupamentos de Dados ---

print("\n1. Compras por Gênero:\n", df.groupby('genero')['id_compra'].count())
print("\n2. Compras por Categoria:\n", df.groupby('categoria_produto')['id_compra'].count())

print("\nAgrupamento cruzado (Gênero e Categoria):")
analise = df.groupby(['genero', 'categoria_produto']).size().sort_values(ascending=False)
print(analise)


print(" CONCLUSÕES DA ANÁLISE")
print("1. A grande maioria dos clientes não possui filhos (Mediana e Moda = 0).")
print("2. O público feminino realiza um volume levemente maior de compras do que o masculino.")
print("3. A categoria 'ALIMENTOS' disparada é a mais vendida.")
print("4. Havia um número grande de registros duplicados que precisaram ser removidos para não interferir nas análises.")
print("5. Existem algumas compras sem categoria definida que requerem atenção do time de cadastro.")