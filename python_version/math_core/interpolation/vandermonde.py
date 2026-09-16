from math_core.linear.matrix import Matriz

def vandermonde_matriz(x: list[float]) -> 'Matriz':
    """
    Construye la matriz de Vandermonde a partir de una lista de puntos.

    La matriz de Vandermonde tiene la forma:
        [[ 1,  x0,  x0²,  ...,  x0ⁿ ],
        [ 1,  x1,  x1²,  ...,  x1ⁿ ],
        [ 1,  x2,  x2²,  ...,  x2ⁿ ],
        [ ⋮    ⋮    ⋮    ⋱    ⋮         ],
        [ 1,  xn,  xn²,  ...,  xnⁿ ]]

    Args:
        x (list[float]): lista de puntos donde se evalúa el polinomio.

    Returns:
        Matriz: matriz de Vandermonde de tamaño n x n transpuesta.
    """
    n = len(x)
    A = [
        [1] * n,
        x
    ]
    for i in range(2, n):
        A.append([xj ** i for xj in x])

    return Matriz(A).t
