import streamlit as st
import matplotlib.pyplot as plt

def calculate_cooling_tower_efficiency(T_in, T_out, T_wb):
    """Calculate the efficiency of a cooling tower."""
    if T_in <= T_wb:
        return "Error: The Inlet Water Temperature must be greater than the Wet Bulb Temperature."
    if T_out >= T_in:
        return "Error: The Outlet Water Temperature must be less than the Inlet Water Temperature."
    
    efficiency = (T_in - T_out) / (T_in - T_wb) * 100
    return efficiency

# Title of the application
st.title("Cooling Tower Efficiency Calculator")

# Input fields for temperatures
st.write("Enter the temperatures below (in °C):")
T_in = st.number_input("Inlet Water Temperature:", min_value=-100.0, max_value=100.0, value=30.0)
T_out = st.number_input("Outlet Water Temperature:", min_value=-100.0, max_value=100.0, value=25.0)
T_wb = st.number_input("Wet Bulb Temperature:", min_value=-100.0, max_value=100.0, value=20.0)

# Button to perform calculation
if st.button("Calculate Efficiency"):
    efficiency = calculate_cooling_tower_efficiency(T_in, T_out, T_wb)

    if isinstance(efficiency, str):  # Error message
        st.subheader("Result:")
        st.write(efficiency)
    else:  # Successful calculation
        st.subheader("Result:")
        st.write(f"The efficiency of the cooling tower is: {efficiency:.2f}%")
        
        # Comparison with standard efficiency
        standard_efficiency = 75.0
        st.write(f"Comparing with standard cooling water efficiency: {standard_efficiency}%")
        
        # Create a bar chart for graphical representation
        efficiencies = [efficiency, standard_efficiency]
        labels = ['Calculated Efficiency', 'Standard Efficiency']

        fig, ax = plt.subplots()
        ax.bar(labels, efficiencies, color=['blue', 'orange'])
        ax.set_ylim(0, 100)
        ax.set_ylabel('Efficiency (%)')
        ax.set_title('Cooling Tower Efficiency Comparison')
        
        # Display the chart
        st.pyplot(fig)
