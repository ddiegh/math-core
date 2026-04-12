#En este archivo se hacen crean algunas propiedas de las matrices

class Matriz:
    def __init__(self, matriz:list):
        if isinstance(matriz[0], list):
            #matrices bien 
            self.matriz = matriz
        else:
            #matrices 1D A=[1,2,3]
            self.matriz = [[elemento] for elemento in matriz]

    def __iter__(self):
        return iter(self.matriz)

    def __str__(self):
        """
        Formatea la matriz para que se vea como un arreglo matemático
        """
        filas_como_texto = [str(renglon) for renglon in self.matriz]
        return "\n".join(filas_como_texto)

    def __len__(self):
        return len(self.matriz)
    
    #tamaño de una matriz (n,m) = nxm
    @property
    def renglones(self):
        return len(self)
    
    @property
    def columnas(self):
        return len(self.matriz[0])
    
    @property
    def tamaño(self):
        return (self.renglones, self.columnas)
    
    def __add__(self, B:list[list[float]]):
        """
        Suma de dos matrices 

        Example:
            >>> A = Matriz([[1,2], [2,1]])
        >>> B = [[1,0], [0,1]]
        >>> suma = A+B
        >>> print(suma)
            [[2,2],
            [2,2]]
        """
        if not isinstance(B,Matriz):   #checamos si la matriz es un objeto de la clase para evitar errores despues
            B = Matriz(B)
        #las matrices deben ser de las mismas dimensiones
        if (self.renglones != B.renglones) or (self.columnas != B.columnas):
            raise ValueError("No se pueden sumar las matrices")
        
        suma = []
        for i in range(self.renglones):
            s_renglon = []
            for j in range(self.columnas):
                s_renglon.append(self.matriz[i][j] + B.matriz[i][j])
            suma.append(s_renglon)
        return Matriz(suma)
    
    def escalar(self, c:float):
        """
        Multiplicacion escalar 

        Example:
            >>> A = Matriz([[1,2], [2,1]])
        >>> c = 2
        >>> esc = A.escalar(c)
        >>> print(esc)
        [[2,4],
        [4,2]]
        """
        mult = []
        for i in range(self.renglones):
            m_renglon = []
            for j in range(self.columnas):
                m_renglon.append(c*self.matriz[i][j])
            mult.append(m_renglon)
        return Matriz(mult)
    
    def __mul__(self, B:list[list[float]]):
        """
        Realiza la multiplicacion de dos matrices utilizando el operador logico *

        Example:
            >>> A = Matriz([[1,2], [2,1]])
            >>> B = Matriz([[1,0],[0,1]])
            >>> mult = A*B
            >>> print(mult)
            [[1,2],
            [2,1]]
        """
        if not isinstance(B, Matriz):
            B = Matriz(B)

        if self.columnas != B.renglones:
            raise ValueError("No se pueden multiplicar las matrices")
        
        #multiplicacion por un vector columna
        if B.columnas == 1:
            mult = []
            for i in range(self.renglones):
                valor = 0
                for k in range(self.columnas):
                    valor += self.matriz[i][k]*B.matriz[k][0]
                mult.append([valor])
            return Matriz(mult)
        #multiplicacion por un matrices
        else:
            mult = []
            for i in range(self.renglones):   #fijamos un renglon de A
                renglon = []
                for j in range(B.columnas):   #fijamos una columna de B
                    value = 0
                    for k in range(self.columnas):  #recorremos los valores y hacemos la multiplicacion
                        value += self.matriz[i][k] * B.matriz[k][j]
                    renglon.append(value)
                mult.append(renglon)
            return Matriz(mult)
    
    @property
    def t(self):
        '''
        Realiza la transpuesta de una matriz.

        Example:
            >>> A = Matriz([[1,2], [3,4]])
            >>> At = A.t
            >>> print(At)
            [[1,3],
            [2,4]]
        '''
        At = []  
        #los vectores acostados deben tener la misma cantidad de elementos, entonces escogemos el primero para saber la cantidad de columnas de la matriz 
        for i in range(self.columnas):
            renglon = []
            for j in range(self.renglones):
                renglon.append(self.matriz[j][i])
            At.append(renglon)

        return Matriz(At)
