#en este archivo algunos algoritmos que podemoa ocupar en matrices

from .matrix import Matriz
from .vector import Vector

def sol_triangular_sup(A:Matriz, b:Matriz):
    """
    Resuelve un sistema de ecuaciones definido por una matriz triangular superior
    """
    #vereficamos que si sea un sistema de ecuaciones bien definido
    #la matriz es triangular superior entonces tiene que ser cuadrada
    if (A.columnas != b.renglones) or (b.columnas!=1) or (A.columnas!=A.renglones):
        raise ValueError("No podemos resolver el sistema")
    
    n,n = A.tamaño
    #el sistema tiene el mismo numero de incognitas que la cantidad de elementos de b
    #vamos a guardar los valores solucion en esta lista llena de ceros
    valores = [0.0] * n  

    for i in range(n):
        #en cada igualdad, hacemos producto punto del renglon de la matriz con los valores que ya conocemos,
        #los pasamos al otro lado con signo negativo y dividimos entre el coeficiente que tiene nuestra incognita 
        #terminamos, agregando el valor (van de ultimo a primero)
        valor = (b.matriz[n-i-1][0] - Vector(A.matriz[n-i-1]).dot(valores))/A.matriz[n-i-1][n-i-1]
        valores[n-i-1] = valor
    return Matriz(valores)



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


"""def eigenvalous(A:Matriz, n:int=100)->list[float]:
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
    return val"""

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




