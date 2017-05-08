/* EulerDriver.cpp
*
*  Created on : May 4, 2017
* Author : CleverChuk
*
	Description:
		This program test drives the implemetation of Euler's Method
*/

#include <cstdio>
#include "Euler.h"
double func(double, double);

int main() {
	double t0 = 0;
	double y0 = 1;
	double h = 0.001;
	double t = 5.0;
	Euler solver;
	vector<double> values = solver.solver(func, t0, y0, h, t,10000,1e-4);

	for (double i : values) {
		if (!i)
		{
			break;
		}
		printf("%f\n", i);
	}
	getchar();
	return 0;
}

/*
	function that describes the first ODE to be solved
*/
double func(double t0, double y0) {
	return (2 - pow(2.71828183, -4 * t0) - 2 * y0);
}