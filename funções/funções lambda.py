#nota=float(input("Digite a nota do estudante: "))

def qualitativo(x):
    return x+0.5

#print(qualitativo(nota))

# Uso da mesma função para uma função lambda

qualitativo= lambda x: x + 0.5

#print(qualitativo(nota))

# Função lambda com mais parâmetros

n1=float(input("Digite sua primeira nota: "))
n2=float(input("Digite sua segunda nota: "))
n3=float(input("Digite sua terceira nota: "))

media_ponderada= lambda x,y,z: (x*3+y*2+z*5)/10
media_estudante=media_ponderada(n1,n2,n3)
print(media_estudante)



