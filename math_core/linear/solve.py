
from .matrix import Matriz
from .vector import Vector
from .descomposicion import qr
from .gaussian import diag_gaussian

def sol_triangular_sup(A: 'Matriz', b: 'Matriz') -> 'Matriz':
    """
    Resuelve un sistema de ecuaciones Ax = b donde A es triangular superior,
    mediante sustitución hacia atrás.

    Args:
        A (Matriz): matriz cuadrada triangular superior de tamaño n x n.
        b (Matriz): vector columna de términos independientes de tamaño n x 1.

    Returns:
        Matriz: vector columna x con la solución del sistema, de tamaño n x 1.

    Raises:
        ValueError: si las dimensiones no corresponden a un sistema válido.
    """
    if (A.columnas != b.renglones) or (b.columnas != 1) or (A.columnas != A.renglones):
        raise ValueError("Las dimensiones no corresponden a un sistema válido.")

    n, _ = A.tamaño
    valores = [0.0] * n

    for i in range(n):
        # Índice de atrás hacia adelante
        k = n - i - 1

        # Despejamos la incógnita: (b_k - A_k · valores) / A_kk
        valor = (b.matriz[k][0] - Vector(A.matriz[k]).dot(valores)) / A.matriz[k][k]
        valores[k] = valor

    return Matriz(valores)


def solve(A: 'Matriz', b: 'Matriz', metodo: str = "qr") -> 'Matriz':
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método indicado.

    Args:
        A      (Matriz): matriz de coeficientes cuadrada de tamaño n x n.
        b      (Matriz): vector columna de términos independientes de tamaño n x 1.
        metodo   (str) : método de resolución. Opciones: "qr", "gauss".
                         Default: "qr".

    Returns:
        Matriz: vector columna x con la solución del sistema.

    Raises:
        ValueError: si el método indicado no está soportado.
    """
    if metodo == "qr":
        Q, R = qr(A)
        return sol_triangular_sup(R, Q.t * b)

    if metodo == "gauss":
        diagonal = diag_gaussian(A)
        return sol_triangular_sup(diagonal, b)

    raise ValueError(f"Método '{metodo}' no soportado. Usa 'qr' o 'gauss'.")