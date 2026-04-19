from .matrix import Matriz
from .algoritm import gram_schmidt

def qr(A:Matriz):
    """
    Descomposicion QR para una matriz, usando Gram-Schmit

    Args: 
        A(Matriz): La matriz que queremos descomponer
    """
    Q = gram_schmidt(A)
    R = (Q.t)*A
    return Q,R