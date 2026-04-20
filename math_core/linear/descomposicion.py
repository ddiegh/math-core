from .matrix import Matriz
from .algoritm import gram_schmidt

def qr(A: 'Matriz') -> tuple['Matriz', 'Matriz']:
    """
    Descomposición QR de una matriz usando Gram-Schmidt.

    Args:
        A (Matriz): matriz a descomponer.

    Returns:
        tuple[Matriz, Matriz]: par (Q, R) donde Q es ortogonal y R es
                               triangular superior, tal que A = Q * R.
    """
    Q = gram_schmidt(A)
    R = Q.t * A
    return Q, R
