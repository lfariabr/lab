
import streamlit as st


# Sidebar for page selection
st.sidebar.title("Navigation") # Novo
page = st.sidebar.selectbox("Choose a page", ["Calculator", "Currency Converter"]) # Novo

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

elif page == "Currency Converter": # novo

  st.title("Currency Converter!")
