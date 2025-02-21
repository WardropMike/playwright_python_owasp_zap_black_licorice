# tool_bench/tools_processing.py
def greet(name):  # Matches your original File 2
    return f"Hello, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):  # Added for sec_analsys_check.py
        return a * b

def convert_temperature(temp, units):
    """
    Convert temperature between Celsius and Fahrenheit.
    """
    unit = units.lower()
    if unit == "c":
        temp_to_convert = (temp * 1.800) + 32
        f_temp = float("{:.2f}".format(temp_to_convert))
        return f_temp, "°F"
    elif unit == "f":
        temp_to_convert = (temp - 32) / 1.800
        c_temp = float("{:.0f}".format(temp_to_convert))
        return c_temp, "°C"
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")
