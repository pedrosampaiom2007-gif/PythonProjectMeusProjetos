# List comprehension é uma forma simples e concisa de criar listas, sendo que essas listas seguirão alguns padrões, via condicionais, laços e outras expressões.
#O formato padrão é:[expressão for item in lista]


def media(lista: list = [0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default [0]
      Lista com as notas para calcular a média
    return = calculo: float
      Média calculada
    '''

    calculo = sum(lista) / len(lista)

    return calculo


notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

medias=[round(media(nota),1) for nota in notas]
print(medias)


