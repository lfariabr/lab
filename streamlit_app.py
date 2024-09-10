
import streamlit as st

st.title("Hello World!")
st.write("This is a test")

number1 = st.text_input("Enter first number:")
number2 = st.text_input("Enter second number:")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

result = None

st.button("Calculate")

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
