
import pandas as pd
import plotly.express as px
import streamlit as st

#### NOVO _ GRÁFICOS - novo
st.title("Leads 11!")
st.write("Dataframe")

# Parte 1: Carregando e abrindo o arquivo de leads
leads = 'leads.xlsx'
df_leads = pd.read_excel(leads)

# Parte 2: Criando um dataframe e exibindo ele na página
st.write("Dataframe")
st.dataframe(df_leads)

# Parte 3: Tratando as datas para uso
df_leads['Dia da entrada'] = pd.to_datetime(df_leads['Dia da entrada']) # Dizendo que isso é uma data
df_leads['Dia'] = df_leads['Dia da entrada'].dt.day

# Parte 4: Group by por dia do mês contando os leads
groupby_leads_por_dia = (
    df_leads
    .groupby('Dia')                 # Agrupando pelo campo 'Dia'
    .agg({'ID do lead': 'nunique'})  # Contando a quantidade única de 'ID do lead'
    .reset_index()                   # Resetando o índice para manter o formato de DataFrame
)
# Parte 5: Escrever o nome do gráfico pra conferir
st.write("Gráfico de leads por dia!")

# Parte 6: Criar um gráfico de linhas para os dias do mês
grafico_leads_por_dia = px.line(
  groupby_leads_por_dia,
  x='Dia', # linha horizontal do gráfico
  y='ID do lead', # linha vertical
  title='Gráfico de leads por dia!', # titulo...
  labels={'ID do lead': 'Quantida de Leads', 'Dia': 'Dia do mês'}, # Tags/nomenclatura
  markers=True # marcadores nos pontos das linhas
)

st.plotly_chart(grafico_leads_por_dia)

# Para fazer mais gráficos, precisaremos
# repetir os passos 4, 5 e 6
# Adaptando onde necessário
# Parte 7: Fazendo um segundo gráfico, de Pizza
st.write("")
