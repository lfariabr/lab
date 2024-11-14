
import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("Sales Page")

# Parte 1: Carregando e abrindo o arquivo de sales
sales = 'sales.xlsx'
df_sales = pd.read_excel(sales)

# Parte 2: Montando um groupby com as vendas por dia
######## 
# Parte 2a - Criando uma coluna para "DIA"

# Aqui vamos dizer para o código que este campo é uma data (pd.to_datetime)
df_sales['Data venda'] = pd.to_datetime(df_sales['Data venda']) 

# Isolando o dia do campo "Data venda"
df_sales['Dia'] = df_sales['Data venda'].dt.day

# Parte 3: Exibir o dataframe no frontend
st.write("Mostrando o Dataframe no frontend")
st.dataframe(df_sales)

# Parte 4: Group by Vendas por Dia
groupby_vendas_por_dia = (
      df_sales
      .groupby('Dia')                
      .agg({'Valor líquido': 'sum'})  
      .reset_index()                   
  )

st.write("Exibindo o groupby_vendas_por_dia")
st.dataframe(groupby_vendas_por_dia)

# Tarefa de colocar linha de tendência no gráfico

# Parte 5: Group by Venda / Dia / Loja
# colunas: 'Unidade', 'Valor líquido', 'Dia'
groupby_vendas_dia_loja = (
    df_sales
    .groupby(['Dia', 'Unidade'])                
    .agg({'Valor líquido': 'sum'})  
    .reset_index()                   
)

st.write("Exibindo o groupby_vendas_dia_loja")
st.dataframe(groupby_vendas_dia_loja)
