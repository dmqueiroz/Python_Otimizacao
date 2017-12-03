# -*- coding: utf-8 -*-
"""
Programa para o cálculo de ventiladores em silos para secagem e armazenagem
de grãos

Created on Thu Sep 14 13:44:34 2017

@author: Daniel Marçal de Queiroz
"""
import math
print("\nPrograma para o cálculo da potência do ventilador necessária para")
print("                  silos secadores de grãos\n")
parametros = {'milho': [20.7, 30.4, 750.0],
               'soja': [10.2, 16.0, 750.0],
              'arroz': [25.7,13.2, 600.0]}
prod=input("Qual o produto que será secado no silo (milho, soja ou arroz)?\n")
par=parametros[prod.lower()]
d=float(input("\nQual é o diâmetro do silo (m)?\n"))
h=float(input("\nQual é a altura da camada de grãos (m)?\n"))
Qa=float(input("\nQual é a vazão por unidade de área do secador (m**3/(s.m**2))?\n"))
# Define fator de majoração da perda de carga em relação ao previsto pela
# equação de Shedd.
k=1.5
# Define a eficiência do ventilador, decimal
eff=0.7
# Calcula a área do silo, m**2
Area=math.pi*d*d/4
# Calcula o volume de grãos no silo, m**3
Volume=Area*h
# Calcula a massa de grãos no silo, kg
Massa=Volume*par[2]
# Calcula a vazão de ar que o ventilador tem que produzir, m**3/s
Vazao=Qa*Area
# Calcula a perda de carga na camada de grãos, kPa
deltaP=k*h*par[0]*Qa**2/math.log(1+par[1]*Qa)
# Calcula a potência do ventilador, kW
pot=Vazao*deltaP/eff
print("\nRESULTADOS:")
print("Área do silo (m**2).......................: {0:.2f}".format(Area))
print("Volume do silo (m**3).....................: {0:.2f}".format(Volume))
print("Massa de produto (kg).....................: {0:.2f}".format(Massa))
print("Vazão de ar do ventilador (m**3/s)........: {0:.2f}".format(Vazao))
print("Perda de carga na camada de grãos (kPa)...: {0:.2f}".format(deltaP))
print("Potência do ventilador (kW)...............: {0:.2f}".format(pot))


