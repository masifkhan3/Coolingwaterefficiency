import streamlit as st

def calculate_cooling_tower_efficiency(T_in, T_out, T_wb):
    """Calculate the efficiency of a cooling tower."""
    if T_in <= T_wb:
        return "Error: The Inlet Water Temperature must be greater than the Wet Bulb Temperature."
    if T_out >= T_in:
        return "Error: The Outlet Water Temperature must be less than the Inlet Water Temperature."
    
    efficiency = (T_in - T_out) / (T_in - T_wb) * 100
    return f"The efficiency of the cooling tower is: {efficiency:.2f}%"

# Title of the application
st.title("Cooling Tower Efficiency Calculator")

# Input fields for temperatures
st.write("Enter the temperatures below (in °C):")
T_in = st.number_input("Inlet Water Temperature:", )
T_out = st.number_input("Outlet Water Temperature:", )
T_wb = st.number_input("Wet Bulb Temperature:",)

# Button to perform calculation
if st.button("Calculate Efficiency"):
    result = calculate_cooling_tower_efficiency(T_in, T_out, T_wb)
    st.subheader("Result:")
    st.write(result)
