from math_core.base.operaciones import arange


def euler_solve(
    f: list,
    xo: list[float],
    t_inicio: float,
    t_final: float,
    delta: float
) -> tuple[list[float], list[list[float]]]:
    """
    Resuelve un sistema de ecuaciones diferenciales ordinarias
    utilizando el método de Euler.

    Args:
        f (list): Lista de funciones fi(t, valores) que representan
                cada ecuacion del sistema.
        xo (list[float]): Condiciones iniciales de cada ecuacion.
        t_inicio (float): Tiempo inicial.
        t_final (float): Tiempo final.
        delta (float): Tamaño del paso.

    Returns:
        tiempos (list[float]): Dominio discreto.
        valores (list[list[float]]): Solucion, donde valores[i][j]
                                    es la ecuacion i en el tiempo j.

    Example:
    
        >>> f = [lambda t, v: v[1], lambda t, v: -v[0]]
        >>> tiempos, valores = euler_sistemas(f, [1.0, 0.0], 0, 10, 0.01)
    """
    tiempos = arange(t_inicio, t_final, delta)
    n = len(f)
    pasos = len(tiempos)

    # Lista 2D de ceros [ecuacion][paso]
    valores = [[0.0] * pasos for _ in range(n)]

    # Condiciones iniciales
    for i in range(n):
        valores[i][0] = xo[i]

    # Iteramos para conseguir los siguientes valores
    for j in range(pasos - 1):
        t_actual = tiempos[j]
        valor_actual = [valores[i][j] for i in range(n)]
        for i in range(n):
            valores[i][j + 1] = valor_actual[i] + f[i](t_actual, valor_actual) * delta

    return tiempos, valores