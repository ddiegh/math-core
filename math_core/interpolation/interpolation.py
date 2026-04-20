from math_core.interpolation.vandermonde import vandermonde_matriz
from math_core.linear.descomposicion import qr
from math_core.linear.solve import sol_triangular_sup
from math_core.linear.matrix import Matriz

def interpolar(points: list[float], values: list[float]) -> 'Matriz':
    """
    Calcula los coeficientes del polinomio interpolante dado un conjunto
    de puntos y sus valores.

    El polinomio resultante cumple que p(points[i]) == values[i]
    para todo i. Los coeficientes siguen el orden:
        [b, a1, a2, ..., an]  →  p(x) = b + a1*x + a2*x² + ... + an*xⁿ

    Ejemplo:
        interpolar([0, 1, 2], [1, 3, 7])
        >>> coeficientes ≈ [1, 1, 1]  →  p(x) = 1 + x + x²

    Args:
        points (list[float]): valores independientes (x).
        values (list[float]): valores dependientes (y = f(x)).

    Returns:
        Matriz: coeficientes del polinomio interpolante ordenados
                de menor a mayor grado.
    """
    A = vandermonde_matriz(points)
    Q, R = qr(A)
    sol = sol_triangular_sup(R, Q.t * values)

    return sol
