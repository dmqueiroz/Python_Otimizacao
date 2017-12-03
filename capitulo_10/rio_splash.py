# -*- coding: utf-8 -*-
"""
Programa para otimização do uso de água do Rio Splash

Created on Wed Oct 18 17:33:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
from math import fabs
import numpy as np
L=lambda q:-(2.9*q[0]+1.14*q[1]+1.6*q[2]+1.0*q[3])
M=lambda q:1.8E6-1.1*(q[0]+q[1])-1.4*(q[2]+q[3])
T1=lambda q:q[0]+q[1]-0.3E6
T2=lambda q:q[2]+q[3]-0.2E6
VD=lambda q:0.7*2.0E6-q[0]-q[1]-q[2]-q[3]
PL=lambda q:0.4*(q[0]+q[1]+q[2]+q[3])-fabs(q[0]+q[1]-q[2]-q[3])
bnds=((0,np.inf),(0,np.inf),(0,np.inf),(0,np.inf))
con1={"fun": M, "type": "ineq"}
con2={"fun": T1, "type": "ineq"}
con3={"fun": T2, "type": "ineq"}
con4={"fun": VD, "type": "ineq"}
con5={"fun": PL, "type": "ineq"}
q0=[0.5E6,0.5E6,0.5E6,0.5E6]
res=opt.minimize(L,q0,bounds=bnds,constraints=(con1,con2,con3,con4,con5))
print("\n\nPrograma para otimização da quantidade de água desviada do rio Splash")
print("\nResultados obtidos:")
print("Lucratividade ótima do sistema ($/ano): {:.2f}".format(-res.fun))
print("Quantidade de água a ser desviada para o canal 1 (m**3/dia): {:.2f}"
      .format(res.x[0]+res.x[1]))
print("Quantidade de água a ser desviada para o canal 2 (m**3/dia): {:.2f}"
      .format(res.x[2]+res.x[3]))
print("Quantidade de água a ser desviada para o canal 1 (m**3/dia): {:.2f}"
      .format(res.x[0]+res.x[1]))
print("Quantidade de água do canal 1 usada para eletricidade (m**3/dia): {:.2f}"
      .format(res.x[0]))
print("Quantidade de água do canal 1 usada para irrigação (m**3/dia): {:.2f}"
      .format(res.x[1]))
print("Quantidade de água do canal 2 usada para eletricidade (m**3/dia): {:.2f}"
      .format(res.x[2]))
print("Quantidade de água do canal 2 usada para irrigação (m**3/dia): {:.2f}"
      .format(res.x[3]))


