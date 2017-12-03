# -*- coding: utf-8 -*-
"""
Programa para calcular derivadas de primeira ordem por diferenças finitas

Created on Wed Sep 27 14:01:49 2017

@author: Daniel Marçal de Queiroz
"""
from math import sin,sqrt,cos
#
# Função que calcula o valor da função que queremos derivar
F=lambda x:sin(0.5*sqrt(x))/x
#
# Função que calcula o valor da derivada pela solução analítica
FLanalitica=lambda x:0.25*cos(0.5*sqrt(x))/x**1.5-sin(0.5*sqrt(x))/(x*x)
#
# Função derivada por diferenças finitas com base em duas avaliações de f(x)
FL2avaliacoes=lambda x,h=0.01:(F(x+h)-F(x-h))/(2*h)
#
# Função derivada por diferenças finitas com base em quatro avaliações de f(x)
FL4avaliacoes=lambda x,h=0.01:(-F(x+2*h)+8*F(x+h)-8*F(x-h)+F(x-2*h))/(12*h)
#
# definindo o valor de x
x=1.0
#
# definindo o valor de h
h=0.2
#
# calculando o valor da derivada pelos três métodos
Fana=FLanalitica(x)
F2ava=FL2avaliacoes(x,h)
F4ava=FL4avaliacoes(x,h)
#
# apresentando o resultado os três métodos numéricos
print("\nCalculando a derivada de primeira ordem numericamente e comparando")
print("                     com a solução analítica\n\n")
print("Derivada pela solução analítica= {:.5f}".format(Fana))
print("Derivada obtida por 2 avaliações= {:.5f}, erro={:.5f}".format(F2ava,Fana-F2ava))
print("Derivada obtida por 4 avaliações= {:.5f}, erro={:.5f}".format(F4ava,Fana-F4ava))


