pedrao=[97, 80, 94, 33, 80, 1, 16, 53, 62, 32, 24, 99]

def mult_3(lista):
    multiplo_3=[]

    for i in lista:
        if i%3==0:
         (multiplo_3.append(i))

    return multiplo_3

a=mult_3(pedrao)

print(a)