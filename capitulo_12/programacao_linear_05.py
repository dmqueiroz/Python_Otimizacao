# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Minimizar C=2*x0+4*x1+1,50*x2+0,01*x3

sujeito a
2∙x0+2∙x1+100∙x2+0,2∙x3≤11
50∙x0+20∙x1+10∙x2+0,3∙x3≤70
80∙x0+70∙x1+10∙x2+0,8∙x3≤250

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(2.0,4.0,1.50,0.01)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((-1.0,-2.0,-100.0,-0.20),
   (-50.0,-20.0,-10.0,-0.30),
   (-80.0,-70.0,-10.0,-0.80))
# definindo o limite superior das restrições (lado direito das inequações)
b=(-11.0,-70.0,-250.0)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,None),(0,None),(0,None),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Custo mínimo da ração= {:.4f}".format(res.fun))
print("Quantidade (L) de leite= {:.4f}".format(res.x[0]))
print("Quantidade (kg) de carne= {:.4f}".format(res.x[1]))
print("Quantidade (kg) de peixe= {:.4f}".format(res.x[2]))
print("Quantidade (g) de salada= {:.4f}".format(res.x[3]))
print("Otimização foi realizada com sucesso? ",res.success)
