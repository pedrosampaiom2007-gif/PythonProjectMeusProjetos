estudantes=["Pedro","João","Maria","Mateus"]

from random import randint

def gera_codigo():
    return str(randint(0,999))

codigo_estudante=[]

for i in range(len(estudantes)):

    codigo_estudante.append((estudantes[i],estudantes[i][0]+ gera_codigo()))

print(codigo_estudante)