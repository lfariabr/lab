
import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("Sales Page")

# Parte 1: Carregando e abrindo o arquivo de sales
sales = 'sales.xlsx'
df_sales = pd.read_excel(sales)

# Parte 3: Montando um groupby com as vendas por dia
######## 
# Parte 3a - Criando uma coluna para "DIA"

# Aqui vamos dizer para o código que este campo é uma data (pd.to_datetime)
df_sales['Data venda'] = pd.to_datetime(df_sales['Data venda']) 

# Isolando o dia do campo "Data venda"
df_sales['Dia'] = df_sales['Data venda'].dt.day

# Parte 2: Exibir o dataframe no frontend
st.write("Mostrando o Dataframe no frontend")
st.dataframe(df_sales)
