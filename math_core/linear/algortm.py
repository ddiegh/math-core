from .matrices import Matriz
from .vectores import Vector

import collections.abc
import numbers

from math import pi, sin
import matplotlib.pyplot as plt


#en este archivo algunos algoritmos que podemoa ocupar en matrices

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



def gram_schmidt(A:Matriz, norm:bool= False):
    """
    Realiza el proceso de ortogonalizacion de Gram-Schmidt en una matriz 

    Args:
        A(Matriz): La matriz que queremos hacer ortogonal
        norm(bool): True si queremos que sea ortonormal
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
    if norm:
        matriz_ortogonal = [list(Vector(v).normal) for v in A_ort]
    else:
        matriz_ortogonal = A_ort
    #volvemos a trasponer para dejarla como al inicio (ahora ya ortogonal)
    return Matriz(matriz_ortogonal).t

def qr(A:Matriz, norm = False):
    """
    Descomposicion QR para una matriz, usando Gram-Schmit

    Args: 
        A(Matriz): La matriz que queremos descomponer
        norm(bool): true si queremos que la matriz Q sea ortonormal
    """
    Q = gram_schmidt(A,norm)
    R = Q.t*A
    return Q,R

# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(collections.abc.Sequence):
    """linspace(start, stop, num) -> linspace object
    
    Return a virtual sequence of num numbers from start to stop (inclusive).
    
    If you need a half-open range, use linspace(start, stop, num+1)[:-1].
    """
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                        self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  


def eigenvalous(A:Matriz, n:int=100)->list[float]:
    """
    Algoritmo para encontrar los valores propios de una matriz
    Args:
        A(Matriz): Matriz que queremos saber sus eigenvalores
        n = cantidad de iteraciones
    Returns:
        eigenvalores(list): los valores propios de la matriz
    """
    A_k = A
    for _ in range(n):
        Q,R = qr(A_k, True)
        A_k = R*Q
    val = [round(A_k.matriz[i][i]) for i in range(A.renglones)]
    return val

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

def interpolar(points:list[float], values:list[float]):
    """
    Dada una lista de datos con sus sus valores, obtenemos los coeficientes del polinomio con el que podemos interpolar los datos

    Args:
        points(list): datos dependientes
        values(list): datos que dependen de values
    
    Returns:
        coeficientes(Matriz): los coeficientes del polinomio con el que podemos interpolar los datos
    """
    A = vandermonde_matriz(points)
    Q,R = qr(A)
    sol = sol_triangular_sup(R, Q.t * values)
    return sol

def evaluar_pol(x, coefs):
    """
    Evaluacion de un polimio

    Args:
        x: los valores en donde evaluaremos el polinomio
        coefs: coeficientes del polinomio
    """
    # Sumamos cada coeficiente multiplicado por x elevado a su posición (índice)
    return sum(c * (x**i) for i, c in enumerate(coefs))

def interpolar_sin(n:int):
    """Recibe la cantidad de puntos a interpolar la función seno y grafica"""
    lim_inf:float = 0
    lim_sup:float = 2 * pi

    points = linspace(lim_inf, lim_sup, n)

    puntos = list(points)
    values = [sin(p) for p in puntos]

    #obtener los coeficientes del polinomio 
    coeficientes = interpolar(puntos,values)
    #desempaquetar 
    coef = [fila[0] for fila in coeficientes]

    #graficamos los n puntos
    plt.figure(figsize=(12,8))
    plt.scatter(puntos, values, c='black', label=f'{n} puntos bases')
    #evaluamos un linespace en el polinomio (500 puntos) para que se vea bien
    dom = list(linspace(lim_inf, lim_sup, 500))
    y_interpolado = [evaluar_pol(xi,coef) for xi in dom]

    plt.plot(dom,y_interpolado, c='red', label = 'interpolacion')
    plt.title("Interpolacion de la funcion seno")
    plt.legend()
    plt.show()
    return 



