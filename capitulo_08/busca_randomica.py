# -*- coding: utf-8 -*-
"""
Programa para obter o máximo da função f(x,y)=y-x-2x**2-2xy-y**2

Created on Tue Oct  3 12:33:03 2017

@author: Daniel Marçal de Queiroz
"""
import random as rnd   # importa biblioteca random
from math import inf   # importa função infinito da biblioteca math
maxf=-inf  # inicializa o valor máximo com menos infinito
n = 1000   # define o número de iterações como sendo 1000
# define limites para a variável x
xmin=-2    
xmax=2
# define limites para a variável y
ymin=1
ymax=3
# incia loop com o número de iterações
for j in range (n):
    # gera valores aleatórios de x e y e calcula o valor da função no ponto
	x = xmin+ (xmax-xmin)*rnd.random()
	y = ymin + (ymax-ymin)*rnd.random()
	fn = y - x - 2*x*x - 2*x*y - y*y
    # testa se o valor da função que acabou de ser calculado é maior que
    # o valor máximo atual, se verdadeiro atualiza os valores da resposta
	if fn > maxf:
		maxf = fn
		maxx = x
		maxy = y
# imprime o resultado
print("\n\nPrograma para o cálculo do valor máximo da função")
print("          f(x,y)=y-x-2*x**2-2*x*y-y**2")
print('\nValor ótimo de x= {0:.5f}'.format(maxx))
print('Valor ótimo de y= {0:.5f}'.format(maxy))
print('Valor máximo da função F= {0:.5f}'.format(maxf))


