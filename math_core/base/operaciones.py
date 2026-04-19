
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