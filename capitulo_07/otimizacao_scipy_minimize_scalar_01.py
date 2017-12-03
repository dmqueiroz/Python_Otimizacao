# -*- coding: utf-8 -*-
"""
Programa para achar o valor mínimo da função f(x) = x**2 no intervalo -2 e +2

Created on Wed Sep 20 14:11:15 2017

@author: Daniel Marçal de Queiroz
"""
from scipy.optimize import minimize_scalar
# 
# definindo função objetivo
F=lambda x:x*x
#
print("\n\nPrograma para obter o mínimo da função f(x)= x**2,")
print("            no intervalo -2 a +2\n")
#
# definindo o limite de busca
bnds=(-2,2)
#
# chamando a função minimize_scalar para cálculo do valor mínimo, não
# será definido o método
resultado=minimize_scalar(F,bounds=bnds)
#
print("\n\nResultados:")
print("O valor torna a função mínima: {0:.4f}".format(resultado.x))
print("O valor mínimo da função: {0:.4f}".format(resultado.fun))
print("A solução foi obtida com sucesso: ",resultado.success)


