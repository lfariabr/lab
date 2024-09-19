
import streamlit as st
import pandas as pd # novo 3
import plotly.express as px
import json
import requests

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

  currency = st.selectbox("Options:", [None, "USD to BRL", "BRL to USD"])
  amount = st.number_input("Enter the amount:")

  if currency == "USD to BRL":
    result = amount * exchange_rate_br
    st.write(f"You have R${result}")

  elif currency == "BRL to USD":
    result = amount * exchange_rate_us
    st.write(f"You have U${result}")
