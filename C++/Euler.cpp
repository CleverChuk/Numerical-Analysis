/* Euler.cpp
*
*  Created on : May 4, 2017
* Author : CleverChuk
*/
#include "Euler.h"
using namespace std;
/*  solver that performs the Euler discretization and approximation of first
	order ODE
*/
vector<double> Euler::solver(double(*fptr)(double t0, double f0), double t0, 
	                 double f0, double h, double t, int maxIter, double tol) {

	vector<double> yvalues(maxIter);
	yvalues[0] = f0 ;
	for (int i = 1; i < maxIter; i++)
	{
		if (abs(t0-t) < tol)
			break;
		
		yvalues[i] = yvalues[i - 1] + h * fptr(t0, yvalues[i - 1]);
		t0 += h;
	}
	
	return yvalues;
}

Euler::Euler()
{
}

Euler::~Euler()
{
}
