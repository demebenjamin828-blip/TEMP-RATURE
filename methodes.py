# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 10:58:29 2025

@author: demeb
"""

import numpy as np 
def RK4(prb,t0,tmax ,T0,N):
    h=(tmax-t0)/N
    t=np.zeros(N+1)
    T=np.zeros(N+1)
    t[0]=t0
    T[0]=T0
    for i in range(N):
        k1=h*prb(t[i], T[i])
        k2=h*prb(t[i]+h/2, T[i]+k1/2)
        k3=h*prb(t[i]+h/2 ,T[i]+k2/2)
        k4=h*prb(t[i]+h, T[i]+k3)
        T[i+1]=T[i]+(1/6)*(k1+2*k2+2*k3+k4)
        t[i+1]=t[i]+h
    return T,t
def Eulerexplicite(prb,t0,tmax,T0,N):
        h=(tmax-t0)/N
        t=np.zeros(N+1)
        T=np.zeros(N+1)
        t[0]=t0
        T[0]=T0
        for i in range(N):
            T[i+1]=T[i]+h*prb(t[i],T[i])
            t[i+1]=t[i]+h
        return T,t
    