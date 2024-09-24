
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd # novo 3
import plotly.express as px

# Sidebar for page selection
st.sidebar.title("Navigation") # Novo
page = st.sidebar.selectbox("Choose a page", ["Calculator", "Currency Converter", "Graphics"]) # Novo

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

#### NOVO _ CONVERSOR


elif page == "Currency Converter": # novo

  # Declarando a URL:
  url = 'https://api.exchangerate-api.com/v4/latest/USD'
  my_request = requests.get(url)
  content = my_request.content
  dados = json.loads(content)
  exchange_rate_br = dados['rates']['BRL']
  exchange_rate_us = 1/exchange_rate_br

  st.title("Currency Converter!")

  st.text("It's simple: select the currency, type in the value and the magic will apear!")
  currencies = list(dados['rates'].keys())

  col_1, col_2 = st.columns(2)

  with col_1:

    currency_1 = st.selectbox("Options:", currencies, index=0)
    currency_2 = st.selectbox("Options:", currencies, index=20)


    conversion_currency_1 = dados['rates'][currency_1]
    conversion_currency_2 = dados['rates'][currency_2]

  with col_2:
    amount = st.number_input("Enter the amount:", format="%0.2f")
    
    converted_value = (amount * conversion_currency_2) / conversion_currency_1
    st.markdown(f"## {currency_2}{converted_value:.2f}")

    #st.write(f"R$ {converted_value:.2f}")
    # Testando o código
    # st.write(conversion_currency_1)
    # st.write(conversion_currency_2)
