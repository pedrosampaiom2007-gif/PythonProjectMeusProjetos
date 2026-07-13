#Importando bibliotecas

import matplotlib

print(matplotlib.__version__)
#Importando Pacotes da biblioteca

import matplotlib.pyplot as plt

estudantes=["Pedro","Raul","Brasão"]
notas=[6,8,7]

plt.bar(x=estudantes,height=notas)
#plt.show()

#Importando funções específicas da biblioteca

from random import choice

estudantes_2=["Leôncio","Jordan","Lebron","Maicon"]

A=choice(estudantes_2)

print(A)