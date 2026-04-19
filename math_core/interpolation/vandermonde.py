from math_core.linear.matrix import Matriz

def vandermonde_matriz(x:list[float]):
    """
    Dada una lista de datos, se crea la matriz de vandermonde

    Args:
        x(list): datos iniciales
    Returns:
        vandermonde(Matriz): la matriz de vandermonde
    """
    n = len(x)
    A = [[1]*n,
        x]

    for i in range(2,n):
        A.append([xj**i for xj in x])
    V = Matriz(A)

    return V.t