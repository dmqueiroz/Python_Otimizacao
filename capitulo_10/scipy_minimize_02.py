# -*- coding: utf-8 -*-
"""
Programa criado para otimização de uma função de várias variáveis dada por:
    Minimizar f(x)=x1*x4*(x1+x2+x3)+x3
Sujeito a:
    x1*x2*x3*x4 maior ou igual a 25
    x1**2+x2**2+x3**2+x4**2=40
    x1,x2,x3 e x3 entre 1 e 5
    chute inicial x0=(1,5,5,1)
    
Created on Wed Oct 25 10:07:41 2017

@author: Daniel Marçal de Queiroz
"""
from scipy import optimize as opt            
# define a função objetivo a ser minimizada
F=lambda x:x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]
# define restrição associada ao produto das variáveis de decisão
restricao_produto=lambda x:x[0]*x[1]*x[2]*x[3]-25
# define restrição associada à soma do quadrado das variáveis de decisão
restricao_soma_quadrado=lambda x:x[0]**2+x[1]**2+x[2]**2+x[3]**2-40
# define limites para as variáveis de decisão
bnds=((1,5),(1,5),(1,5),(1,5))
# define um chute inicial para as variáveis de decisão
x0=(1,5,5,1)
# define as restrições do problema
con1={"fun": restricao_produto, "type": "ineq"}
con2={"fun": restricao_soma_quadrado, "type": "eq"}
# chama a função de otimização
res=opt.minimize(F,x0,bounds=bnds,constraints=(con1,con2))
print('\n\nPrograma para minimizar o valor da função objetivo')
print('\n\nResultados:')
print('O valor mínimo da função é {:.3f}'.format(res.fun))
print('O valor da variável x1 no ponto ótimo é {:.3f} '.format(res.x[0]))
print('O valor da variável x2 no ponto ótimo é {:.3f} '.format(res.x[1]))
print('O valor da variável x3 no ponto ótimo é {:.3f} '.format(res.x[2]))
print('O valor da variável x4 no ponto ótimo é {:.3f} '.format(res.x[3]))
print('O método convergiu com sucesso? ',res.success)



