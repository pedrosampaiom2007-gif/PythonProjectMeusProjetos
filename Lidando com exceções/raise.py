def media(lista:list=[0])->float:

    calculo=sum(lista)/len(lista)
    if len(lista)>4:
       raise ValueError(" A lista não pode possuir mais de 4 notas ")


    return calculo
try:

    notas=[5,5,6,7,5]

    resultado= media(notas)

except ValueError as e:

    print(e)

except TypeError:

    print("Não é possivel calcular a media do estudante, todos os valores devem ser numéricos")
