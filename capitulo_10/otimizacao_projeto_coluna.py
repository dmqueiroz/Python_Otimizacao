# -*- coding: utf-8 -*-
"""
Programa otimização do projeto de uma coluna

Created on Tue Oct 17 15:05:16 2017

@author: Daniel Marçal de Queiroz
"""
# importando optimize de scicpy
from scipy import optimize as opt            
from math import pi
# define a função objetivo, para minimizar custo de implantação da
# coluna
C=lambda x,H,rho,E,P,Sad:0.4*pi*x[0]*x[1]*H*rho+2*x[0]
# define função que verifica se a tensão é menor que a tensão admissível
forca_compressao=lambda x,H,rho,E,P,Sad:Sad*pi*x[0]*x[1]-P
# define função que verifica se a força crítica de flambagem não é ultrapassada
flambagem=lambda x,H,rho,E,P,Sad:pi**3*(E/H**2)*x[0]*x[1]*(x[0]*x[0]+x[1]*x[1])/8-P
# define limites para diâmetro interno e espessura da coluna
bnds=((1,10),(0.1,1))
# define um chute inicial para diâmetro interno e espessura da coluna
x0=(5,0.5)
H=275.0       # altura da coluna, cm
rho=0.025     # peso específico da coluna,N/cm**3
E=9.0E6       # módulo de elasticidade N/cm**2
P=20000.0     # carga aplicada na coluna, N
Sad=5500.0    # tensão admissível do material à compressão, N/cm**2
# cria tuple com os parâmetros adcionais do problema
parametros=(H,rho,E,P,Sad)
# define as restrições do problema
con1={"fun": forca_compressao, "type": "ineq","args":parametros}
con2={"fun": flambagem, "type": "ineq","args":parametros}
# chama a função de otimização
res=opt.minimize(C,x0,args=parametros,bounds=bnds,constraints=(con1,con2))
print('\n\nPrograma para minimizar o peso de uma coluna')
print('\nDados de Entrada:')
print('Altura da coluna (m) = {:.2f}'.format(H))
print('Peso específico do material (N/cm**2) = {:.3f}'.format(rho))
print('Módulo de elasticidade do material (MPa) = {:.2f}'.format(E/1.0E6))
print('Carga aplicada na coluna (kN) = {:.2f}'.format(P/1000))
print('Tensão admissível do material (kN/cm**2) = {:.2f}'.format(Sad/1000))
print('\n\nResultados:')
print('O valor do custo mínimo da coluna é ${:.3f}'.format(res.fun))
print('O valor do diâmetro interno da coluna é {:.3f} cm'.format(res.x[0]))
print('O valor da espessura da coluna é {:.3f} cm'.format(res.x[1]))
print('O método convergiu com sucesso? ',res.success)


