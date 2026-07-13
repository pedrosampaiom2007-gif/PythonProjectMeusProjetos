aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

result=[i[1] for i in aluguel if i[0]=='Apartamento']

print(result)

