biologia={'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
soma_maior=0

area_maior=""




for chaves,valores in biologia.items():

    media=sum(valores)/len(valores)

    print(f"A média de biodiversidade da {chaves} é de: {media}\n")

    diversidade = sum(valores)


    if diversidade> soma_maior:
        soma_maior=diversidade
        area_maior=chaves

print(f"A região com maior diversidade é {area_maior}")



media_total=[]

for i in biologia.values():
    media_total.extend(i)

media_geral= sum(media_total)/len(media_total)

print(f"A media geral de biodiversidade é de {media_geral} ")
