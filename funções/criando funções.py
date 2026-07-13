#Funções sem parâmetros

def media():

    calculo=(8+5+8)/3

    print(calculo)

print(media())

#Função com parâmetro

def medias(nota_1,nota_2,nota_3):

    caalculo= (nota_1+nota_2+nota_3)/3
    print(caalculo)
print(medias(9,2,5))
nota=[9,5,2,7,9,8]

def mediao(lista):
    calc=sum(lista)/len(lista)

    print(calc)

#print(mediao(notas))

#Funções que retornam valores

notas=[9,5,5,7,9,8]

def mediao(lista):
    calc=sum(lista)/len(lista)
    return calc

resultado=mediao(notas)

print(resultado)
