import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

st.title("📏 Unit Converter")
st.caption("Convert between different measurement units")

# Conversion options
conversion_type = st.selectbox(
    "Select conversion type:",
    ["Length", "Weight", "Temperature"]
)

# Unit definitions
units = {
    "Length": {
        "Millimeter": 0.001,
        "Centimeter": 0.01, 
        "Meter": 1,
        "Kilometer": 1000,
        "Inch": 0.0254,
        "Foot": 0.3048
    },
    "Weight": {
        "Gram": 1,
        "Kilogram": 1000,
        "Pound": 453.592,
        "Ounce": 28.3495
    },
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Input fields
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter value:", value=1.0, step=0.1)
    from_unit = st.selectbox("From unit:", options=list(units[conversion_type].keys()))

with col2:
    st.write("")  # Spacer
    st.write("")  # Spacer  
    to_unit = st.selectbox("To unit:", options=list(units[conversion_type].keys()))

# Conversion logic
def convert(value, from_unit, to_unit, conversion_type):
    if conversion_type in ["Length", "Weight"]:
        base_value = value * units[conversion_type][from_unit]
        return base_value / units[conversion_type][to_unit]
    else:  # Temperature
        if from_unit == to_unit:
            return value
            
        # Convert to Celsius first
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        else:  # Kelvin
            celsius = value - 273.15
            
        # Convert from Celsius to target unit
        if to_unit == "Celsius":
            return celsius
        elif to_unit == "Fahrenheit":
            return celsius * 9/5 + 32
        else:  # Kelvin
            return celsius + 273.15

# Convert button
if st.button("Convert", type="primary", use_container_width=True):
    try:
        result = convert(value, from_unit, to_unit, conversion_type)
        st.success(f"**Result:** {value} {from_unit} = {result:.2f} {to_unit}")
    except:
        st.error("Invalid conversion. Please check your inputs.")

