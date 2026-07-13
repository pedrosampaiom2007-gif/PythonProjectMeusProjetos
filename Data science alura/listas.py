lista= ["Fabrício Daniel", 6.0 , 9.0, 8.0, True]
lista[3]= 10

for elemento in lista:
    print(elemento)


media=(lista[1] + lista[2] + lista[3])/3
print(f"{media:.2f}")

print(lista[::])

print(lista[2:])

print(lista[2:4])