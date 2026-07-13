# Lista que irá armazenar os 5 números inteiros
lista_numeros = []

for i in range(0,5):

  numero=int(input("digite um número: "))
  lista_numeros.append(numero)

print(f" A ordem reversa é: {lista_numeros[::-1]}")