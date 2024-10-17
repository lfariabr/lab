import streamlit as st

st.title("Calculator!")

# Get inputs from the user
number1 = st.text_input("Enter first number:")
number2 = st.text_input("Enter second number:")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

result = None

# Perform the calculation if both numbers are entered
if number1 and number2:
    try:
        number1 = float(number1)
        number2 = float(number2)

        if operation == "Add":
            result = number1 + number2
        elif operation == "Subtract":
            result = number1 - number2
        elif operation == "Multiply":
            result = number1 * number2
        elif operation == "Divide":
            result = number1 / number2

        st.write(f"Result: {result}")
    except ValueError:
        st.error("Please enter valid numeric values.")
