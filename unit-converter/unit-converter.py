import streamlit as st

# 🎉 Title and Description
st.title("🧮 Unit Converter App")
st.markdown("### 🔁 Convert Length 📏, Weight ⚖️, and Time ⏱️ instantly")
st.write("👋 Welcome! This app helps you quickly convert between units of length, weight, and time. Just pick a type and enter your value.")

# 🚀 Select conversion type
conversion_type = st.selectbox("📦 Select conversion type", ["📏 Length", "⚖️ Weight", "⏱️ Time"])

# 🔧 Conversion logic functions
def convert_length(value, from_unit, to_unit):
    units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

def convert_time(value, from_unit, to_unit):
    units = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400
    }
    return value * units[from_unit] / units[to_unit]

# 💡 UI for each type
if conversion_type == "📏 Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    value = st.number_input("🔢 Enter value:", min_value=0.0)
    from_unit = st.selectbox("🡆 From:", units)
    to_unit = st.selectbox("🡄 To:", units)
    if st.button("🔄 Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "⚖️ Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
    value = st.number_input("🔢 Enter value:", min_value=0.0)
    from_unit = st.selectbox("🡆 From:", units)
    to_unit = st.selectbox("🡄 To:", units)
    if st.button("🔄 Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "⏱️ Time":
    units = ["Second", "Minute", "Hour", "Day"]
    value = st.number_input("🔢 Enter time value:", min_value=0.0)
    from_unit = st.selectbox("🡆 From:", units)
    to_unit = st.selectbox("🡄 To:", units)
    if st.button("🔄 Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit}(s) = {result:.2f} {to_unit}(s)")
