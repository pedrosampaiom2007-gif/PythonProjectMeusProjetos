numero = int(input("Digite um número inteiro qualquer: "))


while numero <= 0:
    numero = int(input("Número inválido! Digite um número positivo maior que 0: "))

soma = 0

for n in range(1, numero + 1):
    soma+= n

print(f"A soma de 1 até {numero} é: {soma}")