import numpy as np


class Malkus:
    
    def __init__(self, q1,K=0.2,I =0.2 ,v=0.1,r=0.02):
            self.q1 = q1
            self.K = K
            self.I = I
            self.v = v
            self.r = r
            
    def malkus(self,a,b,w):
        
        adot = -K*a + w*b
        
        bdot = self.q1-K*b - w*a
    
        wdot = (-v*w+9.8*r*a*np.pi)/I
        
        return np.array([adot,bdot,wdot])
    


    