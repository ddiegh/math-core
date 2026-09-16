#include "fundamentals/arithmetic.hpp"
#include <functional>

namespace{

    double newton_raphson(std::function<double(double)> f, std::function <double (double)> df, double xo, int iter, double tol){
        
        double x = xo;

        for (int i = 0; i<iter; i++){
            //asignaciones 
            double fn = f(x);
            double dfn = df(x);

            //en caso de que la derivada se haga cero
            if (absoluto(dfn) < tol){
                break;
            }
            //metodo de newton
            x = x - (fn / dfn);
        }
        return x; 
    }
}

double raiz(double x){
    //funcion lambda para sacarle raiz usando newton-raphson. Raiz de x seria la raix de esta funcion
    auto f = [x](double y){
        return x - (y*y);
    };

    //derivada
    auto df = [](double y){
        return -2*y;
    };

    //aplicamos newton y tenemos la raiz
    double xo = (x > 1.0) ? x / 2.0 : 1.0;
    double a = newton_raphson(f, df, xo, 10, 0.000001);

    return a;
}

double absoluto(double x){
    if (x < 0){
        x = -x;
    }
    return x;
}


double signo(double x){
    if (x>0) return 1.0;
    if (x<0) return -1.0;
    return 0.0;
}


double elevar(double x, int k){
    double xk = 1; 
    int j = k / 2;
    //solo calculamos un x**2
    double x2 = x*x;
    //multiplicamos x**2 j veces
    for ( int i = 0; i<j; i++){
        xk *= x2;
    }
    //si k es par entonces ya acabamos, sino nos falta multiplicar un x
    if (k % 2 == 0) return xk;
    return xk * x;
}

double ln(double x){
    if (x < 0) return 0.0;

    double y = x;
    int k = 0; //pasos

    // dividir el ln(x) en partes muy pequeñas hasta que este muy cercano al 1
    while (absoluto(y - 1.0) > 0.000001){
        y = raiz(y);
        k ++;
    }

    //muy cerca del 1, ln(y) = area(trapecio)
    double area_y = ((1.0 + (1.0/y))  * ( y-1.0 )) / 2.0;

    //regresamos a ln(x)
    return elevar(2.0, k) * area_y;
}