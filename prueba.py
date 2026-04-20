from math_core.regresion import lineal, polinomial

x = [63, 52, 50, 55, 57, 60, 63, 51] 
y = [80, 45, 37, 67, 58, 79, 89, 46] 

print(lineal.rls(x,y))
print(polinomial.regresion(x,y))



