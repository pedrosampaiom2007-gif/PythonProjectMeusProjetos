from random import randrange

participantes= (int(input("Digite o número de participantes: ")))
if participantes==0:

    print("Digite um número a partir de 1")

a= randrange(participantes)

print(f"Parabéns número  {a}, você foi o escolhido")