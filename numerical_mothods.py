def bisection(f, a, b, tol, v0, theta, g):
    if f(a, v0, theta, g) * f(b, v0, theta, g) >= 0:
        raise ValueError(
            "Bisection method requires opposite signs at the interval endpoints."
        )

    while abs(b - a) >= tol:
        c = (a + b) / 2

        if abs(f(c, v0, theta, g)) < tol:
            return c

        if f(a, v0, theta, g) * f(c, v0, theta, g) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
