#en este archivo algunos algoritmos que podemoa ocupar en matrices

from .matrix import Matriz
from .vector import Vector


def gram_schmidt(A: 'Matriz', norm: bool = True) -> 'Matriz':
    """
    Realiza el proceso de ortogonalización de Gram-Schmidt en una matriz.

    Args:
        A    (Matriz): matriz sobre la que se aplica el proceso.
        norm  (bool) : si es True, normaliza los vectores (ortonormal).
                       si es False, solo los ortogonaliza. Default: True.

    Returns:
        Matriz: matriz ortogonal u ortonormal, del mismo tamaño que A.
    """
    # Transponemos para trabajar con vectores como renglones
    At = A.t
    A_ort = [At.matriz[0]]  # el primer vector se queda igual

    for i in range(1, At.renglones):
        proy = Vector([0.0] * At.columnas)  # acumulador de proyecciones
        vector_vi = Vector(At.matriz[i])

        # Proyectamos vi sobre cada uj ya ortogonalizado
        for j in range(i):
            vector_uj = Vector(A_ort[j])
            proy = proy + vector_vi.proy(vector_uj)

        # Nuevo vector ortogonal: vi menos la suma de proyecciones
        nuevo_renglon = list(Vector(vector_vi - proy))
        A_ort.append(nuevo_renglon)

    # Normalizamos si se pidió
    if norm:
        matriz_ortogonal = [list(Vector(v).normal) for v in A_ort]
    else:
        matriz_ortogonal = A_ort

    # Volvemos a transponer para dejar la matriz en su orientación original
    return Matriz(matriz_ortogonal).t





