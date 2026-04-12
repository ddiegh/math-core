from .matrices import Matriz
from .algoritm import gram_schmidt

def qr(A:Matriz):
    """
    Descomposicion QR para una matriz, usando Gram-Schmit

    Args: 
        A(Matriz): La matriz que queremos descomponer
        norm(bool): true si queremos que la matriz Q sea ortonormal
    """
    Q = gram_schmidt(A)
    R = (Q.t)*A
    return Q,R