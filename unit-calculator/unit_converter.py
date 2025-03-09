import streamlit as st
import requests

# Custom CSS for better styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
        font-family: 'Arial', sans-serif;
        transition: background 0.3s, color 0.3s;
    }
    .st-bq {
        font-size: 1.2rem;
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .result-box:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .dark-mode .reportview-container {
        background: #2c3e50;
        color: #ecf0f1;
    }
    .dark-mode .result-box {
        background-color: #34495e;
        color: #ecf0f1;
    }
    .dark-mode .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: #ecf0f1;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s, transform 0.2s;
    }
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 5px;
        padding: 10px;
    }
    .stNumberInput input {
        border-radius: 5px;
        padding: 10px;
    }
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 30px;
        font-size: 0.9rem;
        color: #666;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for history and dark mode
if 'history' not in st.session_state:
    st.session_state.history = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Conversion functions
CONVERSION_FUNCTIONS = {
    "📏 Length": {
        "units": ["meters", "kilometers", "miles", "centimeters", "millimeters", "inches"],
        "factors": {
            "meters": 1,
            "kilometers": 0.001,
            "miles": 0.000621371,
            "centimeters": 100,
            "millimeters": 1000,
            "inches": 39.3701
        }
    },
    "⚖️ Weight": {
        "units": ["kilograms", "grams", "pounds", "ounces", "tons"],
        "factors": {
            "kilograms": 1,
            "grams": 1000,
            "pounds": 2.20462,
            "ounces": 35.274,
            "tons": 0.001
        }
    },
    "🌡️ Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "convert": lambda v, f, t: convert_temperature(v, f, t)
    },
    "⏳ Time": {
        "units": ["seconds", "minutes", "hours", "days", "weeks"],
        "factors": {
            "seconds": 1,
            "minutes": 1/60,
            "hours": 1/3600,
            "days": 1/86400,
            "weeks": 1/604800
        }
    },
    "🧪 Volume": {
        "units": ["liters", "milliliters", "cubic meters", "gallons", "cups"],
        "factors": {
            "liters": 1,
            "milliliters": 1000,
            "cubic meters": 0.001,
            "gallons": 0.264172,
            "cups": 4.22675
        }
    },
    "💵 Currency": {
        "units": [],  # Will be populated dynamically
        "convert": lambda v, f, t: convert_currency(v, f, t)
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_generic(value, from_unit, to_unit, category):
    if category == "🌡️ Temperature":
        return convert_temperature(value, from_unit, to_unit)
    elif category == "💵 Currency":
        return convert_currency(value, from_unit, to_unit)
    
    factors = CONVERSION_FUNCTIONS[category]["factors"]
    return value * factors[to_unit] / factors[from_unit]

def convert_currency(value, from_currency, to_currency):
    # Use Exchange Rates API to get real-time conversion rates
    API_KEY = "YOUR_EXCHANGE_RATES_API_KEY"  # Replace with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        if to_currency in rates:
            return value * rates[to_currency]
        else:
            raise ValueError(f"Currency {to_currency} not found in rates.")
    else:
        raise ValueError("Failed to fetch currency data.")

# Fetch currency units dynamically
def fetch_currency_units():
    API_KEY = "YOUR_EXCHANGE_RATES_API_KEY"  # Replace with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/USD"  # Use USD as base
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return list(data.get("rates", {}).keys())
    else:
        return ["USD", "EUR", "GBP", "INR", "JPY"]  # Fallback currencies

# Sidebar for additional options
with st.sidebar:
    st.session_state.dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    if st.button("🧹 Clear History"):
        st.session_state.history = []

# Apply dark mode dynamically
if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .reportview-container {
            background: #003092;
            color: #56021F;
        }
        .result-box {
            background-color: #34495e;
            color: #ecf0f1;
        }
        .sidebar .sidebar-content {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
    </style>
    """, unsafe_allow_html=True)

# Main app
st.title("🔢 Ultimate Unit Converter")
st.markdown("### Convert between various units with style!")

# Unit type selection
category = st.selectbox(
    "Select category:",
    list(CONVERSION_FUNCTIONS.keys()),
    index=0
)

# Fetch currency units if category is Currency
if category == "💵 Currency":
    CONVERSION_FUNCTIONS["💵 Currency"]["units"] = fetch_currency_units()

# Unit selection columns
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    from_unit = st.selectbox("From:", CONVERSION_FUNCTIONS[category]["units"])

with col3:
    to_unit = st.selectbox("To:", CONVERSION_FUNCTIONS[category]["units"])

# Swap button
with col2:
    st.write("")  # Vertical spacing
    if st.button("🔄 Swap", use_container_width=True):
        from_unit, to_unit = to_unit, from_unit

# Value input with dynamic validation
min_value = -float('inf') if category == "🌡️ Temperature" else 0.0
value = st.number_input(
    "Enter value:",
    min_value=min_value,
    format="%.4f",
    key="value_input"
)

# Real-time conversion
if value and from_unit and to_unit:
    try:
        result = convert_generic(value, from_unit, to_unit, category)
        result = round(result, 6)  # Limit decimal places
        
        # Add to history
        conversion_entry = f"{value} {from_unit} = {result} {to_unit}"
        if conversion_entry not in st.session_state.history:
            st.session_state.history.append(conversion_entry)
        
        # Display result with animation
        st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2ecc71; margin:0;">{value} {from_unit} =</h3>
            <h2 style="color: #e67e22; margin:0;">{result} {to_unit}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Copy to clipboard button
        if st.button("📋 Copy to Clipboard"):
            st.write(f"Copied: {result} {to_unit}")
        
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")

# Conversion history
with st.expander("📚 Conversion History"):
    if st.session_state.history:
        for entry in reversed(st.session_state.history):
            st.markdown(f"- {entry}")
    else:
        st.info("No conversions yet!")

# Quick reference
st.markdown("---")
st.markdown("### 📖 Quick Reference")
st.markdown("""
- **Length**: Includes inches for imperial conversions
- **Weight**: Now supports metric tons
- **Volume**: Added gallons and cups for cooking conversions
- **Temperature**: Supports negative values
- **Currency**: Real-time exchange rates
- **Swap**: Click the swap button to quickly reverse units
""")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    Built with ❤️ by <a href="https://github.com/yourusername" target="_blank">Bakhtawar</a>
</div>
""", unsafe_allow_html=True)