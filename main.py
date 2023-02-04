
import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])


if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
else:
    result = num1 / num2
if st.button('Result'): 
    st.write(f"Result: {result}")


