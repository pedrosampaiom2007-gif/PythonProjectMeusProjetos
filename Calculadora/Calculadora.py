numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = numero1 + numero2
    print(f"A soma é {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"A subtração é {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"A multiplicação é {resultado}")
elif operador == "/":
    if numero2 == 0:
        print("Erro: não é possível dividir por zero")
    else:
        resultado = numero1 / numero2
        print(f"A divisão é {resultado}")
else:
    print("Operador inválido")
