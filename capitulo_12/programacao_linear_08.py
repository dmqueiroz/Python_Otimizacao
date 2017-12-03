# -*- coding: utf-8 -*-
"""
Resolvendo problema de programação linear em python

Maximizar L=5000*x0+7000*x1+8000*x2+5000*x3+7000*x4+8000*x5+5000*x6+7000*x7+8000*x8

sujeito a
x0+x1+x2≤160
x3+x4+x5≤260
x6+x7+x8≤140
13,75*x0+10,00*x1+8,75*x2≤1800
13,75*x3+10,00*x4+8,75*x5≤2200
13,75*x6+10,00*x7+8,75*x8≤950
x0+x3+x6≤264
x1+x4+x7≤352
x2+x5+x8≤160
260*x0+260*x1+260*x2-160*x3-160*x4-160*x5=0
-140*x3-140*x4-140*x5+260*x6+260*x7+260*x8=0


Created on Mon Nov  6 11:23:45 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt
# definindo coeficientes da função objetivo
c=(-5000.00,-7000.00,-8000.00,
   -5000.00,-7000.00,-8000.00,
   -5000.00,-7000.00,-8000.00,)
# definindo coeficientes que compõem o lado esquerdo das restrições tipo inequação
A=((1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
   (0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0),
   (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0),
   (13.75, 10.0, 8.75, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
   (0.0, 0.0, 0.0, 13.75, 10.00, 8.75, 0.0, 0.0, 0.0),
   (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 13.75, 10.00, 8.75),
   (1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0),
   (0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0),
   (0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0))
# definindo o limite superior das restrições (lado direito das inequações)
b=(160.0,260.0,140.0,1800.0,2200.0,950.0,264.0,352.0,160.0)
#definindo lado esquerdo das retrições tipo igualdade
D=((260.0,260.0,260.0,-160.0,-160.0,-160.0,0.0,0.0,0.0),
   (0.0,0.0,0.0,-140.0,-140.0,-140.0,260.0,260.0,260.0))
#definindo lado direto das retrições tipo igualdade
e=(0.0,0.0)
# definindo a faixa de valores possíveis para cada variável
bnds=((0.0,None),(0.0,None),(0.0,None),
      (0.0,None),(0.0,None),(0.0,None),
      (0.0,None),(0.0,None),(0.0,None))
# chamando linprog para executar a otimização
res=opt.linprog(c,A_ub=A,b_ub=b,A_eq=D,b_eq=e,bounds=bnds)
print("\n\nProblema de Programação Linear")
print("\nRESULTADOS:")
print("Lucro máximo da cooperativa= {:.2f}".format(-res.fun))
print("Área plantada com milho (ha) na fazenda 1= {:.4f}".format(res.x[0]))
print("Área plantada com arroz (ha) na fazenda 1= {:.4f}".format(res.x[1]))
print("Área plantada com feijão (ha) na fazenda 1= {:.4f}".format(res.x[2]))
print("Área plantada com milho (ha) na fazenda 2= {:.4f}".format(res.x[3]))
print("Área plantada com arroz (ha) na fazenda 2= {:.4f}".format(res.x[4]))
print("Área plantada com feijão (ha) na fazenda 2= {:.4f}".format(res.x[5]))
print("Área plantada com milho (ha) na fazenda 3= {:.4f}".format(res.x[6]))
print("Área plantada com arroz (ha) na fazenda 3= {:.4f}".format(res.x[7]))
print("Área plantada com feijão (ha) na fazenda 3= {:.4f}".format(res.x[8]))
print("Otimização foi realizada com sucesso? ",res.success)


