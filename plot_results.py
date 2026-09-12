import math
import numpy as np
import matplotlib.pyplot as plt


# Projectile trajectory function
def f(x, v0, theta, g):
    theta_rad = math.radians(theta)

    return (
        x * math.tan(theta_rad)
        - (g * x**2)
        / (2 * v02 * math.cos(theta_rad)2)
    )


# Physical parameters
v0 = 20          # Initial velocity (m/s)
theta = 45       # Launch angle (degrees)
g = 9.8          # Gravitational acceleration (m/s^2)


# Numerical roots obtained from the five methods
roots = {
    "Bisection": 40.81549145281315,
    "False Position": 40.81632609056563,
    "Newton-Raphson": 40.81632653061226,
    "Secant": 40.816326530612244,
    "Successive Approximation": 40.81632653061225
}


# ---------------------------------------------------------
# Plot 1: Projectile trajectory
# ---------------------------------------------------------

x = np.linspace(0, 42, 1000)
y = f(x, v0, theta, g)

plt.figure(figsize=(8, 5))

plt.plot(x, y, label="Projectile trajectory")

for method, root in roots.items():
    plt.scatter(
        root,
        f(root, v0, theta, g),
        s=70,
        label=method
    )

plt.axhline(0, linestyle="--", linewidth=1)

plt.xlabel("Horizontal distance, x (m)")
plt.ylabel("Vertical position, y (m)")
plt.title("Projectile Motion and Numerical Roots")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("figures/projectile_motion.png", dpi=300)
plt.show()


# ---------------------------------------------------------
# Plot 2: Comparison of numerical roots
# ---------------------------------------------------------

methods = list(roots.keys())
root_values = list(roots.values())

plt.figure(figsize=(9, 5))

plt.bar(methods, root_values)

plt.ylabel("Root x (m)")
plt.xlabel("Numerical Method")
plt.title("Comparison of Numerical Root-Finding Methods")

plt.xticks(rotation=20)
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("figures/root_comparison.png", dpi=300)
plt.show()
