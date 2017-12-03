# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Maximizar R=3000*x0+5000*x1

sujeito a
0,50∙x0+0,20∙x1≤16
0,25∙x0+0,30∙x1≤11
0,50∙x0+0,50∙x1≤15

Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-3000.0,-5000.0)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((0.50,0.20),
   (0.25,0.30),
   (0.50,0.50))
# definindo o limite superior das restrições (lado direito das inequações)
b=(16.0,11.0,15.0)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,None),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Receita máxima da metalúrgica= {:.2f}".format(-res.fun))
print("Quantidade (t) da liga de baixa resistência= {:.4f}".format(res.x[0]))
print("Quantidade (t) da liga de alta resistência= {:.4f}".format(res.x[1]))
print("Otimização foi realizada com sucesso? ",res.success)

