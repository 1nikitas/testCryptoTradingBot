import math


def isclose(a, b, rel_tol=1e-9):
    """Сравнивает два числа с заданной погрешностью."""
    return math.isclose(a, b, rel_tol=rel_tol)
