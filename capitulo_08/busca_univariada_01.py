# -*- coding: utf-8 -*-
"""
Programa para maximização da função f(x,y)=y-x-2x**2-2xy-y**2
utilizando o método de eliminação de região univariada

Created on Wed Sep 13 15:31:59 2017

@author: Daniel Marçal de Queiroz
"""
from math import fabs
# função para a qual se quer achar o mínimo
F=lambda x,y:-(y-x-2*x*x-2*x*y-y*y)
# função que calcula o mínimo da função
def elimina_regiao(step,x,y,a,b,LP=0.01):
    """
    A função elimina_região calcula o mínimo da função F. Ela utiliza o método
    de eliminação de região.
    Dados de entrada:
    step: variável inteira, se step for para mantém x constante
          se step for ímpar mantém y constante
    a: limite inferior da faixa de busca do valor mínimo
    b: limite superior da faixa de busca do valor mínimo
    LP: tolerância para busca do valor mínimo, se o usuário não o definí-lo
        o programa assume o valor default de 0.01
    Retorna:
    xm,ym: ponto em que a função tem o menor valor
    Fzm: valor mínimo da função
    """
    # calcula valor médio entre a e b
    zm=(a+b)/2
    # calcula valor da função no ponto médio, se step é par mantém
    # x constante, se step é impar mantém y constante.
    if(step%2==0):
        Fzm=F(x,zm)
    else:
        Fzm=F(zm,y)
    # calcula largura da região inicial
    L=(b-a)
    # loop até que a solução seja encontrada
    while(L>LP):
        # define dois pontos intermediários um entre a 
        # e outro entrexm e entre xm e b
        z1=a+L/4
        z2=b-L/4
        # calcula o valor da função nesses pontos
        if(step%2==0):
            Fz1=F(x,z1)
            Fz2=F(x,z2)
        else:
            Fz1=F(z1,y)
            Fz2=F(z2,y)
        # verifica em que região o mínimo está, se entre a e zm, ou
        # entre zm e b ou entre z1 e z2
        # em seguida atualiza os limites a e b
        if (Fz1<Fzm):
            b=zm
            zm=z1
            Fzm=Fz1
        else:
            if(Fz2<Fzm):
                a=zm
                zm=z2
                Fzm=Fz2
            else:
                a=z1
                b=z2
        # redefine a lagura da faixa
        L=b-a    
    if(step%2==0):
        ym=zm
        xm=x
    else:
        xm=zm
        ym=y
    # retorna o ponto de mínimo e o valor mínimo
    return xm,ym,Fzm
print("\n\nPrograma para obtenção do máximo da função")
print("     f(x,y)=y-x-2*x**2-2*x*y-y**2")
# definindo os valores da região em que se buscará o mínimo para a variável x
ax=-2.0
bx=2.0
# definindo os valores da região em que se buscará o mínimo para a variável y
ay=1.0
by=3.0
# definindo uma tolerância para finalizar o processo e inicializando a 
# variável step
tol = 0.000001
step=0
# chutando um valor inicial para as variáveis x e y e calculando o valor da 
# função no ponto
x=(ax+bx)/2.0
y=(ay+by)/2.0
Fant=F(x,y)
print("\n\nO chute inicial é x= {0:.4f}".format(x))
print("O chute inicial é y= {0:.4f}".format(y))
print("O valor incial da função é: {0:.4f}".format(-Fant))
# iniciando loop
while(True):
    # chama a função que calcula o mínimo, se step é par será buscado
    # yótimo, e step é impar será buscado xótimo.
    x,y,Fmin=elimina_regiao(step,x,y,ay,by)
    step=step+1
    x,y,Fmin=elimina_regiao(step,x,y,ax,bx)
    step=step+1
    # verificando se a função atingiu o valor ótimo
    if(fabs(Fant-Fmin)>tol and step<100):
        Fant=Fmin
    else:
        break
# imprime o resultado
print("\n\nResultado Final:")
print("O valor ótimo é x= {0:.4f}".format(x))
print("O valor ótimo é y= {0:.4f}".format(y))
print("O valor ótimo da função é F= {0:.4f}".format(-Fmin))
print("Número de passos para obtenção da solução foi de {0:3d}".format(step))


