# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 09:13:22 2025

@author: demeb
"""
import matplotlib.pyplot as plt
import numpy as np
import methodes as M
import probleme as pb
def main():
    T1, t1=M.RK4(pb.f,0,600,473,500)
    T2, t2=M.Eulerexplicite(pb.f,0,180,473,500)
    plt.plot(t1,T1,'r',lw=2)
    plt.plot(t2,T2,"m",lw=2)
    plt.legend(["Graphique pour rang kutta4","Graphiqure pour EuleurExplicite"])
    plt.xlabel("Temps")
    plt.ylabel("Température")
    plt.title("Evolution de la chaleur")
    plt.show()
main()