
def raiz(x:float)-> float | complex:
    """
    Calcula la raiz de un numero
    
    Admite raices complejas
    """
    if x<0:
        return complex(x**0.5)   #dato nativo de python que tiene todo lo relacionado a complejos
    return x**0.5


def arange(inicio: float, fin: float, paso: float) -> list[float]:
    """Genera una lista de valores espaciados uniformemente."""
    valores = []
    t = inicio
    while t <= fin + paso:
        valores.append(round(t, 10))  # round evita errores de punto flotante
        t += paso
    return valores

# linspace obtenido de (https://code.activestate.com/recipes/579000/)

import collections.abc
import numbers

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
    


def evaluar_pol(x: float, coefs: list[float]) -> float:
    """
    Evaluación de un polinomio en un punto x.

    El polinomio se expresa como:
        p(x) = coefs[0] + coefs[1]*x + coefs[2]*x² + ... + coefs[n]*xⁿ

    Ejemplo:
        Para y = 2x² - 3x + 5  →  coefs = [5, -3, 2]

        evaluar_pol(3, [5, -3, 2])
        >>> 5 + (-3)*3 + (2)*3² = 5 - 9 + 18 = 14

    Args:
        x     (float): valor donde se evalúa el polinomio.
        coefs  (list): coeficientes ordenados de menor a mayor grado,
                       es decir [término independiente, ..., coef. de xⁿ].

    Returns:
        float: valor del polinomio evaluado en x.
    """
    return sum(c * (x ** i) for i, c in enumerate(coefs))