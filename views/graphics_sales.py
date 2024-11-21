
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Título
st.title("02 - Sales")

# Carregando e abrindo o arquivo de sales
sales = 'sales.xlsx'
df_sales = pd.read_excel(sales)

# Groupby com as vendas por dia
########
# Parte 2a - Criando uma coluna para "DIA"
df_sales['Data venda'] = pd.to_datetime(df_sales['Data venda']) # Aqui vamos dizer para o código que este campo é uma data (pd.to_datetime)
df_sales['Dia'] = df_sales['Data venda'].dt.day # Isolando o dia do campo "Data venda"

# Group by Vendas por Dia
groupby_vendas_por_dia = (
      df_sales
      .groupby('Dia')
      .agg({'Valor líquido': 'sum'})
      .reset_index()
  )

# Gráfico barra vendas_por_dia
grafico_vendas_por_dia = px.bar(
    groupby_vendas_por_dia,
    x='Dia',
    y='Valor líquido',
    title='Venda Diária',
    labels={'Valor líquido': 'Valor Líquido', 'Dia': 'Dia do Mês'},
)
st.plotly_chart(grafico_vendas_por_dia)

#####
# Tarefa de colocar linha de tendência no gráfico
####

# Group by Venda / Dia / Loja
# colunas: 'Unidade', 'Valor líquido', 'Dia'
groupby_vendas_dia_loja = (
    df_sales
    .groupby(['Dia', 'Unidade'])
    .agg({'Valor líquido': 'sum'})
    .reset_index()
    .fillna(0)
)

# Pivotando os dados para exibir Dia x Unidade
pivot_vendas_dia_loja = groupby_vendas_dia_loja.pivot(
                        index='Dia',
                        columns='Unidade',
                        values='Valor líquido')

pivot_vendas_dia_loja = pivot_vendas_dia_loja.fillna(0)

st.write("Venda Diária Detalhada")
st.dataframe(pivot_vendas_dia_loja)


# Dividindo a tela em 2 colunas:
col1, col2 = st.columns(2)

with col1:

  # Groupby por profissões
  groupby_vendas_por_profissao = (
      df_sales
      .groupby('Profissão cliente')
      .agg({'Valor líquido': 'sum'})
      .reset_index()
      .sort_values('Valor líquido', ascending=False)
      .head(10) # top 10
  )

  # Gráfico de Pizza 
  grafico_vendas_por_profissao_top10 = px.pie(
        groupby_vendas_por_profissao,
        names='Profissão cliente',
        values='Valor líquido', # : 'sum'
        title='Valor comprado por Profissão',
        labels={'Valor líquido': 'Valor Comprado', 'Profissão cliente': 'Profissão'},
    )

  st.plotly_chart(grafico_vendas_por_profissao_top10)

with col2:

  # Groupby por Vendedoras
  groupby_vendas_por_vendedoras = (
      df_sales
      .groupby('Consultor')
      .agg({'Valor líquido': 'sum'})
      .reset_index()
      .sort_values('Valor líquido', ascending=False)
      .head(10) # top 10
  )

  # Gráfico barra vendas_por_dia
  grafico_vendas_por_consultor = px.bar(
      groupby_vendas_por_vendedoras,
      x='Consultor',
      y='Valor líquido',
      title='Venda Por Consultora',
      labels={'Valor líquido': 'Valor Líquido', 'Consultor': 'Consultora de Vendas'},
  )
  st.plotly_chart(grafico_vendas_por_consultor)


st.dataframe(df_sales)
