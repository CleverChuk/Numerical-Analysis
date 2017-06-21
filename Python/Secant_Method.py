"""
    Secant-Method

    Formula:
        x_n = x_n-1 - f(x_n-1)*(x_n-1 - x_n-2) /(f(x_n-1) - f(x_n-2))
"""
from Nu_Meth import *
class Secant_Method(Nu_Meth):

    def __init__(self, fptr, max_iter = 500, tol = 0.0001):
        self._fptr = fptr     
        self._max_iter = max_iter
        self._tol = tol


    """
       mutators
    """
    def set_step_size(h):
        self._step_size = h

    def set_tol(tol):
        self._tol = tol

    def set_maxIter(mI):
        self._max_iter = mI;

    def execute(self, x_0, x):
        """
            Does iteration to find a solution / root
        """

        if(self._fptr is None):
            raise Exception("ftpr cannot be None")

        for i in range(self._max_iter):
            x_n = x - self._fptr(x)*(x - x_0)/(self._fptr(x) - self._fptr(x_0))
            x_0 = x
            x = x_n

            if(abs(x_0 - x) < self._tol):
                break;

        return (x, i+1)



    
"""
    Test of Secant-Method
    f(x) = 12*x^2 + 13*x + 1
"""
def f(x):
    return (x*x*x - x - 2)

Sobj = Secant_Method(f)


x_0 = 1000000000
x = 100000000000

import timeit
start_time = timeit.default_timer()
soln = Sobj.execute(x_0,x)
print(soln)
elapsed = timeit.default_timer() - start_time
print("Time: " + str(elapsed))





















        
    
