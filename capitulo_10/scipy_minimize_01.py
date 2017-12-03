# -*- coding: utf-8 -*-
"""
Programa para maximizar a função f(x,y)=y-x-2x**2-2xy-y**2

Created on Tue Oct 17 13:58:15 2017

@author: Daniel Marçal de Queiroz	
"""
# importando optimize de scicpy
from scipy import optimize as opt             
# define a função objetivo, para maximizar f(x,y) podemos minimizar -f(x,y)
# x será substituído por x[0] e y por x[1]
f=lambda x:-(x[1]-x[0]-2*x[0]*x[0]-2*x[0]*x[1]-x[1]*x[1])
# define o tuple com os limites das variáveis x e y
bnds=((-2,2),(1,3))
# define um chute inicial
x0=(-0.5,2)
# chama a função de otimização
res=opt.minimize(f,x0,bounds=bnds)
print('\n\nPrograma para maximizar a função f(x,y)=y-x-2x**2-2xy-y**2')
print('             no intervalo x=(-2,2) e y=(1,3))')
print('\nO valor da função objetivo ótimo é {:.3f}'.format(-res.fun))
print('O valor da variável de decisão x é {:.3f}'.format(res.x[0]))
print('O valor da variável de decisão y é {:.3f}'.format(res.x[1]))
print('O método convergiu com sucesso? ',res.success)


