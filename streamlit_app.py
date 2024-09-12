
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

  st.title("Currency Converter!")

  real_amount = st.text_input("Enter the amount in real (R$):")
  exchange_rate = 0.20

  if real_amount:
    try:
      real_value = float(real_amount)
      dollar_value = real_value * exchange_rate
      st.write(f"Result: ${dollar_value:.2f}")
    except ValueError:
      st.write("Invalid input. Please enter a valid number.")

#### NOVO _ GRÁFICOS - novo 3
elif page == "Graphics": # novo3

  st.title("Graphics!")

  leads = '/content/lab/leads.xlsx'
  df_leads = pd.read_excel(leads)

  # Datetimelike values on 'Dia da entrada'
  df_leads['Dia da entrada'] = pd.to_datetime(df_leads['Dia da entrada'])

  # Extract the day of the week from 'Dia da entrada'
  df_leads['Dia do mês'] = df_leads['Dia da entrada'].dt.day_name()

  # Extract day of the month from 'Dia da entrada'
  df_leads['Dia da semana'] = df_leads['Dia da entrada'].dt.day

  unidades_sp = ['JARDINS', 'SANTO AMARO', 'TATUAPÉ', 
              'IPIRANGA', 'ITAIM', 'TUCURUVI', 'MOEMA', 'OSASCO', 'SÃO BERNARDO', 
              'ALPHAVILLE', 'MOOCA', 'LAPA']
              
  # Filter data for SP units
  df_leads_sp = df_leads[df_leads['Unidade'].isin(unidades_sp)]

  # Group by 'Dia do mês'
  groupby_sp_dia_do_mes = df_leads_sp.groupby('Dia do mês').agg({'ID do lead': 'nunique'}).reset_index()
  st.write("Number of leads by day of the month:")
  fig_mes = px.bar(groupby_sp_dia_do_mes, x='Dia do mês', y='ID do lead', title='Leads by Day of the Month')
  st.plotly_chart(fig_mes)

  # Group by 'Dia da semana'
  groupby_sp_dia_da_semana = df_leads_sp.groupby('Dia da semana').agg({'ID do lead': 'nunique'}).reset_index()
  st.write("Number of leads by day of the week:")
  fig_semana = px.bar(groupby_sp_dia_da_semana, x='Dia da semana', y='ID do lead', title='Leads by Day of the Week')
  st.plotly_chart(fig_semana)

  # Pie chart using 'Dia da semana'
  fig_pie = px.pie(groupby_sp_dia_da_semana, values='ID do lead', names='Dia da semana', title='Leads Distribution by Day of the Week')
  st.plotly_chart(fig_pie)

  # TEST TEST
