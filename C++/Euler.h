#pragma once
/*
* Euler.h
*
*  Created on: May 4, 2017
*      Author: CleverChuk
*/

#ifndef EULER_H_
#define EULER_H_
#include <vector>
using namespace std;

class Euler {
public:
	vector<double> solver(double(*)(double, double), double, double ,
		double , double, int , double);
	// ctor
	Euler();

	// dtor
	~Euler();
};
#endif /* EULER_H_ */

