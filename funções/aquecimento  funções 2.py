usuario=int(input("Digite um número de 1 a 10 para ver sua tabuada: "))


def tabuada(numero:int):
    print(f"A tabuada do {usuario} é: ")
    for i in range(1,10):
        print(f"{usuario} x {i} = {usuario*i}")


print(tabuada(usuario))