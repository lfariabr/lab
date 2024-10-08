
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar for page selection
st.sidebar.title("Navigation") # Novo
page = st.sidebar.selectbox("Choose a page", ["Calculator", "Currency Converter", "Graphics", "Forca"]) # Novo

if page == "Calculator": # novo

  st.title("Calculator!")

  number1 = st.text_input("Enter first number:")
  number2 = st.text_input("Enter second number:")

  operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

  result = None

  if number1 and number2:
    if operation == "Add":
        result = float(number1) + float(number2)
        st.write(f"Result: {result}")

    elif operation == "Subtract":
        result = float(number1) - float(number2)
        st.write(f"Result: {result}")

    elif operation == "Multiply":
        result = float(number1) * float(number2)
        st.write(f"Result: {result}")

    elif operation == "Divide":
        result = float(number1) / float(number2)
        st.write(f"Result: {result}")

#### CONVERSOR API


elif page == "Currency Converter":

  # Declarando a URL:
  url = 'https://api.exchangerate-api.com/v4/latest/USD'
  my_request = requests.get(url)
  content = my_request.content
  dados = json.loads(content)
  exchange_rate_br = dados['rates']['BRL']
  exchange_rate_us = 1/exchange_rate_br

  st.title("Currency Converter!")

  st.text("It's simple: select the currency, type in the value and the magic will apear!")

  currency = st.selectbox("Options:", [None, "USD to BRL", "BRL to USD"])
  amount = st.number_input("Enter the amount:")

  if currency == "USD to BRL":
    result = amount * exchange_rate_br
    st.write(f"You have R${result}")

  elif currency == "BRL to USD":
    result = amount * exchange_rate_us
    st.write(f"You have U${result}")

#### NOVO _ GRÁFICOS - novo

elif page == "Graphics":

  st.title("Graphics!")

  leads = 'leads.xlsx'
  df_leads = pd.read_excel(leads)

  st.write("Dataframe")
  st.dataframe(df_leads)


  # Playing with dates
  df_leads['Dia da entrada'] = pd.to_datetime(df_leads['Dia da entrada']) # trata estes dados como texto
  df_leads['Dia do mês'] = df_leads['Dia da entrada'].dt.day_name()

  # # Extract day of the month from 'Dia da entrada'
  df_leads['apenas_o_dia'] = df_leads['Dia da entrada'].dt.day

  # # Filter data for SP units
  df_leads_total = df_leads

  # # Group by dia do mês and count unique leads
  groupby_leads_dia_do_mes = df_leads.groupby('apenas_o_dia').agg({'ID do lead': 'nunique'}).reset_index()

  st.write("Número de leads por dia")

  # # Create line graph for leads by day of the month
  graph_dia_do_mes = px.line(
      groupby_leads_dia_do_mes,
      x='apenas_o_dia',
      y='ID do lead',
      title='Leads por Dia',
      labels={'ID do lead': 'Número de Leads', 'apenas_o_dia': 'Dia do Mês'},
      markers=True  # Adiciona marcadores nos pontos da linha
  )
  # Display the graph
  st.plotly_chart(graph_dia_do_mes)

#### NOVO: FORCA

elif page == "Forca":

  st.title("Forca")
