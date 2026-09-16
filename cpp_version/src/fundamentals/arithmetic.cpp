#include "fundamentals/arithmetic.hpp"
#include <iostream>
#include <functional>

double newton_raphson(std::function<double(double)> f, std::function <double (double)> df, double xo, int iter, double tol){
    double x = xo;
    for (int i = 0; i<iter; i++){
        double fn = f(x);
        double dfn = df(x);

        x = x - (fn / dfn);
    }
    return x; 
}

double raiz(double x){
    auto f = [&x](double y){
        return x - (y*y);
    };

    auto df = [](double y){
        return -2*y;
    };

    double a = newton_raphson(f, df, x/2, 10, 1);

    return a;
}

