"""
    Newton-Raphson implementation
    x_n+1 = x_n + f(x_n)/f'(x_n)
"""
from Nu_Meth import *
class Newton_Raphson(Nu_Meth):
    _deriv_ptr = None # pointer to derivative function
    
    def __init__(self, fptr = None,deriv_ptr = None, max_iter = 500, tol = 0.0001):
        self._fptr = fptr
        self._deriv_ptr = deriv_ptr
        
        self._max_iter = max_iter
        self._tol = tol


    """
       mutators
    """

    def set_derivFptr(dptr):
        self._deriv_ptr = dptr

    def execute(self, t_0):
        """
          method to perform the calculation          
        """
        if(self._fptr is None):
            raise Exception("fptr is not specified")
        if(self._deriv_ptr is None):
            raise Exception("deriv_ptr is not specified")

        for i in range(self._max_iter):
            t_n = t_0 - self._fptr(t_0)/self._deriv_ptr(t_0)
            t_0 = t_n

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












