#include "fundamentals/sen.hpp"
#include <iostream>
#include <cmath>

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