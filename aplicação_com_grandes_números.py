# -*- coding: utf-8 -*-
"""Aplicação com grandes números.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WpMJpTNRd8EpP0OedTteqIqjwl0IND7D
"""

import random #Importando a biblioteca random do python para simular a aleatoriedade da simulação
import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

"""# Simulando um dado jogado 10 vezes"""

x = []  
n = 300 #Tamanho da amostra

for i in range (n):
  x.append(random.randint(1,6))

"""#Plotando amostras"""

plt.rcParams['figure.figsize'] = (20,10)

TAMar = np.array(range(n)) 

plt.title('Amostragem da relação Amostras') #adicionando o título
plt.xlabel('Amostras')
plt.ylabel('Jogadas')

plt.ylim(-2, 10)
plt.xlim(0, n + 10)
plt.plot(TAMar, x, label='Amostras')
plt.legend()

plt.plot()

"""# Média"""

soma = 0;
media = []

print(x[0])
print(x[1])
for i in range(n):
  soma = x[i] + soma;
  if i == 0:
    media.append(soma)
  else:
    media.append(soma/(i+1))

media

# reta_media = []
# for i in range(0,n):
#   reta_media.append(media)

plt.title('Amostragem da relação Amostras x Média') #adicionando o título
plt.xlabel('Amostras')
plt.ylabel('Jogadas')

plt.ylim(-2, 10)
plt.xlim(0, n + 10)

plt.plot(TAMar, x, label='Amostras')
plt.legend()

plt.plot(TAMar, media, color="green", label = 'Média')
plt.legend()

"""# O valor esperado
 - A esperança é o somatório do numero (i) vezes a probabilidade (1/6)
"""

Exp = 0;

for i in range(1,7):
  Exp = i*(1/6) + Exp

Exp #podemos ver que o numero experado se aproxima da média

"""# Plot Amostras x Média x Esperança x"""

plt.title('Amostragem da relação Amostras x Média x Esperança') #adicionando o título
plt.xlabel('Amostras')
plt.ylabel('Jogadas')

reta_esperanca=[]
for i in range(0,n):
  reta_esperanca.append(3.5)

plt.ylim(-2, 10) #definindo limites x, y
plt.xlim(0, n + 10)

plt.plot(TAMar, x, label='Amostras')
plt.legend()

plt.plot(TAMar, reta_esperanca, color="red", label = 'Esperança')
plt.legend()

plt.plot(TAMar, media, color="green", label = 'Média')
plt.legend()

plt.show()

