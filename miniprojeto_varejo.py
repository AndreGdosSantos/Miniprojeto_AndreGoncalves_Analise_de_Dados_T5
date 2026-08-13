import csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open('Base Varejo.csv','r', encoding='utf-8') as arquivo:
    todas_vendas = list(csv.DictReader(arquivo, delimiter=';'))

print(todas_vendas[0])  # Exibe o primeiro registro 
    
    
    
