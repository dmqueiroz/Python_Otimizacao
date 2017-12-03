# -*- coding: utf-8 -*-
"""
Programa para minimizar a função
F=x1*x4*(x1+x2+x3)+k2*x3
sujeito a
x1*x2*x3*x4>=k0
x1**2+x2**2+x3**2+x4**2=k1

Vamos supor que k0=1, k1=25 e k2=40

Os limites para todas as variáveis é entre 1 e 5

Created on Fri Oct 27 08:13:08 2017

@author: Daniel M Queiroz
"""
from scipy import optimize as opt
# definindo a função objetivo
def F(x,k2):
    F=x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]*k2
    return F
# definindo a primeira restricao
def produto(x,k0):
    produto=x[0]*x[1]*x[2]*x[3]-k0
    return produto
# definindo a segunda restricao
def soma_dos_quadrados(x,k1):
    soma_dos_quadrados=x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]-k1
    return soma_dos_quadrados
print("\n\nExecutando Problema de Minimização")
par1=(25,)     # defininindo parâmetro k0 do modelo
par2=(40,)     # defininindo parâmetro k1 do modelo
par3=(1,)      # defininindo parâmetro k2 do modelo
limites=((1,5),(1,5),(1,5),(1,5))   # limites das variáveis de decisão
x0=(1,5,5,1)                        # chute inicial
# criando primeira restrição
restricao1={"type": "ineq","fun":produto,"args":par1} 
# criando segunda restrição 
restricao2={"type": "eq","fun":soma_dos_quadrados,"args":par2} 
cj_restricoes=(restricao1,restricao2)
resultado=opt.minimize(F,x0,args=par3,bounds=limites,constraints=cj_restricoes)
print("\n\nRESULTADOS FINAIS:")
print("O valor mínimo da função é {:.4f}".format(resultado.fun))
print("O valor da variável x1 no ponto ótimo é: {:.4f}".format(resultado.x[0]))
print("O valor da variável x2 no ponto ótimo é: {:.4f}".format(resultado.x[1]))
print("O valor da variável x3 no ponto ótimo é: {:.4f}".format(resultado.x[2]))
print("O valor da variável x4 no ponto ótimo é: {:.4f}".format(resultado.x[3]))
print("A otimização foi executada com sucesso? ",resultado.success)

