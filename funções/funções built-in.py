notas={"1- Trimestre":8.5, "2- Trimestre": 9.5,"3- Trimestre":7}

print(notas)

soma= sum(notas.values())

indice= len(notas.values())

media= soma/indice

print (f"{media:.1f}")

a=round(media,1)
print(a)