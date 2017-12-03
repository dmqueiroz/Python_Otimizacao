# -*- coding: utf-8 -*-
"""
Programa cálculo da perda de carga em camada de milho

Created on Wed Aug 30 11:26:54 2017

@author: Daniel M. Queiroz
"""
import math
#
# definindo a função que calcula a perda de carga equação de Shedd
delta_p=lambda a,b,Q,A,h,k:k*h*(a*(Q/A)**2)/math.log(1+b*Q/A)
#
# definindo dados de entrada
a=20.700     # coeficiente da equação de Shedd associado ao milho
b=10.2       # coeficiente da equação de Shedd associado ao milho
Q=2          # vazão de ar
A=10         # área da seção do secador
h=1.20       # altura da camada de grãos
k=1.8        # outros fatores de perda de carga
print("\n\nCalculando a perda de carga em secador de milho")
print("\nDados de Entrada:")
print("Vazão de ar (m**3/s)= ",Q)
print("Área da seção transversal (m**2)= ",A)
print("Altura da camada de grãos (m)= ",h)
print("Fator que contempla os outros elementos do sistema= ",k)
# 
# chamando a função que calcula a perda de carga
perda_carga=delta_p(a,b,Q,A,h,k)
#
# imprimindo o resultado
print("\nResultados:")
print("A perda de carga na camada de milho é ",perda_carga," kPa")


