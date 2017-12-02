# -*- coding: utf-8 -*-
"""
Programa para verificar se um número é primo

Created on Thu Sep 14 10:51:15 2017

@author: Daniel Marçal de Queiroz
"""
print("\n\nPrograma para verificar se um número é primo\n")
n=int(input("Digite o número para o qual você quer saber se é primo: "))
i=2
mensagem="Resposta: O número " + str(n) + " é primo"
while(i<n):
    if (n%i==0):
        mensagem="Resposta: O número "+ str(n) +" não é primo"
        break
    i=i+1
print(mensagem)


