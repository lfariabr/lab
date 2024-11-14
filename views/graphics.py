
import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.title("10 - Leads - Test")

# Parte 1: Carregando e abrindo o arquivo de leads
leads = 'leads.xlsx'
df_leads = pd.read_excel(leads)

# Parte 2: Tratando as datas para uso
df_leads['Dia da entrada'] = pd.to_datetime(df_leads['Dia da entrada']) # Dizendo que isso é uma data
df_leads['Dia'] = df_leads['Dia da entrada'].dt.day # Isola o dia da coluna "Dia da Entrada"

# Parte 3: Criando um dataframe e exibindo ele na página
st.write("Dataframe")
st.dataframe(df_leads)

# Dividindo a tela em 2 colunas:
col1, col2 = st.columns(2)

with col1:
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

with col2:
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
    groupby_leads_por_unidade,
          x='Unidade',
          y='ID do lead',
          title='Número de Leads por Loja',
          labels={'ID do lead': 'Número de Leads', 'Unidade': 'Unidade'},
      )
  st.plotly_chart(grafico_leads_por_unidade)

# Para fazer mais gráficos, precisaremos repetir os passos 4, 5 e 6 adaptando onde necessário

##############################
# Colunas 3 e 4:
##############################
col3, col4 = st.columns(2)

with col3:
  # Parte 4c: groupby
  groupby_leads_por_fonte = (
      df_leads
      .groupby('Fonte')
      .agg({'ID do lead': 'nunique'})
      .reset_index()
  )

  #fig = px.pie(df, values='pop', names='country', title='Population of European continent')
  # Parte 5c: gráfico
  grafico_leads_por_fonte = px.pie(
      groupby_leads_por_fonte,
      names='Fonte',
      values='ID do lead',
      title='Número de Leads por Fonte',
      labels={'ID do lead': 'Número de leads', 'Fonte': 'Fonte'},
  )
  st.plotly_chart(grafico_leads_por_fonte)

with col4:
  # Parte 4c: groupby
  groupby_leads_por_status = (
      df_leads
      .groupby('Status')
      .agg({'ID do lead': 'nunique'})
      .reset_index()
  )

  #fig = px.pie(df, values='pop', names='country', title='Population of European continent')
  # Parte 5c: gráfico
  grafico_leads_por_status = px.pie(
      groupby_leads_por_status,
      names='Status',
      values='ID do lead',
      title='Número de Leads por Status',
      labels={'ID do lead': 'Número de leads', 'Status': 'Status'},
  )
  st.plotly_chart(grafico_leads_por_status)

##############################
# Tabelas
##############################

# Fonte por Unidade
fontes_pagas = ['Facebook Leads', 'Facebook Postlink', 'Google Pesquisa']
fontes_organicas = ['Instagram', 'Facebook', 'CRM Bônus']
# Próximo Papo: Fazer groupby por unidade x fonte
# st.dataframe()

# Lead por Dia por Unidade
# Próximo Papo: Fazer groupby por unidade x dia
# st.dataframe()

# Fazer a página de Vendas
