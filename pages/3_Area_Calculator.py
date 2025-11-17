import streamlit as st
import math

st.title("📐 Area Calculation App")
st.markdown("Calculate the area of a Circle, Rectangle, or Triangle.")

# Shape Selection
shape = st.selectbox(
    "Select the shape",
    ["Circle", "Rectangle", "Triangle"],
    index=0
)

st.divider()

area = None
error = None

# --- Circle Area ---
if shape == "Circle":
    st.subheader("Circle Area")
    st.caption("Formula: $A = \\pi r^2$")
    radius = st.number_input("Enter Radius ($r$)", min_value=0.0, value=5.0, step=0.1, format="%.2f")

    if st.button("Calculate Circle Area"):
        if radius < 0:
            error = "Radius cannot be negative."
        else:
            area = math.pi * (radius ** 2)

# --- Rectangle Area ---
elif shape == "Rectangle":
    st.subheader("Rectangle Area")
    st.caption("Formula: $A = \\text{Length} \\times \\text{Width}$")
    length = st.number_input("Enter Length", min_value=0.0, value=10.0, step=0.1, format="%.2f")
    width = st.number_input("Enter Width", min_value=0.0, value=5.0, step=0.1, format="%.2f")

    if st.button("Calculate Rectangle Area"):
        if length < 0 or width < 0:
            error = "Length and Width must be non-negative."
        else:
            area = length * width

# --- Triangle Area ---
elif shape == "Triangle":
    st.subheader("Triangle Area")
    st.caption("Formula: $A = \\frac{1}{2} \\times \\text{Base} \\times \\text{Height}$")
    base = st.number_input("Enter Base", min_value=0.0, value=10.0, step=0.1, format="%.2f")
    height = st.number_input("Enter Height", min_value=0.0, value=5.0, step=0.1, format="%.2f")

    if st.button("Calculate Triangle Area"):
        if base < 0 or height < 0:
            error = "Base and Height must be non-negative."
        else:
            area = 0.5 * base * height

# --- Display Result ---
if error:
    st.error(f"Calculation Error: {error}")
elif area is not None:
    st.success(f"The Area of the {shape} is: **{area:,.4f}** square units.")
