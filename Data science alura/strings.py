linguagem = 'Python'

print(linguagem[0], linguagem[1], linguagem[2], linguagem[-3], linguagem[-2], linguagem[-3])

duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split()
print(lista_palavras)


misturas = ['Tintas: vermelho, azul e amarelo',

            'Verde: mistura de azul e amarelo',

            'Laranja: mistura de vermelho e amarelo',

            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas)