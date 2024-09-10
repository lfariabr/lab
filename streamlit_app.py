
import streamlit as st

st.title("Hello World!")
st.write("This is a test")

number1 = st.text_input("Enter first number:")
number2 = st.text_input("Enter second number:")

if st.button("Calculate"):
    try:
        number1 = float(number1)
        number2 = float(number2)
        result = number1 + number2
        st.write(f"The result is: {result}")
        except ValueError:
        st.write("Please enter valid numbers.")
