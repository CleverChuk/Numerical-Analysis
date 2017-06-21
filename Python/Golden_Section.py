"""
    Golden Section search Implementation
    "NOT COMPLETE"
"""
import math as mt
from Nu_Meth import Nu_Meth

class GoldenSection(Nu_Meth):
    gR = 1.618
    def __init__(self, fptr, maxIter = 500, tol = 0.0001):
        self._fptr = fptr
        self._max_iter = maxIter
        self._tol = tol

    def execute(self, a, b, minimax = 0):
        f_a = self._fptr(a)
        f_b = self._fptr(b)

        c = a + (b - a)/self.gR
        d = b - (b - a)/self.gR

        for i in range(self._max_iter):
            if( not minimax):
                if self._fptr(d) < self._fptr(c):
                    b = d
                else:
                    a = c
                if abs(c - d) <= self._tol:
                    return c
                    
            else:
                if self._fptr(d) > self._fptr(c):
                    a = c
                else:
                    b = d
                if( abs(c - d) <= self._tol):
                    return d
            
            
            c = a + (b - a)/self.gR
            d = b - (b - a)/self.gR

##            print(self._fptr(c), self._fptr(d))

        return "No solution was found after " + str(self._max_iter)

          

"""
    Test of Newton-Raphson
    f(x) = 12*x^2 + 13*x + 1
    f'(x) = 24x + 13

    f1(x) = x^3 - x - 2
    f1'(x) = 3x^2 - 1
"""

def f(x):
    return (12*x*x + 13*x + 1)

def fprime(x):
    return 3*x*x - 1

x_0 = -1
x = 1
GSObj = GoldenSection(f)





import timeit
start_time = timeit.default_timer()
soln = GSObj.execute(x_0,x)
print(soln)
elapsed = timeit.default_timer() - start_time
print("Time: " + str(elapsed))



import math

gr = 1.618

def gss(f, a, b, tol=1e-5):
    '''
    golden section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1, 5)
    >>> x
    2.000009644875678

    '''
    c = b - (b - a) / gr
    d = a + (b - a) / gr 
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # we recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        c = b - (b - a) / gr
        d = a + (b - a) / gr

    return (b + a) / 2





print(gss(f,x_0,x))












        
