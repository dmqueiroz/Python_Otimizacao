# -*- coding: utf-8 -*-
"""
Programa para cálculo das raizes de uma equação de segundo grau

Created on Sat Dec  2 15:43:58 2017

@author: Daniel Marçal de Queiroz
"""
#programa raiz a equação ax**2+bx+c=0
import math
print("\nEsse programa determina as raízes de uma equação de segundo grau\n\n")
print("Dados de Entrada:")
a=float(input("Qual é o valor do parâmetro a?\n"))
b=float(input("\nQual é o valor do parâmetro b?\n"))
c=float(input("\nQual é o valor do parâmetro c?\n"))
print("\nResultados:")
delta=b*b-4*a*c
if delta<0:
     print("Essa equação não tem raiz real\n")
else:
     x1=(-b-math.sqrt(delta))/(2*a)
     x2=(-b+math.sqrt(delta))/(2*a)
     print("As raízes da equação são: ", x1," ",x2)

