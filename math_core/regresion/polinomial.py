from math_core.linear.matrix import Matriz
from math_core.linear.descomposicion import qr
from math_core.linear.solve import sol_triangular_sup

def regresion(x: list[float], y: list[float], grado: int = 1) -> list[float]:
    """
    Calcula los coeficientes del polinomio de regresión de un grado dado,
    usando descomposición QR sobre la matriz de Vandermonde.

    El polinomio resultante tiene la forma:
        p(x) = b + a1*x + a2*x² + ... + an*xⁿ

    Args:
        x     (list[float]): valores de la variable independiente.
        y     (list[float]): valores de la variable dependiente.
        grado       (int)  : grado del polinomio de regresión. Default: 1 (lineal).

    Returns:
        list[float]: coeficientes [b, a1, a2, ..., an] ordenados de menor a mayor grado.
    """
    A = [[xi ** i for xi in x] for i in range(grado + 1)]
    V = Matriz(A).t
    Q, R = qr(V)
    sol = sol_triangular_sup(R, Q.t * Matriz(y))

    return [sol.matriz[i][0] for i in range(grado + 1)]