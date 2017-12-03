# -*- coding: utf-8 -*-
"""
Programa de otimização utilizando o método da secante

Criado em 27 de setembro de 2017

@author: Daniel Marçal de Queiroz
"""
import numpy as np
import matplotlib.pyplot as plt
from math import nan, fabs
#
# define a função a ser otimizada
f=lambda x:2*x+3/x
#
# define a função que calcula a primeira derivada
fL=lambda x:2-3/(x*x)
#
# define a função que calcula o valor ótimo pelo método da secante
def secante(x0,x1,tol):
    xn_menos_um=x0
    xn=x1
    maxit=100     # número máximo de iterações
    iter=0        # número de iterações já realizadas
    dx=nan
    while True:
      xn_mais_um=xn-fL(xn)*(xn-xn_menos_um)/(fL(xn)-fL(xn_menos_um))
      iter=iter+1
      dx=fabs(xn_mais_um-xn)
      if(dx<tol or iter>maxit):
          break
      else:
          xn_menos_um=xn
          xn=xn_mais_um
    return xn_mais_um,f(xn_mais_um),dx,iter
#
# Chutando dois valores iniciais
x0=1.5
x1=2.0
#
# Definindo um valor de erro máximo
tol=0.01
#
# Chamando função que calcula o valor ótimo
valor_otimo=secante(x0,x1,tol)
#
# apresentando a solução
print("\nPrograma para minimização de uma função pelo método da secante\n\n")
print('O valor de x ótimo é {:6.2f}'.format(valor_otimo[0]))
print('O valor ótimo da função é {:6.2f}'.format(valor_otimo[1]))
print('O valor do erro é {:6.5f}'.format(valor_otimo[2]))
print('O número de iterações para a solução foi {:d}'.format(valor_otimo[3]))

# criando um vetor com 101 valores de x entre 0.1 e 10
x=np.linspace(0.1,5,101)
#
# calculando os 101 valores de y = f(x) correspondentes
y=f(x)
#
# criando um gráfico y versus x
fig = plt.figure()
#
# Adicionando eixos à figura
axes=fig.add_axes([0.1,0.1,0.8,0.8])
#
# Adicionando dados ao gráfico
axes.plot(x,y,'b')
axes.plot(valor_otimo[0],valor_otimo[1],'ro')
#
# Adicionando título nos eixos
axes.set_ylabel('Valores da função f(x)')
axes.set_xlabel('Valores da variável independente x')
axes.set_title('Função a ser otimizada')
plt.grid(True)


