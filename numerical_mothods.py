import math
import numpy as np

def f(x, v0, theta, g):
    theta_rad = math.radians(theta)
    return x * math.tan(theta_rad) - (g * x ** 2) / (2 * v0 ** 2 * math.cos(theta_rad)**2)

def bisection(f, a, b, tol, v0, theta, g):
    if f(a, v0, theta, g) * f(b, v0, theta, g) >= 0:
        raise ValueError("Bisection method requires opposite signs at the interval endpoints.")

    while abs(b - a) >= tol:
        c = (a + b) / 2

        if abs(f(c, v0, theta, g)) < tol:
            return c

        if f(a, v0, theta, g) * f(c, v0, theta, g) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def false_position(f, a, b, tol, n, v0, theta, g):
    if f(a, v0, theta, g) * f(b, v0, theta, g) >= 0:
        raise ValueError("False Position method requires opposite signs at the interval endpoints.")

    for _ in range(n):
        fa = f(a, v0, theta, g)
        fb = f(b, v0, theta, g)

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c, v0, theta, g)

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    return c


def f_derivative(x, v0, theta, g):
    theta_rad = math.radians(theta)
    return math.tan(theta_rad) - (g * x) / (v0 ** 2 * math.cos(theta_rad) ** 2)


def newton_raphson(f, f_derivative, x0, tol, n, v0, theta, g):
    x = x0

    for _ in range(n):
        fx = f(x, v0, theta, g)
        fpx = f_derivative(x, v0, theta, g)

        if fpx == 0:
            return None

        x_new = x - fx / fpx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return None


def secant_method(f, x0, x1, tol, n, v0, theta, g):
    for _ in range(n):
        f_x0 = f(x0, v0, theta, g)
        f_x1 = f(x1, v0, theta, g)

        denominator = f_x1 - f_x0
        if denominator == 0:
            return None

        x_new = x1 - f_x1 * (x1 - x0) / denominator

        if abs(x_new - x1) < tol:
            return x_new

        x0, x1 = x1, x_new

    return None


def g_function(x, v0, theta, g):
    theta_rad = math.radians(theta)
    return (2 * v0 ** 2 * math.cos(theta_rad) ** 2 * math.tan(theta_rad)) / g


def successive_approximation(x0, tol, n, v0, theta, g):
    x = x0
    for _ in range(n):
        x_new = g_function(x, v0, theta, g)

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return None


# Parameters
v0 = 20
theta = 45
g = 9.8
tol = 1e-6
n = 100
a = 1
b = 50

initial_guess = 50
initial_guess_1 = 10
initial_guess_2 = 50

# Run methods
R_B = bisection(f, a, b, tol, v0, theta, g)
R_F = false_position(f, a, b, tol, n, v0, theta, g)
R_N = newton_raphson(f, f_derivative, initial_guess, tol, n, v0, theta, g)
R_Se = secant_method(f, initial_guess_1, initial_guess_2, tol, n, v0, theta, g)
R_Su = successive_approximation(initial_guess, tol, n, v0, theta, g)

# Print results
print(f"Bisection Method: {R_B:.15f} m")
print(f"False Position Method: {R_F:.15f} m")
print(f"Newton-Raphson Method: {R_N:.15f} m")
print(f"Secant Method: {R_Se:.15f} m")
print(f"Successive Approximation: {R_Su:.15f} m")
