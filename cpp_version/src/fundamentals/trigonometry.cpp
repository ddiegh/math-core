#include "fundamentals/trigonometry.hpp"
#include "fundamentals/arithmetic.hpp"

double sen(double x){

    double xo = x / 1024.0;

    double y = xo*xo;

    for (int i = 0; i<10; i++){
        y = 4*y*(1-y);
    }
    return signo(x)*raiz(y);
}


