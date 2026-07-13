notas=[]

for i in range(0, 4):
    while True:
        nota = float(input("Digite uma nota de 0 a 10:\n" ))

        if nota > 10 or nota < 0:

            print("Digite uma nota Válida")

        elif nota <= 10 and nota >= 0:
            notas.append(nota)
            break

def analista(analis:list):

    maior=max(analis)
    menor=min(analis)
    media = sum(analis) / len(analis)
    if media>=6:

        situacao="Aprovado"

    elif media<6:

        situacao= "Reprovado "

    return (media,maior,menor,situacao)

media,maior,menor,situacao=analista(notas)
print(f"O(a) estudante obteve uma media de {media:.2f}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")










