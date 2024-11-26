import ipywidgets as widgets
from IPython.display import display, clear_output

def calculate_cooling_tower_efficiency(T_in, T_out, T_wb):
    """Calculate the efficiency of a cooling tower."""
    if T_in <= T_wb:
        return "Error: Inlet temperature must be greater than wet bulb temperature."
    if T_out >= T_in:
        return "Error: Outlet temperature must be less than inlet temperature."
    
    efficiency = (T_in - T_out) / (T_in - T_wb) * 100
    return f"The efficiency of the cooling tower is: {efficiency:.2f}%"

def on_button_click(b):
    clear_output()  # Clear previous output
    display(widgets.VBox([inlet_temp, outlet_temp, wet_bulb_temp, calculate_button, output]))
    
    try:
        T_in = float(inlet_temp.value)
        T_out = float(outlet_temp.value)
        T_wb = float(wet_bulb_temp.value)
        
        result = calculate_cooling_tower_efficiency(T_in, T_out, T_wb)
        output.value = result
    
    except ValueError:
        output.value = "Error: Please enter valid numeric values."

# Create input widgets
inlet_temp = widgets.FloatText(description='Inlet Temp (°C):')
outlet_temp = widgets.FloatText(description='Outlet Temp (°C):')
wet_bulb_temp = widgets.FloatText(description='Wet Bulb Temp (°C):')
calculate_button = widgets.Button(description='Calculate Efficiency')
output = widgets.Textarea(description='Result:', disabled=True)

# Attach the button click event
calculate_button.on_click(on_button_click)

# Display the widgets
display(widgets.VBox([inlet_temp, outlet_temp, wet_bulb_temp, calculate_button, output]))
