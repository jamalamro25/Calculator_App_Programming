import streamlit as st
import math

st.title("🧮 General Purpose Calculator")
st.markdown("Perform basic arithmetic, financial, and single-operand calculations.")

# Operation Type Selection
operation_type = st.selectbox(
    "Choose Calculation Type",
    [
        "Basic Arithmetic (+, -, *, /)",
        "Financial (Simple/Compound Interest)",
        "Single Operand (Square/Square Root)"
    ]
)

st.divider()

# --- Basic Arithmetic Mode (Activity 1 part 1: +, -, *, /) ---
if operation_type == "Basic Arithmetic (+, -, *, /)":
    st.subheader("Basic Arithmetic (A op B)")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number (A)", value=0.0, step=0.01, format="%.2f", key="basic_num1")
    with col2:
        num2 = st.number_input("Enter second number (B)", value=0.0, step=0.01, format="%.2f", key="basic_num2")

    op = st.selectbox(
        "Select Operation",
        ["+", "-", "*", "/"],
        key="basic_op"
    )

    result = None
    if st.button("Calculate Basic Arithmetic"):
        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    st.error("Cannot divide by zero.")
                    result = None
                else:
                    result = num1 / num2

            if result is not None:
                st.success(f"Result: **{result:,.4f}**")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- Financial Mode (Activity 1 part 2: Simple/Compound Interest) ---
elif operation_type == "Financial (Simple/Compound Interest)":
    st.subheader("Financial Calculations")

    financial_op = st.selectbox(
        "Select Financial Calculation",
        ["Simple Interest", "Compound Interest"]
    )

    # Financial Inputs
    principal = st.number_input("Principal Amount (P)", min_value=0.0, value=1000.0, step=100.0, format="%.2f")
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1, format="%.2f")
    time = st.number_input("Time (Years)", min_value=0.0, value=1.0, step=0.5, format="%.2f")

    if st.button("Calculate Financial"):
        try:
            r = rate / 100 # Convert percentage to decimal

            if financial_op == "Simple Interest":
                # Formula: I = P * r * t (Interest)
                interest = principal * r * time
                amount = principal + interest
                st.success(f"Simple Interest Earned: **{interest:,.2f}**")
                st.info(f"Total Amount (P + I): **{amount:,.2f}**")
                st.caption(f"Formula: $I = P \\times R \\times T$")

            elif financial_op == "Compound Interest":
                # Formula: A = P * (1 + r)^t (Amount) - assuming compounding annually
                amount = principal * (1 + r) ** time
                interest = amount - principal
                st.success(f"Compound Interest Earned: **{interest:,.2f}**")
                st.info(f"Total Amount (Compounded Annually): **{amount:,.2f}**")
                st.caption(f"Formula: $A = P \\left(1 + \\frac{r}{n}\\right)^{nt}$ (Assuming $n=1$ for annual compounding)")

        except Exception as e:
            st.error(f"An error occurred: {e}")


# --- Single Operand Mode (Activity 1 part 3: Square/Square Root) ---
elif operation_type == "Single Operand (Square/Square Root)":
    st.subheader("Single Operand Calculations (on X)")

    single_op = st.selectbox(
        "Select Operation",
        ["Square", "Square Root"]
    )

    num_x = st.number_input("Enter a number (X)", value=4.0, step=0.1, format="%.2f", key="single_num_x")

    if st.button("Calculate Single Operand"):
        try:
            if single_op == "Square":
                result = num_x ** 2
                st.success(f"Square of {num_x} is: **{result:,.4f}**")
                st.caption(f"Formula: $X^2$")

            elif single_op == "Square Root":
                if num_x < 0:
                    st.error("Cannot calculate the square root of a negative number (result is imaginary).")
                else:
                    result = math.sqrt(num_x)
                    st.success(f"Square Root of {num_x} is: **{result:,.4f}**")
                    st.caption(f"Formula: $\\sqrt{{X}}$")
        except Exception as e:
            st.error(f"An error occurred: {e}")
