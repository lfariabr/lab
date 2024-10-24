
import pandas as pd
import plotly.express as px
import streamlit as st

#### NOVO _ GRÁFICOS - novo

st.title("Teste Graphics!")

# Carregando e abrindo o arquivo de leads
leads = 'leads.xlsx'
df_leads = pd.read_excel(leads)

# Criando um dataframe e exibindo ele na página
st.write("Dataframe")
st.dataframe(df_leads)

