# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Maximizar L=0,20*10.8*x0+0,30*4,2*x1+0,40*2,03*x2

sujeito a
x0+x1+x2≤200000
0,2∙x0+0,30∙x1+0,40.x2≤60000
x0>=400
x1>=800
x2>=10000

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-0.20*10.8,-0.30*4.2,-0.40*2.03)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((1.0,1.0,1.0),
   (0.20,0.30,0.40))
# definindo o limite superior das restrições (lado direito das inequações)
b=(200000.0,60000.0)
# definindo a faixa de valores possíveis para cada variável
bnds=((400.0,None),(800.0,None),(10000.0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Lucro máximo da propriedade= {:.2f}".format(-res.fun))
print("Área plantada (m**2) do produto 1= {:.4f}".format(res.x[0]))
print("Área plantada (m**2) do produto 2= {:.4f}".format(res.x[1]))
print("Área plantada (m**2) do produto 3= {:.4f}".format(res.x[2]))
print("Otimização foi realizada com sucesso? ",res.success)


