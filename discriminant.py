"""Finds the number of real roots that a quadratic equation has."""


def checkDiscriminant(a, b, c):
    """Check the discriminant of a quadratic function."""
    disc = (b**2)-4*a*c
    if disc > 0:
        roots = 2
    if disc < 0:
        roots = 0
    else:
        roots = 1
    return("This equation has " + str(roots) + " real roots.")

print(checkDiscriminant(-2, -7, 4))
