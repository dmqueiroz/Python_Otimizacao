# -*- coding: utf-8 -*-
"""
Programa para achar a patinagem que torna máximo a eficiência tratória

Created on Wed Sep 20 14:11:15 2017

@author: Daniel Marçal de Queiroz
"""
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt  
from math import exp,sqrt
#
# definindo função para cálculo da eficiência tratória com sinal trocado
def ET(s,f1,f2,f3,IC,W,b,d,delta,h):
    # calculando adimensional Bn 
    Bn=(IC*b*d/W)*(1+(5*delta/h)/(3*b/d))
    # calculando coeficiente de resistência ao rolamento rho
    rho=f3/Bn+f2+0.5*s/sqrt(Bn)
    # calculando o coeficiente de tração bruta mig
    mig=0.88*(1-exp(-Bn*s))*(1-exp(-f1*s))+f2
    # calculando a eficiência tratória ET
    ET=(1-s)*(1.0-rho/mig)
    # como queremos maximizar ET, retornaremos -ET
    return -ET
#
print("\n\nPrograma para obter a patinagem que torna máximo")
print("        o valor da eficiência tratória")
# definindo o limite de busca
bnds=(0.005,1.0)
#
# Dados de entrada
IC=1000.0*1000.0    # índice de cone do solo, Pa
W=13000.0           # carga dinâmica sobre a roda, N
b=0.4674            # largura do pneu, m
d=1.552             # diâmetro indeformado do pneu, m
delta=0.0662        # deflexão do pneu, m
h=0.37              # altura da banda de rodagem, m
tipo_pneu="diagonal"  # tipo do pneu
# definindo os parâmetros da equação de tração em função do tipo de pneu
if tipo_pneu=="radial":
    f1=9.5
    f2=0.0325
    f3=0.9
else:
    f1=7.5
    f2=0.04
    f3=1.0
#
# chamando a função minimize_scalar para cálculo do valor mínimo, será
# utilizado o método default que é o método de Brent
resultado=minimize_scalar(ET,bounds=bnds,args=(f1,f2,f3,IC,W,b,d,delta,h))
#
print("\n\nResultados:")
print("Eficiência tratória máxima(%): {0:.4f}".format(-100*resultado.fun))
print("Patinagem ótima (%): {0:.4f}".format(100*resultado.x))
print("A solução foi obtida com sucesso: ",resultado.success)
# gerando gráfico da função
# gerando 101 pontos igualmente espaçado entre a e b
x=np.linspace(1.0,99.0,100)
y=np.zeros(len(x))
# calculando o valor da função em cada um dos 101 pontos
for i in range(100):
    y[i]=-100.0*ET(x[i]/100,f1,f2,f3,IC,W,b,d,delta,h)
# plotando os pontos usando linha de cor vermelha
plt.plot(x,y, 'r')
# plotando o ponto de mínimo usando bola azul
plt.plot(100*resultado.x,-100*resultado.fun,'bo')
# definindo títulos do gráfico e dos eixos
plt.title("Maximizando a Eficiência Tratória de uma Roda")
plt.ylabel("Eficiência Tratória (%)")
plt.xlabel("Patinagem (%)")
# mostrando uma malha na área de plotagem
plt.grid(True)
plt.show()


