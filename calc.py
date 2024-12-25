import streamlit as st
import math

# Advanced Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Square root of negative number"

def factorial(a):
    if a >= 0 and int(a) == a:
        return math.factorial(int(a))
    else:
        return "Error: Factorial of non-integer or negative number"

def logarithm(a, base):
    if a > 0 and base > 0 and base != 1:
        return math.log(a, base)
    else:
        return "Error: Invalid input for logarithm"

# Streamlit App
def main():
    st.title("Advanced Calculator")

    menu = ["Basic Operations", "Advanced Functions"]
    choice = st.sidebar.selectbox("Select Operation Type", menu)

    if choice == "Basic Operations":
        st.header("Basic Operations")
        num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
        num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
        operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

        if st.button("Calculate"):
            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)

            st.success(f"Result: {result}")

    elif choice == "Advanced Functions":
        st.header("Advanced Functions")
        adv_operation = st.selectbox("Operation", ["Square Root", "Power", "Factorial", "Logarithm"])

        if adv_operation == "Square Root":
            num = st.number_input("Enter number", value=0.0, format="%.2f")
            if st.button("Calculate"):
                result = sqrt(num)
                st.success(f"Result: {result}")

        elif adv_operation == "Power":
            base = st.number_input("Enter base", value=0.0, format="%.2f")
            exponent = st.number_input("Enter exponent", value=0.0, format="%.2f")
            if st.button("Calculate"):
                result = power(base, exponent)
                st.success(f"Result: {result}")

        elif adv_operation == "Factorial":
            num = st.number_input("Enter number (integer only)", value=0.0, format="%.2f")
            if st.button("Calculate"):
                result = factorial(num)
                st.success(f"Result: {result}")

        elif adv_operation == "Logarithm":
            num = st.number_input("Enter number", value=0.0, format="%.2f")
            base = st.number_input("Enter base", value=10.0, format="%.2f")
            if st.button("Calculate"):
                result = logarithm(num, base)
                st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
