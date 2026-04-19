# Metodo de Euler para una ecuacion diferencial
Cuando tenemos una ecuacion diferencial  $\frac{dy}{dt} = f(t, y)$ podemos pasarlo a una ecuación en diferencias de la forma:

$$\frac{\Delta y}{\Delta t} = \frac{y_{n+1} - y_n}{t_{n+1} - t_n} = f(t, y)$$

Despejando obtenemos $$\Delta y = f(t, y) \cdot \Delta t$$ es decir $$y_{n+1} - y_n = f(t, y) \cdot \Delta t$$

Finalmente, llegamos a la **ecuación recursiva** 

*$$y_{n+1} = y_n + f(t, y) \cdot \Delta t$$*

Esta forma de discretizar ecuaciones diferenciales se llama *metodo de Euler* y nos permite realizar el cálculo computacional de una forma más sencilla. 

Despues de considerar ecuaciones podemos pensar en sistemas de ecuaciones diferenciales, en las que tenemos relacion entre ellas

## Sistemas de 2 Ecuaciones Diferenciales

Un sistema de ecuaciones diferenciales de primer orden (lineales) describe la interacción simultánea entre ellas. A diferencia de una ecuación única, aquí el cambio de una ecuacion depende no solo del tiempo, sino también del estado de la otra ecuacion (o variable).

Un sistema general de dos ecuaciones diferenciales de primer orden se ve de la forma:

$$
\begin{cases} 
\dfrac{dx}{dt} = f(t, x, y) \\ 
\dfrac{dy}{dt} = g(t, x, y) 
\end{cases}
$$

Donde:
* **$t$**: Variable independiente (usualmente el tiempo).
* **$x(t), y(t)$**: Variables de estado del sistema (ej. poblaciones, voltajes, concentraciones).
* **$f, g$**: Funciones que definen la dinámica o tasa de cambio para cada variable.

---

### Discretización: Método de Euler 

Para resolver estos modelos mediante **Ecuaciones en Diferencias Finitas (FDE)**, el proceso es el mismo que con una sola ecuacion, solo que ahora se tiene que hacerlo en las dos ecuaciones. El estado del sistema en el paso $n+1$ se calcula a partir del estado actual $n$:

1.**$$x_{n+1} = x_n + f(t_n, x_n, y_n) \cdot \Delta t$$**

2. **$$y_{n+1} = y_n + g(t_n, x_n, y_n) \cdot \Delta t$$**




## Sistemas de $n$ Ecuaciones Diferenciales

Para modelar sistemas complejos extendemos el concepto a un conjunto de $n$ ecuaciones diferenciales acopladas, y todo sigue funcionando de la misma forma solo que ahora tenemos vectores.

Un sistema de $n$ ecuaciones se representa de forma compacta mediante vectores de estado:

$$\frac{d\mathbf{u}}{dt} = \mathbf{f}(t, \mathbf{u})$$

Donde:
* $\mathbf{u} = [u^{(1)}, u^{(2)}, \dots, u^{(n)}]^T$ es el **vector de estado**.
* $\mathbf{f} = [f^{(1)}, f^{(2)}, \dots, f^{(n)}]^T$ es el **vector de funciones**.

De forma expandida, utilizando superíndices para las variables, el sistema se ve así:

$$
\begin{cases} 
\dfrac{du^{(1)}}{dt} = f^{(1)}(t, u^{(1)}, u^{(2)}, \dots, u^{(n)}) \\ 
\dfrac{du^{(2)}}{dt} = f^{(2)}(t, u^{(1)}, u^{(2)}, \dots, u^{(n)}) \\ 
\vdots \\
\dfrac{du^{(n)}}{dt} = f^{(n)}(t, u^{(1)}, u^{(2)}, \dots, u^{(n)}) 
\end{cases}
$$

---

La actualización de Euler se aplica a todo el vector simultáneamente. Para un paso de tiempo $i$ hacia el siguiente $i+1$, la expresión para cada componente $j$ es:

$$u_{i+1}^{(j)} = u_{i}^{(j)} + f^{(j)}(t_i, \mathbf{u}_i) \cdot \Delta t$$

O en su forma puramente vectorial, que simplifica el cálculo computacional:

$$\mathbf{u}_{i+1} = \mathbf{u}_i + \mathbf{f}(t_i, \mathbf{u}_i) \cdot \Delta t$$

> * El **superíndice $(j)$** identifica la ecuación diferencial (la variable de estado).
> * El **subíndice $i$** identifica el paso en la tiempo.

---
> [!IMPORTANT]
> **Acoplamiento:** En cada iteración, ambas variables deben actualizarse utilizando los valores del paso anterior ($x_n, y_n$). Esto asegura que la interacción sea simultánea y no secuencial.