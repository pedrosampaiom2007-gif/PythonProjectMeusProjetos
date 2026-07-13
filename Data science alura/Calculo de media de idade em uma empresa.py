# Especificamos os dados para um dicionário
dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
total_idades=0

for setor,idades in dados.items():

    media=sum(idades)/len(idades)
    print(f"A média  de idades do  {setor} é de: {media}\n")

todas_idades = []

for i in dados.values():
    todas_idades.extend(i)

media_geral= sum(todas_idades)/len(todas_idades)

print(f"A média de idades geral é de: {media_geral}")

for j in todas_idades:

    if j> media_geral:
        total_idades+=1
print(f"A quantidade de pessoas com a idade acima da idade geral é de: {total_idades}")





