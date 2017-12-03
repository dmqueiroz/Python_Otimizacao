# -*- coding: utf-8 -*-
"""
Programa para achar o valor mínimo da função f(x) = x**2 no intervalo -2 e +2

Created on Wed Sep 20 14:11:15 2017

@author: Daniel Marçal de Queiroz
"""
# importando a biblioteca numérica numpy
import numpy as np    
# importando a função infinito da biblioteca math           
from math import inf              
 # importando pyplot da biblioteca matplotlib
import matplotlib.pyplot as plt  
# importando minimize_sclar da biblioteca scipy.optimize
from scipy.optimize import minimize_scalar  
# 
# definindo função objetivo
def F(x):
    if(x!=0.0):
        F=2*x+3/x
    else:
        # se x=0, define o resultado como infinito
        F=inf
    return F
#
print("\n\nPrograma para obter o mínimo da função f(x)= 2*x+3/x,")
print("            no intervalo 0.1 a 4\n")
# 
#definindo limites
bnds=(0.1,4.0)
#
# chamando a função minimize_scalar para cálculo do valor mínimo, não
# será definido o método
resultado=minimize_scalar(F,bounds=bnds)
#
print("\n\nResultados:")
print("O valor torna a função mínima: {0:.4f}".format(resultado.x))
print("O valor mínimo da função: {0:.4f}".format(resultado.fun))
print("A solução foi obtida com sucesso: ",resultado.success)
# gerando gráfico da função
# gerando 101 pontos igualmente espaçado entre a e b
x=np.linspace(0.1,4.0,101)
y=np.zeros(len(x))
# calculando o valor da função em cada um dos 101 pontos
for i in range(101):
    y[i]=F(x[i])
# plotando os pontos usando linha de cor vermelha
plt.plot(x,y, 'r')
# plotando o ponto de mínimo usando bola azul
plt.plot(resultado.x,resultado.fun,'bo')
# definindo títulos do gráfico e dos eixos
plt.title("Procurando o mínimo de uma função")
plt.ylabel("Valor de F(x)")
plt.xlabel("Valor de x")
# mostrando uma malha na área de plotagem
plt.grid(True)
plt.show()


