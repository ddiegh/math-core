def rls(x: list[float], y: list[float]) -> tuple[float,float]: 
    """
    Calcula los parámetros de la Regresión Lineal Simple mediante mínimos cuadrados.
    Args:
        x (list[float]): Lista de valores de la variable independiente.
        y (list[float]): Lista de valores de la variable dependiente.

    Returns:
        m,b tuple[float, float]: Un par (b, m) que representa la ordenada y la pendiente.
    """
    #tamaño de los datos
    n = len(x)
    #ocuamos las formulas 
    suma_x = sum(x)
    suma_y = sum(y)

    xy = [xi * yi for xi,yi in zip(x,y)]
    suma_xy = sum(xy)

    suma_x2 = sum(xi ** 2 for xi in x)

    m = (n*suma_xy-(suma_y*suma_x))/(n*suma_x2-(suma_x**2))
    b = suma_y/n - m*(suma_x/n)

    return b,m