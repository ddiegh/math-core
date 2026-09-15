#include <iostream>
#include <cmath>
/**
 * @brief Calcula la aproximación del seno.
 * 
 * Este método utiliza la aproximación de ángulos pequeños y la aplica de forma 
 * iterativa 10 veces.
 * @param x El ángulo en radianes.
 * @return Un valor de tipo double que representa la magnitud del seno del ángulo (positivo).
 * 
 * @note Actualmente la función solo devuelve el valor absoluto.
 * 
 * Ejemplo de uso:
 * double resultado = sen(2.0); // Devolverá aprox 0.909297
 */
double sen(double x){
    // Funcion que calcula el seno de un numero real.
    double xo = x / 1024.0;

    double y = xo*xo;

    for (int i = 0; i<10; i++){
        y = 4*y*(1-y);
    }
    return std::sqrt(y);
}

int main(){
    double x = 2;
    std::cout << "El seno de " << x << " es: " << sen(x) << std::endl;
    return 0;
}