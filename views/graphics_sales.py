
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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

# Gráfico barra vendas_por_dia
grafico_vendas_por_dia = px.bar(
    groupby_vendas_por_dia,
    x='Dia',
    y='Valor líquido',
    title='Vendas por Dia',
    labels={'Valor líquido': 'Valor Líquido', 'Dia': 'Dia do Mês'},
)
st.plotly_chart(grafico_vendas_por_dia)

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


# Convert the 'Dia' column to numeric for trend line calculation (if not already numeric)
groupby_vendas_por_dia['Dia'] = pd.to_datetime(groupby_vendas_por_dia['Dia']).map(pd.Timestamp.toordinal)

# Calculate linear regression (trend line)
coef = np.polyfit(groupby_vendas_por_dia['Dia'], groupby_vendas_por_dia['Valor líquido'], 1)
trend_line = np.poly1d(coef)

# Generate trend line values
groupby_vendas_por_dia['Tendência'] = trend_line(groupby_vendas_por_dia['Dia'])

# Convert 'Dia' back to the original format if needed for display
groupby_vendas_por_dia['Dia'] = pd.to_datetime(groupby_vendas_por_dia['Dia'])

# Create the bar chart
grafico_vendas_por_dia = px.bar(
    groupby_vendas_por_dia,
    x='Dia',
    y='Valor líquido',
    title='Venda Diária',
    labels={'Valor líquido': 'R$ Valor Líquido', 'Dia': 'Dia do Mês'},
    text='Valor líquido'  # This will display the value on top of each bar
)

# Add trend line on top of the bar chart
grafico_vendas_por_dia.add_trace(
    go.Scatter(
        x=groupby_vendas_por_dia['Dia'],
        y=groupby_vendas_por_dia['Tendência'],
        mode='lines',
        name='Tendência',
        line=dict(color='cyan', width=2, dash='dash')  # Adjust color and style as needed
    )
)

# Show the chart in Streamlit
st.plotly_chart(grafico_vendas_por_dia)
