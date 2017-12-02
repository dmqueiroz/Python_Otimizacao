# -*- coding: utf-8 -*-
"""
Programa para o cálculo do fatorial de um número

Created on Thu Sep 14 10:51:15 2017

@author: Daniel Marçal de Queiroz
"""
print("\n\nPrograma para o cálculo do fatorial de um número\n")
n=int(input("Digite o número para o qual você quer o fatorial: "))
i=1
fatorial=1
while(i<n):
    i=i+1
    fatorial=fatorial*i
print("\nO valor do fatorial é ",fatorial)


