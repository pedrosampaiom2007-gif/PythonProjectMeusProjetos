idade= int(input("Digite sua idade:\n "))

if idade < 16  :
    print(" Você não pode votar, Idade insuficiente")
elif idade >= 16 and idade < 18 :
    print("Seu voto é opcional")
elif idade >= 18 and idade < 65 :
    print("Seu voto é obrigatório")
elif idade >= 65 :
    print("Seu voto é opcional")
