nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

resultado=["aprovado"if media >6 else "reprovado" for media in medias]

print(resultado)

cadastro = [x for x in [nomes, notas, medias,resultado]]
print(cadastro)

lista_completa = [nomes, notas, medias, resultado]
print(lista_completa)