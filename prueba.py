from math_core import linear as ln
import math_core.linear.gaussian as gs
from math_core.linear.matrix import Matriz
from math_core.ode.euler_method import euler_solve


import matplotlib.pyplot as plt
'''A = ln.matrix.Matriz([[1,-1,4],
                        [1,4,-2],
                        [1,4,2],
                        [1,-1,0]])
q,r = ln.descomposicion.qr(A)

A = Matriz([[1,2,3],
            [2,6,1],
            [1,0,4]])
'''

#constante de proporcion de calor 
k = 1/36

#creamos las dos ecuaciones diferenciales
def dP(t, y):
    #y deberia ser una lista con los valor [Pn, Qn]
    P = y[0]
    Q = y[1]
    return k * (Q - P)

def dQ(t, y):
    #y deberia ser una lista con los valor [Pn, Qn]
    P = y[0]
    Q = y[1]
    return -k * (Q - P)

sistema_ecuaciones = [dP, dQ]
condiciones_iniciales = [9, 33]

#simulacion
tiempos, valores = euler_solve(sistema_ecuaciones,condiciones_iniciales, 0, 60, 1)
plt.figure(figsize=(10, 5))
plt.plot(tiempos, valores[0], label="Temperatura P", color="tomato")
plt.plot(tiempos, valores[1], label="Temperatura Q", color="steelblue")
plt.title("Sistema de enfriamiento/calentamiento")
plt.xlabel("Tiempo")
plt.ylabel("Temperatura")
plt.legend()
plt.grid(True)
plt.show()



