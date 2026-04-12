
def raiz(x:float)-> float | complex:
    """
    Calcula la raiz de un numero
    
    Admite raices complejas
    """
    if x<0:
        return complex(x**0.5)   #dato nativo de python que tiene todo lo relacionado a complejos
    return x**0.5