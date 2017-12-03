# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python problema corte de chapas



Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(12,12,12,12,12,12,12)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((-5,-3,-3,-2,-1,0,0),
   (0,-1,0,-2,0,-3,-2),
   (0,0,-1,0,-2,0,-1))
   
   
# definindo o limite superior das restrições (lado direito das inequações)
b=(-2500,-4500,-8000)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear problema corte de chapa")
print("\nRESULTADOS:")
print("Valor mínimo de perdas = {:.4f}".format(res.fun-57300))
print("Comprimento de corte do padrão 1: {:.4f}".format(res.x[0]))
print("Comprimento de corte do padrão 2: {:.4f}".format(res.x[1]))
print("Comprimento de corte do padrão 3: {:.4f}".format(res.x[2]))
print("Comprimento de corte do padrão 4: {:.4f}".format(res.x[3]))
print("Comprimento de corte do padrão 5: {:.4f}".format(res.x[4]))
print("Comprimento de corte do padrão 6: {:.4f}".format(res.x[5]))
print("Comprimento de corte do padrão 7: {:.4f}".format(res.x[6]))
print("Otimização foi realizada com sucesso? ",res.success)

