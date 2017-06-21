"""
    Bisection-Method

    Formula:
        Given two guesses: [a,b]
        find the mid-point
            c = (b+a)/2
        evaluation f(a), f(b) and f(c)
        if:
           f(a) is +ve and f(b) is -ve and f(c) is +ve
           then replace  a = c          
"""
from Nu_Meth import *
class Bisection_Method(Nu_Meth):
    def __init__(self,fptr, max_iter = 500, tol = 0.0001):       
        self._fptr = fptr
        self._max_iter = max_iter
        
        self._tol = tol

    def execute(self, a,b):
        """
            Takes two numbers
        """            

        for i in range(self._max_iter):
            c = (a + b)/2
            f_a = self._fptr(a)
            
            f_b = self._fptr(b)
            f_c = self._fptr(c)

            if f_a * f_c <= 0:
                b = c
                if abs(f_a) < self._tol :
                    return (a, i+1)
            if f_b * f_c <= 0:
                a = c
                if abs(f_b) < self._tol :
                    return (b, i+1)
        return "No solution was found after " + str(self._max_iter) +" iterations"


"""
    Test of Newton-Raphson
    f(x) = 12*x^2 + 13*x + 1
"""

def f(x):
    return (12*x*x + 13*x + 1)

BObj = Bisection_Method(f, 10000)

import timeit
start_time = timeit.default_timer()

a = -.5
b = 0

soln = BObj.execute(a,b)
print(soln)
elapsed = timeit.default_timer() - start_time
print("Time: " + str(elapsed))






















            
            
        
