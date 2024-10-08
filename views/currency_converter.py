import requests
import json
import streamlit as st

#### CONVERSOR API

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
