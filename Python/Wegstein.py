"""
    Wegstein Method of Non-Linear root finding

    Formula:
        x_n+1 = (x_0*f(x_n) - x_n*f(x_0)) / (x_0-f(x_0)-x_n+f(x_n))
"""
"""
    NOT COMPLETE
"""
from Nu_Meth import *

class Wegstein(Nu_Meth):
    def __init__(self, fptr = None, maxIter = 500, tol = 0.00001):
        self._fptr = fptr
        self._max_iter = maxIter
        self._tol = tol
    
    def execute(self, x0, x):
        if(self._fptr is None):
            raise Exception("fptr cannot be None")

        for i in range(self._max_iter):

            x_n = (x0 * self._fptr(x) - x * self._fptr(x0)) / (x0 - self._fptr(x0) - x + self._fptr(x))

            x0 = x
            x = x_n

            if abs(self._fptr(x)) < self._tol:
                return ( x0, i + 1)

        return "No Solution found after " + str(self._max_iter)


     
"""
    Test of Newton-Raphson
    f(x) = 12*x^2 + 13*x + 1
    f'(x) = 24x + 13
"""

def f(x):
    return (12*x*x + 13 * x + 1)


x0 = -12
x = 10
WObj = Wegstein(f)





import timeit
start_time = timeit.default_timer()
soln = WObj.execute(x0, x)
print(soln)
elapsed = timeit.default_timer() - start_time
print("Time: " + str(elapsed))













