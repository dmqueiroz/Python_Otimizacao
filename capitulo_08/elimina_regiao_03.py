# -*- coding: utf-8 -*-
"""
Programa para minimização de função utilizando o método de eliminação de região

Created on Wed Sep 13 15:31:59 2017

@author: Daniel Marçal de Queiroz
"""
# função para a qual se quer achar o mínimo
F=lambda x:2*x+3/x
# função que calcula o mínimo da função
def elimina_regiao(a,b,LP=0.01):
    """
    A função elimina_região calcula o mínimo da função F. Ela utiliza o método
    de eliminação de região.
    Dados de entrada:
    a: limite inferior da faixa de busca do valor mínimo
    b: limite superior da faixa de busca do valor mínimo
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
# definindo os valores da região em que se buscará o mínimo
a=0.1
b=2.0
# chama a função que calcula o mínimo
xmin,Fmin=elimina_regiao(a,b)
# imprime o resultado
print("O valor mínimo é: {0:.2f}".format(Fmin))
print("O ponto em que o valor é mínimo é: {0:.2f}".format(xmin))

