#include <iostream>
#include "fundamentals/arithmetic.hpp"
#include "fundamentals/trigonometry.hpp"



void prueba_raiz_seno() {
    std::cout << "=== PRUEBAS MATH-CORE ===\n";
    
    // 1. Pruebas de Aritmética (Newton-Raphson optimizado)
    double num1 = 25.0;
    double num2 = 0.25; // Para probar tu semilla condicional xo = 1.0
    
    std::cout << "La raiz de " << num1 << " es: " << raiz(num1) << "\n";
    std::cout << "La raiz de " << num2 << " es: " << raiz(num2) << "\n";
    std::cout << "-------------------------\n";

    // 2. Pruebas de Trigonometría (Algoritmo logístico y signo)
    double angulo = 1.570796; // Aproximación a pi/2 (debería dar cerca de 1)
    
    std::cout << "El seno de 1.570796 rad es: " << sen(angulo) << "\n";
    std::cout << "El seno de -1.570796 rad es: " << sen(-angulo) << "\n";
}

void prueba_ln() {
    std::cout << "=== PRUEBAS DE LOGARITMO NATURAL ===\n";

    // 1. El caso base (debe dar 0)
    std::cout << "ln(1.0) = " << ln(1.0) << "\n";

    // 2. El numero de Euler aproximado (debe dar muy cercano a 1)
    std::cout << "ln(2.718281) = " << ln(2.718281) << "\n";

    // 3. Un numero entre 0 y 1 (debe dar negativo, aprox -0.693)
    std::cout << "ln(0.5) = " << ln(0.5) << "\n";

    // 4. Un numero mayor para probar la elasticidad del bucle (aprox 2.302)
    std::cout << "ln(10.0) = " << ln(10.0) << "\n";

    // 5. El caso de seguridad (debe dar 0 segun tu proteccion)
    std::cout << "ln(-5.0) = " << ln(-5.0) << "\n";
    
    std::cout << "------------------------------------\n";
}

int main(){
    prueba_ln();
    return 0;
}