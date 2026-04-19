#implementamos en metodo de gauss-jordan para escalonar una matriz

from .matrix import Matriz
from .vector import Vector

def triang_sup(A:Matriz):
    if A.columnas != A.renglones:
        return "solo puedo con matrices cuadradas"
    g = [renglones for renglones in A]
    n = A.columnas
    #primero hacemos 1 en la diagonal
    for i in range(n):
        valor = g[i][i]
        if valor == 0:
            g[i] = g[i]
        else:
            g[i] = list(Vector(g[i])*(1/valor))

        for k in range(i+1,n):
            factor = g[k][i]
            renglon = list(Vector(g[k]) - factor*Vector(g[i]))
            g[k]=renglon
    return Matriz(g)

def triang_inf(A:Matriz):
    At = A.t
    return triang_sup(At).t

def diag_gaussian(A:Matriz):
    triangular = triang_sup(A)
    diagonal = triang_inf(triangular)

    return diagonal 




