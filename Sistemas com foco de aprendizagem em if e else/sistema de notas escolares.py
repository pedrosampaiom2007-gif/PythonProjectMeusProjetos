nota1 = float(input("Digite a sua primeira nota:\n"))
nota2 = float(input("Digite a sua segunda nota:\n"))
nota3 = float(input("Digite a sua terceira nota:\n"))
nota4 = float(input("Digite a sua quarta nota:\n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if any(nota > 10 for nota in [nota1, nota2, nota3, nota4]):
    print("Digite um número válido")
elif media < 4:
    print("Você foi reprovado")
elif media < 6 and media >= 4:
    print("Você está de recuperação")
elif media > 6:
    print("Você foi aprovado")