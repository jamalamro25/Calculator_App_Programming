import streamlit as st

# Set the page configuration for better aesthetics and a custom title
st.set_page_config(
    page_title="Workshop 7 Calculator App",
    page_icon="➗",
    layout="centered"
)

st.title("🔢 Multi-Page Calculator Application")
st.markdown("""
This application is designed to complete the workshop 7 activity, featuring three distinct calculators organized using Streamlit's multi-page functionality.

Use the **sidebar on the left** to navigate between the different calculators.
""")

st.info("👈 Select a calculation tool from the sidebar to begin (e.g., General Calculator, BMI, or Area).")

st.header("Application Overview")
st.markdown("""
1.  **General Calculator:** Handles basic arithmetic, simple/compound interest, and square/square root.
2.  **BMI Calculator:** Calculates Body Mass Index and provides interpretation.
3.  **Area Calculator:** Calculates the area for a Circle, Rectangle, and Triangle.
""")
