import numpy as np
import matplotlib.pyplot as plt

# === Step 1: Constants and initial values ===
g = 9.8               # Gravity (m/s^2)
L = 1.0               # Length of pendulum (m)
m = 0.2               # Mass of bob (kg)
theta0 = np.radians(10)  # Initial angle in radians

# === Step 2: Time setup ===
t = np.linspace(0, 10, 500)   # Time array (0 to 10 sec)

# === Step 3: Angle and Angular Velocity ===
omega = np.sqrt(g / L)                  # Angular frequency
theta = theta0 * np.cos(omega * t)      # Angle as function of time
dtheta_dt = -theta0 * omega * np.sin(omega * t)   # Angular velocity

# === Step 4: Calculate quantities ===
# Force restoring towards center
F = -m * g * np.sin(theta)

# Angular acceleration
alpha = -g / L * np.sin(theta)

# Linear velocity of bob
v = L * dtheta_dt

# Height of bob from lowest point
h = L * (1 - np.cos(theta))

# Energies
KE = 0.5 * m * v**2             # Kinetic Energy
PE = m * g * h                  # Potential Energy
TE = KE + PE                    # Total Energy (should remain constant)

# === Step 5: Plot Energies ===
plt.figure(figsize=(10, 6))
plt.plot(t, KE, label='Kinetic Energy (KE)', color='green')
plt.plot(t, PE, label='Potential Energy (PE)', color='orange')
plt.plot(t, TE, label='Total Energy (TE)', color='red', linestyle='--')

plt.xlabel("Time (s)")
plt.ylabel("Energy (Joules)")
plt.title("Pendulum Energies Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
