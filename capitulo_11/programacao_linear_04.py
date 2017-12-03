# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Minimizar C=1,2*x0+1,00*x1+1,50*x2+0,40*x3

sujeito a
0,13∙x0+0,05∙x1+0,07∙x2+0,25∙x3≥0,05
0,13∙x0+0,05∙x1+0,07∙x2+0,25∙x3≤0,12
0,18∙x0+0,10∙x1+0,30∙x2+0,13∙x3≥0,15
0,18∙x0+0,10∙x1+0,30∙x2+0,13∙x3≤0,30
0,06∙x0+0,02∙x1+0,20∙x2+0,13∙x3≥0,00
0,06∙x0+0,02∙x1+0,20∙x2+0,13∙x3≤0,20

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(1.2,1.0,1.50,0.40)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((-0.13,-0.05,-0.07,-0.25),
   (0.13,0.05,0.07,0.25),
   (-0.18,-0.10,-0.30,-0.13),
   (0.18,0.10,0.30,0.13),
   (-0.06,-0.02,-0.20,-0.13),
   (0.06,0.02,0.20,0.13))
# definindo o limite superior das restrições (lado direito das inequações)
b=(-0.05,0.12,-0.15,0.30,0.00,0.20)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,None),(0,None),(0,None),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
x0=res.x[0]
x1=res.x[1]
x2=res.x[2]
x3=res.x[3]
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Custo mínimo da ração de cada animal= {:.4f}".format(res.fun))
print("Quantidade (kg) ingrediente 1 de cada animal= {:.4f}".format(x0))
print("Quantidade (kg) ingrediente 2 de cada animal= {:.4f}".format(x1))
print("Quantidade (kg) ingrediente 3 de cada animal= {:.4f}".format(x2))
print("Quantidade (kg) ingrediente 4 de cada animal= {:.4f}".format(x2))
print("\nAnálise por kg de ração produzida")
print("Custo mínimo por kg de ração = {:.4f}".format(res.fun/(x0+x1+x2+x3)))
print("Quantidade (kg) ingrediente 1 por kg de ração= {:.4f}".format(x0/(x0+x1+x2+x3)))
print("Quantidade (kg) ingrediente 2 por kg de ração= {:.4f}".format(x1/(x0+x1+x2+x3)))
print("Quantidade (kg) ingrediente 3 por kg de ração= {:.4f}".format(x2/(x0+x1+x2+x3)))
print("Quantidade (kg) ingrediente 4 por kg de ração= {:.4f}".format(x3/(x0+x1+x2+x3)))
print("Otimização foi realizada com sucesso? ",res.success)


