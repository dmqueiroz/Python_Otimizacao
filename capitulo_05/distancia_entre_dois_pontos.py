# -*- coding: utf-8 -*-
"""
Programa para cálculo da distância entre pontos

Criado em 15 de setembro de 2017

@author: Daniel Marçal de Queiroz
"""
import math                     # importa funções matemáticas
def distancia(x1,y1,x2,y2):
    """
    Essa função calcula a distância entre dois pontos.

    Entrada:
    Coordenadas do ponto 1: x1,y1
    Coordenadas do ponto 2: x2,y2

    Retorna:
    Distância entre os dois pontos: d
    """
    dx=x1-x2                  # calcula delta x
    dy=y1-y2                  # calcula delt y
    d2=dx*dx+dy*dy            # calcula o quadrado da distância entre pontos 
    d=math.sqrt(d2)           # calcula a distância
    return d                  # retorna o valor para o programa
# definindo coordenadas do ponto 1
p1x=0.0
p1y=0.0
# definindo coordenadas do ponto 2
p2x=3.0
p2y=4.0
# chamando função para calcular distância entre os pontos 1 e 2
dist=distancia(p1x,p1y,p2x,p2y)
print("A distância entre 1 e 2 é: {0:.2f}".format(dist))


