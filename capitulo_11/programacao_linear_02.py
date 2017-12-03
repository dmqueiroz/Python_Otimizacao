# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Maximizar Z=20*x0+30*x1

sujeito a
x0+2*x1<=120
0<=x0<=60
0<=x1<=50

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-20,-30)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=(1,2)
# definindo o limite superior das restrições (lado direito das inequações)
b=(120,)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,60),(0,50))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Valor máximo da função objetivo= {:.4f}".format(-res.fun))
print("Valor de x0 no ponto ótimo: {:.4f}".format(res.x[0]))
print("Valor de x1 no ponto ótimo: {:.4f}".format(res.x[1]))
print("Otimização foi realizada com sucesso? ",res.success)


