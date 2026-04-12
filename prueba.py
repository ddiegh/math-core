from math_core import linear as ln
 
A = ln.matrices.Matriz([[1,-1,4],
                        [1,4,-2],
                        [1,4,2],
                        [1,-1,0]])
q,r = ln.descomposicion.qr(A)



print(q*r)