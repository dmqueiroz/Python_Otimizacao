# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Maximizar L=3*x0+2*x1

sujeito a
1*x0+1*x1<=80
1*x0+2*x1<=100
0<=x0<=40
0<=x1<=infinito

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-3,-2)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((1,1),(1,2))
# definindo o limite superior das restrições (lado direito das inequações)
b=(80,100)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,40),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Valor máximo da função objetivo= {:.4f}".format(-res.fun))
print("Valor de x0 no ponto ótimo: {:.4f}".format(res.x[0]))
print("Valor de x1 no ponto ótimo: {:.4f}".format(res.x[1]))
print("Otimização foi realizada com sucesso? ",res.success)


