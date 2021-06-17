import numpy as np


def RK4_3variable(a0,b0,w0,func_a,h,N):
    """
    Solivng IVP with 
    
    * a0,b0,w0 : initial value
    * y' = func_a(t,a0,b0,w0)
    
    h is time step, and N is the number of steps
    
    Here, func_a is independent with time t
    
    func_a example,
    
    malkus(a, b, w, q1, K=0.5, I =1, v=0.25, r=0.25):
    
    
    """
    w_list = np.zeros((3,N+1))
    t_list = np.zeros(N+1)
    
    w_list[0,0] = a0
    w_list[1,0] = b0
    w_list[2,0] = w0
    
    t_list[0] = 0
    
    for i in range(N):
        
        t_i = t_list[i]
        
        t_list[i+1] = t_i+h
        

        k1,l1,m1 = h*func_a(w_list[0,i],w_list[1,i],w_list[2,i])
        
        k2,l2,m2 = h*func_a(w_list[0,i] + (1/2)*k1, w_list[1,i] + (1/2)*l1, w_list[2,i] + (1/2)*m1 )
        
        k3,l3,m3 = h*func_a( w_list[0,i] + (1/2)*k2, w_list[1,i] + (1/2)*l2 ,w_list[2,i] + (1/2)*m2)
        
        
        k4,l4,m4 = h*func_a( w_list[0,i]+k3,w_list[1,i]+l3, w_list[2,i]+m3)

        
        w_list[0,i+1] = w_list[0,i] + (1/6)*(k1+ 2*k2 + 2*k3 + k4)
        w_list[1,i+1] = w_list[1,i] + (1/6)*(l1+ 2*l2 + 2*l3 + l4) 
        w_list[2,i+1] = w_list[2,i] + (1/6)*(m1+ 2*m2 + 2*m3 + m4) 
        
    return w_list,t_list



def Euler(a0, b0,w0, func_a,h,N):
    """Solve y’= f(y,t), y(0)=y0, with n steps until t=T."""
    w_list = np.zeros((3,N+1))
    t_list = np.zeros(N+1)
    w_list[0,0] = a0
    w_list[1,0] = b0
    w_list[2,0]= w0
    t_list[0] = 0

    
    for k in range(N):
        t_list[k+1] = t_list[k] + h
        w_list[0,k+1],w_list[1,k+1],w_list[2,k+1] = w_list[:,k] + h*func_a(w_list[0,k],w_list[1,k],w_list[2,k])
    return w_list,t_list