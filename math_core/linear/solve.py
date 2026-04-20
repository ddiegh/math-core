
from .matrix import Matriz
from .vector import Vector

def solve(A:Matriz, B:Matriz, metodo="qr") -> Matriz:
    """
    Funcion para resolver sistemas de ecuaciones
    """

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