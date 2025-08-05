import numpy as np
import matplotlib.pyplot as plt

# === Step 1: Initial Values ===
v0 = 30  # Initial velocity (m/s)
theta = 45  # Launch angle (degrees)
g = 9.8  # Acceleration due to gravity (m/s^2)

# Convert angle to radians
theta_rad = np.radians(theta)

# Time of flight (till it hits the ground)
T = (2 * v0 * np.sin(theta_rad)) / g

# Time points
t = np.linspace(0, T, num=100)

# === Step 2: Equations of Motion ===
x = v0 * np.cos(theta_rad) * t
y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

# === Step 3: Plot the Trajectory ===
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("Projectile Motion Simulation")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.ylim(bottom=0)
plt.show()
