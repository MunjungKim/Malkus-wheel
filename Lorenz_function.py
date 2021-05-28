import numpy as np


class Lorenz:
    
    def __init__(self, s=10, r=28, b=2.667):
            self.s = s
            self.b = b
            self.r = r
            
    def Lorenz_func(self,x, y, z):
        xdot = self.s*(y - x)
        ydot = self.r*x - y - x*z
        zdot = x*y - self.b*z
        return np.array([xdot,ydot,zdot])

