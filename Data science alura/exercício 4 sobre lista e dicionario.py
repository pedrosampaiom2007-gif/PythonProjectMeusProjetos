lista=[]

numero=int(input("Digite qualquer número: "))


for i in range(2,numero):

    primo=True

    for j in range(2,i):
        if i%j==0:
            primo=False
            break

    if primo:
       lista.append(i)

print(lista)