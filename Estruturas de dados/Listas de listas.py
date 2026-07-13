notas_turma=["João" ,8,7,5, "Maria" ,5,2,3, "Miguel" , 8,7,9, "Pedrão" , 10,5,8, "Yasmin" ,7,9,7]


nomes=[]
notas_juntas=[]

for i in range(len(notas_turma)):

    if i %4==0:

        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])


print(nomes)
print(notas_juntas)

notas=[]

for i in range(0,len(notas_juntas),3):

    notas.append([notas_juntas[i],notas_juntas[i+1],notas_juntas[i+2]])

print(notas[0])