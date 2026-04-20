from math_core.linear.matrix import Matriz
from math_core.linear.descomposicion import qr


def eigenvalues(A: 'Matriz', n: int = 100) -> list[float]:
    """
    Calcula los valores propios de una matriz mediante el algoritmo QR iterativo.

    Aplica la descomposición QR repetidamente hasta que la matriz converge
    a una forma triangular, cuyos elementos diagonales son los eigenvalores.

    Args:
        A (Matriz): matriz cuadrada de la que se desean los eigenvalores.
        n   (int) : número de iteraciones. A mayor n, mayor precisión.
                    Default: 100.

    Returns:
        list[float]: eigenvalores de la matriz, extraídos de la diagonal.
    """
    A_k = A
    for _ in range(n):
        Q, R = qr(A_k)
        A_k = R * Q

    return [round(A_k.matriz[i][i]) for i in range(A.renglones)]