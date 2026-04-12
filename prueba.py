from math_core import linear as ln
import math_core.linear.gaussian as gs
from math_core.linear.matrices import Matriz

A = ln.matrices.Matriz([[1,-1,4],
                        [1,4,-2],
                        [1,4,2],
                        [1,-1,0]])
q,r = ln.descomposicion.qr(A)

A = Matriz([[1,2,3],
            [2,6,1],
            [1,0,4]])



print(gs.triang_sup(A))


