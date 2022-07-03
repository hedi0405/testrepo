# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:16:50 2022

@author: Hedi
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return np.sqrt(x)
def rk4(f,ti,tf,x0,N):
     h=(tf-ti)/N
     t,x=np.linspace(ti,tf,N+1),[]
     x.append(x0)
     for n in range(N):
         K1=f(t[n],x[n])
         k2=f(t[n]+0.5*h,x[n]+0.5*h*K1)
         k3=f(t[n]+0.5*h,x[n]+0.5*h*k2)
         k4=f(t[n]+h,x[n]+h*k3)
         x.append(x[n]+h*(K1+2*(k2+k3)+k4/6))
         return t,x
x0 = np.array([abs(np.sqrt(2.)**2.)])
t,x=rk4(f,0.,14.,x0,10**5)
xref,err,h=x[-1],[],[]
for i in range(4):
    N=10**(i+1)
    h.append(14/N)
    t,x=rk4(f,0.,14.,x0,N)
    err.append(np.linalg.norm(xref-x[-1]))
slope=np.polyfit(np.log(h),np.log(err),1)
plt.loglog(h,err,'+',h,np.exp(slope[1])*(h**(slope[0])))
print("lordre de convergence effectif vaut",slope[0])