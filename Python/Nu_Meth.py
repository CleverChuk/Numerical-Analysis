"""
    BaseClass module for Numerical Methods
    for Non-Linear root finding
"""

class Nu_Meth:
    _max_iter = 500  # maximum iteriation before the solver quits
    _tol = 0.0001 # tolerance

    def __init__():
        pass
    
    def execute(self):
        raise NotImplemented

    def set_tol(self,tol):
        self._tol = tol

    def set_maxIter(mIter):
        self._max_iter = mIter
