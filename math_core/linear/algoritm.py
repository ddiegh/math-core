#en este archivo algunos algoritmos que podemoa ocupar en matrices

from .matrix import Matriz
from .vector import Vector


def gram_schmidt(A:Matriz, norm:bool= True):
    """
    Realiza el proceso de ortogonalizacion de Gram-Schmidt en una matriz 

    Args:
        A(Matriz): La matriz que queremos hacer ortogonal
        norm(bool): False si no queremos que sea ortonormal
    """
    #transponemos para tener vectores acostados 
    At = A.t
    A_ort = [At.matriz[0]]    #primer vector se queda igual

    for i in range(1,At.renglones):
        proy = Vector([0.0]* At.columnas)    #vector de proyecciones (inicia con puros ceros)
        vector_vi = Vector(At.matriz[i])
        #proyectamos vi sobre cada Uj
        for j in range(i):
            vector_uj = Vector(A_ort[j])
            proy = proy + vector_vi.proy(vector_uj)   #sumamos todas las proyecciones
        #el nuevo vector ortogonal es vi - la suma de las proyecciones (formula gram-schmit)
        nuevo_renglon = list(Vector(vector_vi - proy))   
        
        A_ort.append(nuevo_renglon)
    #si pedimos ortogonalizar, divimos cada vector ortogonal entre su norma
    if norm == True:
        matriz_ortogonal = [list(Vector(v).normal) for v in A_ort]
    else:
        matriz_ortogonal = A_ort
    #volvemos a trasponer para dejarla como al inicio (ahora ya ortogonal)
    return Matriz(matriz_ortogonal).t





