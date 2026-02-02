# Ohm's Law Calculator
voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

if resistance != 0:
    current = voltage / resistance
    print("Current (A):", current)
else:
    print("Error: Resistance cannot be zero")