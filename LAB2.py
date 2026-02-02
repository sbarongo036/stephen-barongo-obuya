import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 1000      # Ohms
C = 1e-6      # Farads
V = 5         # Volts
tau = R * C   # Time Constant

# Time array: 0 to 5 * tau (the full discharge period)
t = np.linspace(0, 5 * tau, 1000)
Vc = V * np.exp(-t / tau)

plt.figure(figsize=(8, 5))
plt.plot(t, Vc, label="Capacitor Voltage", color='blue')

# Formatting
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Discharging Curve")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()