import streamlit as st

def calculate_cooling_tower_efficiency(T_in, T_out, T_wb):
    """Calculate the efficiency of a cooling tower."""
    if T_in <= T_wb:
        return "Error: Inlet temperature must be greater than wet bulb temperature."
    if T_out >= T_in:
        return "Error: Outlet temperature must be less than inlet temperature."
    
    efficiency = (T_in - T_out) / (T_in - T_wb) * 100
    return f"The efficiency of the cooling tower is: {efficiency:.2f}%"

# Title of the application
st.title("Cooling Tower Efficiency Calculator")

# Input fields for temperatures
T_in = st.number_input("Inlet Water Temperature (°C):", min_value=-100.0, max_value=100.0, value=30.0)
T_out = st.number_input("Outlet Water Temperature (°C):", min_value=-100.0, max_value=100.0, value=25.0)
T_wb = st.number_input("Wet Bulb Temperature (°C):", min_value=-100.0, max_value=100.0, value=20.0)

# Button to perform calculation
if st.button("Calculate Efficiency"):
    result = calculate_cooling_tower_efficiency(T_in, T_out, T_wb)
    st.write(result)
