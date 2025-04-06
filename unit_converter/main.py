import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        transition: all 0.2s ease;
        background-color: #4e79a7;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        background-color: #3a5f8a;
    }
    .result-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        border-left: 4px solid #4e79a7;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📏 Unit Converter")
st.caption("Convert between different measurement units")

# Unit definitions
units = {
    "Length": {
        "Millimeter": {"factor": 0.001, "symbol": "mm"},
        "Centimeter": {"factor": 0.01, "symbol": "cm"},
        "Meter": {"factor": 1, "symbol": "m"},
        "Kilometer": {"factor": 1000, "symbol": "km"},
        "Inch": {"factor": 0.0254, "symbol": "in"},
        "Foot": {"factor": 0.3048, "symbol": "ft"},
        "Yard": {"factor": 0.9144, "symbol": "yd"},
        "Mile": {"factor": 1609.34, "symbol": "mi"}
    },
    "Weight": {
        "Milligram": {"factor": 0.001, "symbol": "mg"},
        "Gram": {"factor": 1, "symbol": "g"},
        "Kilogram": {"factor": 1000, "symbol": "kg"},
        "Pound": {"factor": 453.592, "symbol": "lb"},
        "Ounce": {"factor": 28.3495, "symbol": "oz"}
    },
    "Temperature": {
        "Celsius": {"symbol": "°C"},
        "Fahrenheit": {"symbol": "°F"},
        "Kelvin": {"symbol": "K"}
    },
    "Speed": {
        "Meters/second": {"factor": 1, "symbol": "m/s"},
        "Kilometers/hour": {"factor": 0.277778, "symbol": "km/h"},
        "Miles/hour": {"factor": 0.44704, "symbol": "mph"}
    },
    "Area": {
        "Square Meter": {"factor": 1, "symbol": "m²"},
        "Square Kilometer": {"factor": 1e6, "symbol": "km²"},
        "Square Foot": {"factor": 0.092903, "symbol": "ft²"},
        "Acre": {"factor": 4046.86, "symbol": "ac"}
    },
    "Volume": {
        "Milliliter": {"factor": 0.001, "symbol": "mL"},
        "Liter": {"factor": 1, "symbol": "L"},
        "Gallon (US)": {"factor": 3.78541, "symbol": "gal"},
        "Cubic Meter": {"factor": 1000, "symbol": "m³"}
    },
    "Time": {
        "Second": {"factor": 1, "symbol": "s"},
        "Minute": {"factor": 60, "symbol": "min"},
        "Hour": {"factor": 3600, "symbol": "hr"},
        "Day": {"factor": 86400, "symbol": "day"}
    },
    "Digital Storage": {
        "Byte": {"factor": 1, "symbol": "B"},
        "Kilobyte": {"factor": 1024, "symbol": "KB"},
        "Megabyte": {"factor": 1024**2, "symbol": "MB"},
        "Gigabyte": {"factor": 1024**3, "symbol": "GB"}
    }
}

# Conversion type selection
conversion_type = st.selectbox(
    "Select conversion type:",
    list(units.keys())
)

# Input fields
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter value:", value=1.0, step=0.1)
    from_unit = st.selectbox(
        "From unit:", 
        options=list(units[conversion_type].keys()),
        format_func=lambda x: f"{x} ({units[conversion_type][x]['symbol']})"
    )

with col2:
    st.write("")  # Spacer for alignment
    to_unit = st.selectbox(
        "To unit:", 
        options=list(units[conversion_type].keys()),
        index=1 if len(units[conversion_type]) > 1 else 0,
        format_func=lambda x: f"{x} ({units[conversion_type][x]['symbol']})"
    )

# Conversion logic
def convert(value, from_unit, to_unit, conversion_type):
    if conversion_type == "Temperature":
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == "Celsius":
            return celsius
        elif to_unit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
    else:
        if from_unit == to_unit:
            return value
            
        base_value = value * units[conversion_type][from_unit]["factor"]
        return base_value / units[conversion_type][to_unit]["factor"]

# Convert button
if st.button("Convert", type="primary"):
    try:
        result = convert(value, from_unit, to_unit, conversion_type)
        
        from_sym = units[conversion_type][from_unit]["symbol"]
        to_sym = units[conversion_type][to_unit]["symbol"]
        
        st.markdown(f"""
        <div class="result-box">
            <p><strong>Conversion Result:</strong></p>
            <p>{value:,.2f} {from_unit} ({from_sym}) = <strong>{result:,.4f} {to_unit} ({to_sym})</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Conversion error: {str(e)}")