import streamlit as st

# 💅 Custom CSS Styling for Beautiful UI
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body, .stApp {
        background: linear-gradient rgba(255, 255, 255, 0.1) */
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    h1 {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(45deg, #ff6347, #ff1493); /* Gradient for the heading */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 10px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #ff6347, #ff1493); /* Gradient for the heading */
        color: white;
        font-size: 18px;
        padding: 12px 28px;
        border: none;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0px 8px 15px rgba(246, 208, 47, 0.3);
    }

    .stButton>button:hover {
        transform: scale(1.08);
        background: linear-gradient(45deg, #ff6326, #ff1430);
        color: #fff;
        box-shadow: 0px 10px 25px rgba(255, 99, 71, 0.4);
    }

    .result-box {
        font-size: 22px;
        font-weight: 500;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 15px;
        margin-top: 25px;
        backdrop-filter: blur(8px);
        box-shadow: 0 4px 20px rgba(255, 99, 71, 0.2);
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #f0f0f0;
        padding-bottom: 20px;
    }

    .stSelectbox, .stNumberInput {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔤 Heading and Info
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("🌟 Easily convert between different units of Length, Weight, and Temperature.")

# 🧭 Sidebar for Conversion Type
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# 🔄 Unit Selection Based on Type
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometer", "Centimeter", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometer", "Centimeter", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# 🔧 Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Ounces': 35.274, 'Pounds': 2.20462
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value

# 🚀 Convert Button and Result Display
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# 📌 Footer
st.markdown("<div class='footer'>Created with 💜 by Bakhtawar</div>", unsafe_allow_html=True)
