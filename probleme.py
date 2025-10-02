# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 13:52:27 2025

@author: demeb
"""

import numpy as np 
def f(t,T):
    A=0.25
    N=500
    p=300
    V=0.001
    C=900
    hc=30
    ε=0.8
    σ=0.0000000567
    T_ab=294
    m=(p*V)
    b=A/(m*C)
    z=b*(ε*σ*(294**4 - T**4) + hc*(297 - T));
    return z;
    