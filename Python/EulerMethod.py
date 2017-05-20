"""
 Euler's Method:
    Solving Ordinary Differential Eqautions numerically

 Theory:
    Euler's method is a technique used in estimating the value of the gradient of
    a field. Like most numerical approximations, the Euler's method has some element
    of Taylor series approximation in it.
    
    Given and ODE of the form
        dy/dt + 2*y = 2 - e^(-4*t)
        initial conditions:
           y(0) = 0; t = 0
    Find y(5)?

    Using Euler's method:
       Redefine the equation so that the derivative is the subject of the formula
       and it has to be firt order derivative.
       In the case you are dealing with higher order derivative, you define new variables.
       Doing this ensures that you are only approximating systems of coupled first ODE

       Redefine:
          dy/dt = -2*y + 2 - e^(-4*t)

       Once redefined, you are ready to use the Euler's method solve the problem

       Algorithm:
          Requirements:
                Initial conditions
                Step size
          Euler formula:
             y_n+1 = y_n + h * f(y_n,t_n)    
"""
import math as m
import time
import matplotlib.pyplot as plt
class Euler:
    """
      Implementation of the Euler method for 1st order ODE
    """
    _fptr = None # funtion pointer to the function that performs the calculation
    _step_size = 0.1 # step size
    _max_iter = 500  # maximum iteriation before the solver quits
    _tol = 0.0001 # tolerance

    """
       Object contructor:
         fptr: function to evaluate derivative
         step_size: time increments
         max_iter: maximum iterations to perform
         tol: Error tolerance between the actual 
    """
    def __init__(self, fptr = None, step_size = 0.1, max_iter = 500, tol = 0.0001):
        self._fptr = fptr
        self._step_size = step_size
        self._max_iter = max_iter
        self._tol = tol


    """
       mutators
    """
  
    def set_fptr(self,fptr):
        self._fptr = fptr

    def set_step_size(self,h):
        self._step_size = h

    def set_tol(self,tol):
        self._tol = tol

    def set_maxIter(self,mI):
        self._max_iter = mI;

    def execute(self, y_0, t_0, t):
        """
          method to perform the calculation
          supports only first order ODE
        """
        soln = [y_0]
        lIter = 0
        fig = None
        if(self._fptr is None):
            raise Exception("Must specify function pointer. fptr cannot be None")
        for i in range(self._max_iter):
            """" Eulers formula """
            y_n = y_0 + self._step_size * self._fptr(y_0,t_0)

            if(abs(t_0 - t) <= self._tol):
                break;
            
            soln.append(y_n)
            y_0 = y_n
            t_0 += self._step_size
            lIter = i+1

"""         Not final! Still not what we want!"""
            plt.plot([i for i in range(i+2)],soln,"ro")
            plt.show(block = False)
            time.sleep(2)
            plt.close();

            
        return soln[-1],lIter
            
            

"""
testing
"""

def equation(y,t):
    return -2*y + 2 - m.exp(-4*t)

y_0 = 1
t_0 = 0
t = 5
h = 0.001
mIter = 50000
tol = 0.1

solver = Euler(equation)
solver.set_tol(tol)
soln = solver.execute(y_0, t_0, t)

##for i in soln:
##    print(i)
        
     
        





    




























    
