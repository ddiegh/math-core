
from .matrix import Matriz
from .vector import Vector

def solve(A:Matriz, B:Matriz, metodo="qr") -> Matriz:
    """
    Funcion para resolver sistemas de ecuaciones
    """
