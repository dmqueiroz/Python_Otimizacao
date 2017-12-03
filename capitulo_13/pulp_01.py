# -*- coding: utf-8 -*-
"""
Problema da mochila

Created on Fri Nov 10 09:16:59 2017

@author: Daniel Marçal de Queiroz
"""

import pulp
# Inicializando com a definição do problema
model = pulp.LpProblem("Maximimizando o valor de produtos na mochila", pulp.LpMaximize)
p1 = pulp.LpVariable('Produto 1', lowBound=0, cat='Integer')
p2 = pulp.LpVariable('Produto 2', lowBound=0, cat='Integer')
p3 = pulp.LpVariable('Produto 3', lowBound=0, cat='Integer')
p4 = pulp.LpVariable('Produto 4', lowBound=0, cat='Integer')
p5 = pulp.LpVariable('Produto 5', lowBound=0, cat='Integer')
p6 = pulp.LpVariable('Produto 6', lowBound=0, cat='Integer')
# Função objetivo
model += 8*p1 + 6*p2 + 10*p3 + 4*p4 + 7*p5 + 3*p6, "Valor Transportado"

# Restrições
model += 50*p1 + 30*p2 + 60*p3 + 25*p4 + 40*p5 + 15*p6 <= 100
# Resolve o problema
model.solve()
pulp.LpStatus[model.status]
print("\n\nSolução do Problema da Mochila Utilizando Pulp\n\n")
print("Resultados:")
# Imprime os valores das variáveis de decisão
print("Quantidade do produto 1 na mochila = {}".format(p1.varValue))
print("Quantidade do produto 2 na mochila = {}".format(p2.varValue))
print("Quantidade do produto 3 na mochila = {}".format(p3.varValue))
print("Quantidade do produto 4 na mochila = {}".format(p4.varValue))
print("Quantidade do produto 5 na mochila = {}".format(p5.varValue))
print("Quantidade do produto 6 na mochila = {}".format(p6.varValue))
print("Valor transportado ótimo = {}".format(pulp.value(model.objective)))


