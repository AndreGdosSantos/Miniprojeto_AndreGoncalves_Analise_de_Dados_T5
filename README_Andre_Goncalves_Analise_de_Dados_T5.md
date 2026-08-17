# Análise Exploratória de Dados - Varejo

**Aluno:** André Gonçalves dos Santos
**Turma:** Análise de Dados Turma 05

## Sobre o Projeto e Reflexão Teórica (ETL)
Este projeto consiste em uma Análise Exploratória de Dados (AED) aplicada a uma base de varejo. O objetivo principal foi praticar processos de ETL (Extração, Transformação e Limpeza) e garantir a qualidade dos dados antes de qualquer análise profunda. A etapa de limpeza é fundamental no dia a dia de dados, pois bases com valores nulos, duplicatas ou tipos incorretos podem gerar métricas distorcidas e decisões de negócio equivocadas. 

## Como executar o projeto
1. Baixe os arquivos deste repositório.
2. Certifique-se de ter o Python e a biblioteca Pandas instalados.
3. Abra o arquivo `miniprojeto_varejo.py` no VsCode ou Google Colab.
4. Rode o script no terminal para visualizar os resultados das análises, estatísticas e o relatório de limpeza.

## Principais Insights da Análise
* **Perfil Familiar:** A grande maioria dos clientes da base não possui filhos (mediana e moda iguais a 0).
* **Força Feminina:** O público feminino realiza a maior quantidade de compras no varejo.
* **Categoria Campeã:** O setor de "ALIMENTOS" é o carro-chefe isolado das vendas, representando mais da metade de todas as transações da base.
* **Qualidade dos Dados Brutos:** A base original apresentou mais de 96 mil registros duplicados e mais de 3 mil produtos sem categoria definida, evidenciando a extrema necessidade da etapa de transformação e limpeza.