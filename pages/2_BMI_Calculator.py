import streamlit as st

st.title("🏋️‍♀️ Body Mass Index (BMI) Calculator")
st.markdown("Calculate your BMI using the metric system and receive an interpretation.")

# Input fields for Weight and Height
weight = st.number_input(
    "Enter your Weight (in kilograms, kg)",
    min_value=1.0,
    max_value=300.0,
    value=70.0,
    step=0.1,
    format="%.2f"
)

height = st.number_input(
    "Enter your Height (in meters, m)",
    min_value=0.1,
    max_value=3.0,
    value=1.75,
    step=0.01,
    format="%.2f"
)

st.divider()
st.caption("BMI Formula: $BMI = \\frac{\\text{Weight (kg)}}{\\text{Height}^2 (m^2)}$")

if st.button("Calculate BMI"):
    if height <= 0:
        st.error("Height must be greater than zero to calculate BMI.")
    else:
        # Start of the fixed try block
        try:
            # Calculate BMI: BMI = weight / (height ** 2)
            bmi = weight / (height ** 2)

            # Display BMI result
            st.header(f"Your calculated BMI is: **{bmi:,.2f}**")

            # Interpret the category
            category = ""
            color = "blue"

            if bmi < 18.5:
                category = "Underweight"
                color = "orange"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
                color = "green"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "red"
            else: # bmi >= 30
                category = "Obesity"
                color = "red"

            st.markdown(f"**Interpretation:** You fall into the **:{color}[{category}]** category.")

            st.markdown("---")
            st.subheader("BMI Categories")
            st.markdown("""
            * **< 18.5**: :orange[Underweight]
            * **18.5 – 24.9**: :green[Normal weight] (Healthy Range)
            * **25.0 – 29.9**: :red[Overweight]
            * **≥ 30.0**: :red[Obesity]
            """)

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
