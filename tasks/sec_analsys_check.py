# tasks/sec_analsys_check.py
from app_initializer import greet, calc, convert_temperature

# FEATURE "Basic Functionality Test"
    # CONTEXT "Testing imported functions and class methods"
        # SCENARIO "Greet, calculate, and convert temperature"
message = greet("World")
print(message)

result_add = calc.add(5, 3)
result_multiply = calc.multiply(4, 2)
print(f"Addition: {result_add}")
print(f"Multiplication: {result_multiply}")

temp_f, unit_f = convert_temperature(25.0, "C")
temp_c, unit_c = convert_temperature(98.6, "F")
print(f"25°C converts to {temp_f}{unit_f}")
print(f"98.6°F converts to {temp_c}{unit_c}")
