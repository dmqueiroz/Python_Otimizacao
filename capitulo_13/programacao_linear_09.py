# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python problema refinaria de 
petróleo



Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-16,-11,-15,-8,-9,-4,-8,-1,-3,2,-2,-5)
# definindo coeficientes que compõem o lado esquerdo das restrições
A=((1,0,0,0,1,0,0,0,1,0,0,0),
   (0,1,0,0,0,1,0,0,0,1,0,0),
   (0,0,1,0,0,0,1,0,0,0,1,0),
   (0,0,0,1,0,0,0,1,0,0,0,1),
   (0.7,-0.3,-0.3,-0.3,0,0,0,0,0,0,0,0),
   (0.4,-0.6,0.4,0.4,0,0,0,0,0,0,0,0),
   (-0.5,-0.5,0.5,-0.5,0,0,0,0,0,0,0,0),
   (0,0,0,0,0.7,-0.3,-0.3,-0.3,0,0,0,0),
   (0,0,0,0,0.1,-0.9,0.1,0.1,0,0,0,0),
   (0,0,0,0,0,0,0,0,0.3,-0.7,-0.7,-0.7))
   
   
# definindo o limite superior das restrições (lado direito das inequações)
b=(3500,2200,4200,1800,0,0,0,0,0,0)
# definindo a faixa de valores possíveis para cada variável
bnds=((0,None),(0,None),(0,None),(0,None),(0,None),(0,None),
      (0,None),(0,None),(0,None),(0,None),(0,None),(0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,bounds=bnds)
print("\n\nProblema de Programação Linear da Refinaria")
print("\nRESULTADOS:")
print("Valor máximo da função objetivo (Lucro)= {:.4f}".format(-res.fun))
print("Quantidade petróleo P1 na gasolina superazul no ponto ótimo: {:.4f}".format(res.x[0]))
print("Quantidade petróleo P2 na gasolina superazul no ponto ótimo: {:.4f}".format(res.x[1]))
print("Quantidade petróleo P3 na gasolina superazul no ponto ótimo: {:.4f}".format(res.x[2]))
print("Quantidade petróleo P4 na gasolina superazul no ponto ótimo: {:.4f}".format(res.x[3]))
print("Quantidade petróleo P1 na gasolina azul no ponto ótimo: {:.4f}".format(res.x[4]))
print("Quantidade petróleo P2 na gasolina azul no ponto ótimo: {:.4f}".format(res.x[5]))
print("Quantidade petróleo P3 na gasolina azul no ponto ótimo: {:.4f}".format(res.x[6]))
print("Quantidade petróleo P4 na gasolina azul no ponto ótimo: {:.4f}".format(res.x[7]))
print("Quantidade petróleo P1 na gasolina amarela no ponto ótimo: {:.4f}".format(res.x[8]))
print("Quantidade petróleo P2 na gasolina amarela no ponto ótimo: {:.4f}".format(res.x[9]))
print("Quantidade petróleo P3 na gasolina amarela no ponto ótimo: {:.4f}".format(res.x[10]))
print("Quantidade petróleo P4 na gasolina amarela no ponto ótimo: {:.4f}".format(res.x[11]))
print("Otimização foi realizada com sucesso? ",res.success)


