def rls(x: list[float], y: list[float]) -> tuple[float, float]:
    """
    Calcula los parámetros de la regresión lineal simple mediante mínimos cuadrados.

    Args:
        x (list[float]): valores de la variable independiente.
        y (list[float]): valores de la variable dependiente.

    Returns:
        tuple[float, float]: par (b, m) donde b es el intercepto y m la pendiente,
                             tal que y = b + m*x.
    """
    n = len(x)
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(xi * yi for xi, yi in zip(x, y))
    suma_x2 = sum(xi ** 2 for xi in x)

    m = (n * suma_xy - suma_y * suma_x) / (n * suma_x2 - suma_x ** 2)
    b = suma_y / n - m * (suma_x / n)

    return b, m