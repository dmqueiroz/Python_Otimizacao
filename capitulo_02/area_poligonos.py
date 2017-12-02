# -*- coding: utf-8 -*-
"""
Programa para o cálculo de área da área de triângulos, quadrados e retângulos

Created on Wed Aug 30 16:33:59 2017

@author: Daniel Marçal de Queiroz
"""
area=None
print("\n\nPrograma para cálculo de área de polígonos")
print("\nDados de Entrada:")
fig=int(input("Digite\n"
    "<1> para calcular a área de triângulo\n"
    "<2> para calcular a área de quadrado\n"
    "<3> para calcular a área de retângulo ....: "))
if(fig==1):
    base=float(input("\nQual é a base do triângulo? "))
    altura=float(input("\nQual é a altura do triângulo? "))
    area=base*altura/2
elif(fig==2):
    lado=float(input("\nQual é o lado do quadrado? "))
    area=lado*lado
elif(fig==3):
    lado1=float(input("\nQual é o comprimento do retângulo? "))
    lado2=float(input("\nQual é a altura do retângulo? "))
    area=lado1*lado2
else:
    print("\nA opção não é válida, rode novamente com opção válida")
if(area!=None):
    print("\n\nResultados:")
    print("A área do polígono é ",area)
