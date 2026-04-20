#implementamos en metodo de gauss-jordan para escalonar una matriz

from .matrix import Matriz
from .vector import Vector


def triang_sup(A: 'Matriz') -> 'Matriz':
    """
    Triangulariza una matriz cuadrada hacia su forma triangular superior
    mediante eliminación gaussiana.

    Args:
        A (Matriz): matriz cuadrada a triangularizar.

    Returns:
        Matriz: matriz triangular superior equivalente a A.

    Raises:
        ValueError: si la matriz no es cuadrada.
    """
    if A.columnas != A.renglones:
        raise ValueError("Solo se aceptan matrices cuadradas.")

    g = [renglon for renglon in A]
    n = A.columnas

    for i in range(n):
        valor = g[i][i]

        # Hacemos 1 en la diagonal (si el pivote no es 0)
        if valor != 0:
            g[i] = list(Vector(g[i]) * (1 / valor))

        # Eliminamos los elementos debajo del pivote
        for k in range(i + 1, n):
            factor = g[k][i]
            g[k] = list(Vector(g[k]) - factor * Vector(g[i]))

    return Matriz(g)


def triang_inf(A: 'Matriz') -> 'Matriz':
    """
    Triangulariza una matriz cuadrada hacia su forma triangular inferior
    mediante eliminación gaussiana.

    Args:
        A (Matriz): matriz cuadrada a triangularizar.

    Returns:
        Matriz: matriz triangular inferior equivalente a A.
    """
    return triang_sup(A.t).t


def diag_gaussian(A: 'Matriz') -> 'Matriz':
    """
    Diagonaliza una matriz cuadrada mediante eliminación gaussiana completa
    (triangulación superior e inferior).

    Args:
        A (Matriz): matriz cuadrada a diagonalizar.

    Returns:
        Matriz: matriz diagonal equivalente a A.
    """
    return triang_inf(triang_sup(A))




