# -*- coding: utf-8 -*-
"""
Programa para minimização de função utilizando o método de eliminação de região

Created on Wed Sep 13 15:31:59 2017

@author: Daniel Marçal de Queiroz
"""
import math
import numpy as np        # importando biblioteca que tem funções numéricas
import matplotlib.pyplot as plt # importando biblioteca geração de gráficos
# função para a qual se quer achar o mínimo
F=lambda x:-(2*math.sin(x)-x*x/10)
# função que calcula o mínimo da função
def elimina_regiao(a,b,LP=0.01):
    """
    A função elimina_região calcula o mínimo da função F. Ela utiliza o método
    de eliminação de região. Para executar essa função você precisa definir 
    a função a ser minimizada chamando-a de F e o argumento a ser passado para
    F e é o valor para o qual você quer calcular F.
    
    Dados de entrada:
    a: limite inferior da faixa de busca do valor mínimo
    b: limite superior da faixa de busca do valor máximo
    LP: tolerância para busca do valor mínimo, se o usuário não o definí-lo
        o programa assume o valor default de 0.01
    
    Retorna:
    xm: ponto em que a função tem o menor valor
    Fxm: valor mínimo da função
    
    """
    # calcula valor médio entre a e b
    xm=(a+b)/2
    # calcula valor da função em xm
    Fxm=F(xm)
    # calcula largura da região inicial
    L=(b-a)
    # loop até que a solução seja encontrada
    while(L>LP):
        # define dois pontos intermediários um entre a 
        # e outro entrexm e entre xm e b
        x1=a+L/4
        x2=b-L/4
        # calcula o valor da função nesses pontos
        Fx1=F(x1)
        Fx2=F(x2)
        # verifica em que região o mínimo está, se entre a e xm, ou
        # entre xm e b ou entre x1 e x2
        # em seguida atualiza os limites a e b
        if (Fx1<Fxm):
            b=xm
            xm=x1
            Fxm=Fx1
        else:
            if(Fx2<Fxm):
                a=xm
                xm=x2
                Fxm=Fx2
            else:
                a=x1
                b=x2
        # redefine a lagura da faixa
        L=b-a
    # retorna o ponto de mínimo e o valor mínimo
    return xm,Fxm
print("\n\nPROGRAMA PARA ACHAR O MÍNIMO DE UMA FUNÇÃO")
print("     MÉTODO DE ELIMINAÇÃO DE REGIÃO\n")
# definindo os valores da região em que se buscará o mínimo
a=0
b=4
print("Limite inferior da faixa: {0:.2f}".format(a))
print("Limite superior da faixa: {0:.2f}".format(b))
# chama a função que calcula o mínimo
xmin,Fmin=elimina_regiao(a,b)
# imprime o resultado
print("\nRESULTADOS:")
print("O valor mínimo é: {0:.2f}".format(Fmin))
print("O ponto em que o valor é mínimo é: {0:.2f}".format(xmin))
# gerando gráfico da função
# gerando 101 pontos igualmente espaçado entre a e b
x=np.linspace(a,b,101)
y=np.zeros(len(x))
# calculando o valor da função em cada um dos 101 pontos
for i in range(101):
    y[i]=2*math.sin(x[i])-x[i]*x[i]/10
# plotando os pontos usando linha de cor vermelha
plt.plot(x,y, 'r')
# plotando o ponto de mínimo usando bola azul
plt.plot(xmin,-Fmin,'bo')
# definindo a área de plotagem
plt.axis([0,4,-3,2])
# definindo títulos do gráfico e dos eixos
plt.title("Procurando o mínimo de uma função")
plt.ylabel("Valor de F(x)")
plt.xlabel("Valor de x")
# mostrando uma malha na área de plotagem
plt.grid(True)
plt.show()
