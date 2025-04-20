import streamlit as st

#Page Config 
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# CSS 
custom_css = """
<style>
/* Body and background */
body {
    background-color: #000000;
    color: #FFFFFF;
}

/* Main container */
.stApp {
    background-color: #000000;
    color: #FFFFFF;
}

/* Titles */
h1, h2, h3 {
    color: #FFFFFF;
}

/* Input fields */
input {
    background-color: #1a1a1a;
    color: #FFFFFF;
}

/* Buttons */
div.stButton > button {
    background-color: #FFFFFF;
    color: #000000;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #cccccc;
    color: #000000;
}

/* Result boxes */
.stSuccess {
    background-color: #1a1a1a;
    color: #00FF00;
    font-weight: bold;
}

.stInfo {
    background-color: #1a1a1a;
    color: #FFFFFF;
}

footer {
    color: #FFFFFF;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>⚖️ BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Check Your Health Status with BMI</h3>", unsafe_allow_html=True)
st.markdown("---")

#  Input Section 
st.subheader("Enter your details:")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)

with col2:
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)

# Calculate BMI Function
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

#  BMI Category Function 
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight ⚠️"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️"
    else:
        return "Obesity 🚨"

# Calculate Button 
if st.button("CALCULATE"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.success(f"Your BMI is: {bmi}")
    st.info(f"Category: {category}")

# Footer 
st.markdown("---")
st.markdown("<p style='text-align: center;'>Designed & Developed by Bakhtawar</p>", unsafe_allow_html=True)