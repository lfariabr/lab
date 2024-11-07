
import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("10 - Leads")

# Parte 1: Carregando e abrindo o arquivo de leads
leads = 'leads.xlsx'
df_leads = pd.read_excel(leads)

# Parte 2: Tratando as datas para uso
df_leads['Dia da entrada'] = pd.to_datetime(df_leads['Dia da entrada']) # Dizendo que isso é uma data
df_leads['Dia'] = df_leads['Dia da entrada'].dt.day # Isola o dia da coluna "Dia da Entrada"

# Parte 3: Criando um dataframe e exibindo ele na página
st.write("Dataframe")
st.dataframe(df_leads)

##############################
# Gráfico por Dia

# Parte 4a: Group by por dia do mês contando os leads
groupby_leads_por_dia = (
    df_leads
    .groupby('Dia')                 # Agrupando pelo campo 'Dia'
    .agg({'ID do lead': 'nunique'})  # Contando a quantidade única de 'ID do lead'
    .reset_index()                   # Resetando o índice para manter o formato de DataFrame
)

# Parte 5a: Criar um gráfico de linhas para os dias do mês
grafico_leads_por_dia = px.line(
  groupby_leads_por_dia,
  x='Dia', # linha horizontal do gráfico
  y='ID do lead', # linha vertical
  title='Gráfico de leads por dia!', # titulo...
  labels={'ID do lead': 'Quantida de Leads', 'Dia': 'Dia do mês'}, # Tags/nomenclatura
  markers=True # marcadores nos pontos das linhas
)
st.plotly_chart(grafico_leads_por_dia)

##############################
# Gráfico por Unidade

# Parte 4b: 
# Group by por unidade contando os leads
groupby_leads_por_unidade = (
    df_leads
    .groupby('Unidade')                 # Agrupando pelo campo 'Dia'
    .agg({'ID do lead': 'nunique'})  # Contando a quantidade única de 'ID do lead'
    .reset_index()                   # Resetando o índice para manter o formato de DataFrame
)
# Parte 5b:
# Criar um gráfico de colunas para as unidades do mês
grafico_leads_por_unidade = px.bar(
  groupby_leads_por_dia,
  x='Dia', # linha horizontal do gráfico
  y='ID do lead', # linha vertical
  title='Gráfico de leads por dia!', # titulo...
  labels={'ID do lead': 'Quantida de Leads', 'Dia': 'Dia do mês'}, # Tags/nomenclatura
  markers=True # marcadores nos pontos das colunas
)
st.plotly_chart(grafico_leads_por_unidade)

# Para fazer mais gráficos, precisaremos repetir os passos 4, 5 e 6 adaptando onde necessário

# Parte 7: Fazendo um segundo gráfico, de Pizza
st.write("")
