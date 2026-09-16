#pragma once 

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
double sen(double x);


