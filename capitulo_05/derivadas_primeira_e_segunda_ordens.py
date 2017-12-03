# -*- coding: utf-8 -*-
"""
Programa para calcular as derivadas de primeira e segunda ordem de uma
função em um dado ponto

Criado em 15 de setembro de 2017

@author: Daniel Marçal de Queiroz
"""
import math                         # importando a biblioteca math
f=lambda x:2*math.sin(x)-x*x/10     # função para cálculo da derivada
def derivadas(f,x,h=0.0001): 
    """
    A função derivadas calcula as derivadas de primeira e segunda ordem.

    Dados:
    a função a ser derivada: f
    o ponto em que se quer calcular a derivada: x
    o incremento para calculo das derivadas: h (se não for especificado
    pelo usuário o valor default é 0.0001)

    Retorna:
    o valor da derivada de primeira ordem: df
    o valor da derivada de segunda ordem: ddf
    """
    # derivada de primeira ordem, diferenças centradas
    df=(f(x+h)-f(x-h))/(2.0*h)
    # derivada de segunda ordem, diferenças centradas         
    ddf=(f(x+h)-2.0*f(x)+f(x-h))/h**2  
    return df,ddf                      # retorna o valor das duas derivadas
print("\nPrograma para o cálculo de derivadas de primeira e segunda ordem\n\n")
der_01,der_02=derivadas(f,0.5)         # calcula a derivada para x=0.5
print("O valor da primeira derivada= {0:.4f}".format(der_01))
print("O valor da segunda derivada= {0:.4f}".format(der_02))


