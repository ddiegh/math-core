from math_core.linear.matrix import Matriz
from math_core.linear.descomposicion import qr
from math_core.linear.solve import sol_triangular_sup

def regresion(x:list, y:list, grado=1) -> tuple:
    """
    Dada dos listas de datos (independiente y dependiente) devuelve los coeficientes 
    del polinomio para hacer la regresion
    Args:
        x(list): lista de los valores independientes
        y(list): lista de los valores dependientes
        grado(int): tipo de regresion que se desea (default = regresion lineal)

    Returns:
        list: coeficientes del polimio [b,a1,a2...,an]
        b + a1x + a2*x2^2 ... + an*xn^n
    """
    A = []
    for i in range(grado+1):
        A.append([xi**i for xi in x])
    V = Matriz(A).t

    B = Matriz(y)
    Q,R = qr(V)
    sol = sol_triangular_sup(R, Q.t * y )
    coeficientes = [sol.matriz[i][0] for i in range(grado+1)]

    return coeficientes