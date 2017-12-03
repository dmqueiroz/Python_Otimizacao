# -*- coding: utf-8 -*-
"""
Programa para verificar se cada número de 3 a 100 é primo ou não

Created on Thu Sep 14 16:02:05 2017

@author: Daniel Marçal de Queiroz
"""
i=3
while i<=100:
    resto_min=101
    for j in range(2,i):
        resto=i%j
        if(resto<resto_min):
            resto_min=resto
    if(resto_min!=0):
        print("O número ",i," é primo!!!")
    else:
        print("O número ",i," não é primo.")
    i=i+1


