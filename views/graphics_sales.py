
import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("Sales Page")

# Parte 1: Carregando e abrindo o arquivo de sales
sales = 'sales.xlsx'
df_sales = pd.read_excel(sales)

# Parte 2: Exibir o dataframe no frontend
st.write("Mostrando o Dataframe no frontend")
st.dataframe(df_sales)
