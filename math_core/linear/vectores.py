#en este archivo construimos algunas propiedades de los vectores (suma, multiplicacion escalar, norma, etc)
#lo trate de documentar un poco para que no se me olvide como usar cada cosa 

from math_core.base.operaciones import raiz

class Vector:
    def __init__(self, v:list[float]):
        self.v = v

    #hacemos que nuestro objeto (vector) sea iterable
    def __iter__(self):
        return iter(self.v)
    
    #formateamos para poder imprimir los vectores
    def __str__(self):
        return f"{self.v}"
    
    #nos permite usar len(v) para saber su dimension
    def __len__(self):
        return len(self.v)
    
    def __add__(self, u:list[float]):
        """
        Suma de dos vectores

        Example:
            >>> v = Vector([1,2])
        >>> u = [3,2]
        >>> suma = v+u
        >>> print(suma)
            [4,4]
        """
        if len(self.v)!=len(u):
            raise ValueError("los vectores no son del mismo tamaño")
        return Vector([vi+ui for vi,ui in zip(self.v,u)])
    
    def __sub__(self, u:list[float]):
        """
        La resta entre dos vectores

        Example:
            >>> v = Vector([1,2])
        >>> u = [3,2]
        >>> suma = v-u
        >>> print(suma)
            [-2,0]
        """
        if len(self.v)!=len(u):
            raise ValueError("los vectores no son del mismo tamaño")
        return Vector([vi-ui for vi,ui in zip(self.v,u)])

    def __mul__(self, c:float):
        """
        Devuelve el vector escalado (v*c)

        Example: 
            >>> v = Vector([1,2])
        >>> print(v*2)
            [2,4]
        """
        return Vector([c*vi for vi in self.v])
    
    def __rmul__(self, c:float):
        """
        Devuelve el vector escalado (nos permite hacelo de forma c*v)

        Example: 
            >>> v = Vector([1,2])
        >>> print(2*v)
            [2,4]
        """
        return self.__mul__(c)
    
    def dot(self, u:list[float])->int:
        """
        Realiza el producto punto de dos vectores.
        Args:
            u(list): vector con el que queremos hacer producto punto
        Returns:
            int: producto punto con u

        Example:
            >>> v = Vector([1,2])
            >>> u = [1,1]
            >>> pp = v.dot(u)
            >>> print(pp)
            3
        """
        if len(self.v)!=len(u):
            raise ValueError("No son del mismo tamaño")
        return sum(vi*ui for vi,ui in zip(self.v,u))   #multiplicamos cada entrada y luego sumamos todo 
    
    @property
    def norma(self)->float:
        """
        Norma del vector

        Example:
            >>> v = Vector([0,3])
        >>> print(v.norma)
            3
        """
        return raiz(self.dot(self.v))
    
    @property
    def normal(self):
        """
        Vector normalizado

        Example:
            >>> v = Vector([4,3])
        >>> print(v.normal)
            [4/5, 3/5]
        """
        if self.norma == 0:
            raise ValueError("No se puede normalizar el vector 0")
        return Vector([(1/self.norma)*vi for vi in self.v])
    
        
    def distancia(self, u:list[float]):
        """
        Distancia Euclideana entre dos vectores

        Example:
            >>> v = Vector([1,2])
        >>> u = [4,2]
        >>> distancia = v.distancia(u)
        >>> print(distancia)
            3

        """
        return (self-u).norma

    def proy(self, u:list[float]):
        """
        Realiza la proyeccion de un vector sobre otro

        Example:
            >>> v = Vector([1,2,3])
        >>> u = [2,1,6]
        >>> p = v.proy(u)
        >>> print(p)
            22/41*[2,1,6]
        """
        #revisamos si el vector u es un objeto de Vector() y si no, lo hacemos uno
        if not isinstance(u,Vector):
            u = Vector(u)
        #revisamos si u es el vector 0
        if u.norma == 0:
            raise ValueError("No hay proyeccion sobre el vector 0")
        
        escalar = self.dot(u)/u.dot(u)
        return escalar*u
