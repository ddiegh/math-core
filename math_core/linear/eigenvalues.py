from math_core.linear.matrix import Matriz
from math_core.linear.descomposicion import qr


def eigenvalous(A:Matriz, n:int=100)->list[float]:
    '''
    Algoritmo para encontrar los valores propios de una matriz
    Args:
        A(Matriz): Matriz que queremos saber sus eigenvalores
        n = cantidad de iteraciones
    Returns:
        eigenvalores(list): los valores propios de la matriz
    '''
    A_k = A
    for _ in range(n):
        Q,R = qr(A_k, True)
        A_k = R*Q
    val = [round(A_k.matriz[i][i]) for i in range(A.renglones)]
    return val
