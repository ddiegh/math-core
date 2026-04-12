import sys
import os

ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)

from base.operaciones import raiz 
i = raiz(-1)

print(i**2)

import numpy as np

A = np.array([[1,2],[1,2]])
np.linalg.qr(A)

