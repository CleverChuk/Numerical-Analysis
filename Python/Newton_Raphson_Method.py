"""
    Newton-Raphson implementation
    x_n+1 = x_n + f(x_n)/f'(x_n)
"""
import time
import matplotlib.pyplot as plt
from Nu_Meth import *
class Newton_Raphson(Nu_Meth):    
    def __init__(self, fptr, deriv_ptr, max_iter = 500, tol = 0.0001):
        self._fptr = fptr
        self._deriv_ptr = deriv_ptr
        
        self._max_iter = max_iter
        self._tol = tol


    """
       mutators
    """

    def execute(self, t_0):
        """
          method to perform the calculation          
        """
        soln = [t_0]
        
        for i in range(self._max_iter):
            t_n = t_0 - self._fptr(t_0)/self._deriv_ptr(t_0)
            t_0 = t_n

""" Not Complete! Still not what we want"""
            soln.append(t_0)
            plt.plot([i for i in range(i+2)],soln,"ro")
            plt.show(block = False)

            time.sleep(2)
            plt.close()
            
            if(abs(self._fptr(t_0)) < self._tol):
                break
        return (t_0, i+1)
            
            


"""
    Test of Newton-Raphson
    f(x) = 12*x^2 + 13*x + 1
    f'(x) = 24x + 13
"""

def f(x):
    return (x*x*x - x - 2)

def fprime(x):
    return 3*x*x - 1

x_0 = 100000000000
NObj = Newton_Raphson(f,fprime)





import timeit
start_time = timeit.default_timer()
soln = NObj.execute(x_0)
print(soln)
elapsed = timeit.default_timer() - start_time
print("Time: " + str(elapsed))












