#pragma once 
#include <iostream>
#include <functional>

double newton_raphson(std::function<double(double)> f, std::function <double (double)> df, double xo, int iter, double tol);
double raiz(double x);