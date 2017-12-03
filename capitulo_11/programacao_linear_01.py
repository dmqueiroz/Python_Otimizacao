# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Minimizar Z=10*x0+5*x1

sujeito a
-20*x0-50*x1<=-200
-50*x0-10*x1<=-150
-30*x0-30*x1<=-210
x0,x1>=0

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(10,5)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((-20,-50),(-50,-10),(-30,-30))
# definindo o limite superior das restrições (lado direito das inequações)
b=(-200,-150,-210)
# como as variáveis podem ter qualquer valor positivo, então não é necessário
# estabelecer faixa de variação das variáveis
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Valor mínimo da função objetivo= {:.4f}".format(res.fun))
print("Valor de x0 no ponto ótimo: {:.4f}".format(res.x[0]))
print("Valor de x1 no ponto ótimo: {:.4f}".format(res.x[1]))
print("Otimização foi realizada com sucesso? ",res.success)


