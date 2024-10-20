import requests
import json
import streamlit as st
import locale

# Set locale to Brazilian Portuguese for currency formatting
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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
currencies = list(dados['rates'].keys())

col_1, col_2 = st.columns(2)

with col_1:

  currency_1 = st.selectbox("Value (from)", currencies, index=20)
  currency_2 = st.selectbox("Value (to):", currencies, index=0)


  conversion_currency_1 = dados['rates'][currency_1]
  conversion_currency_2 = dados['rates'][currency_2]

with col_2:
  amount = st.number_input("Enter the amount:", format="%0.2f")

  converted_value = (amount * conversion_currency_2) / conversion_currency_1
  # Format the converted value using Brazilian Real currency format
  formatted_value = locale.currency(converted_value, grouping=True)

  st.markdown(f"## {formatted_value}")

  # Display the exchange rate between the two currencies
  exchange_rate = conversion_currency_2 / conversion_currency_1
  st.write(f"current rate: 1 {currency_1} = {exchange_rate:.4f} {currency_2}")

st.write("...")
st.write("Data loaded from https://www.exchangerate-api.com/")
