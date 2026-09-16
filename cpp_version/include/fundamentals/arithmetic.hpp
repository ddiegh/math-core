#pragma once 
#include <functional>

/*
* @brief Calcula la raiz de un numero real positivo. 
*
*Utiliza el metodo de Newton-Raphson para calcular la raiz.
*/
double raiz(double x);


/*
* @brief Calcula el valor absoluto de un numero real.
*
*
*/
double absoluto(double x);

/*
* @brief Devuelve el signo de un numero.
*
* Devuelve 1.0 si x>0, -1.0 si x<0 o 0.0 si x = 0
* para poder hacer cosas con signo(x) * x. 
*/
double signo(double x);


/*
* @brief Eleva x a la k.
*/
double elevar(double x, int k);


/*
* @brief Calcula ln(x)
* 
* Utiliza division del problema a ln de un numero muy cercano a 1 el cual podemos calcular, posteriormente 
* multilicamos hasta llegar a ln(x)
*/
double ln(double x);