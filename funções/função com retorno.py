notas = [7, 8, 9, 7, 6]

def boletim(lista):
    calculo = sum(lista) / len(lista)


    if calculo >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # O RETURN DEVE FICAR FORA DOS 'IFs'
    # Alinhado com o início do if/else, para rodar em ambos os casos
    return (calculo, situacao)

# Como a função retorna DOIS valores de uma vez só (uma tupla),
# você pode desempacotar esses valores diretamente em duas variáveis:s
media, status = boletim(notas)

print(f"O aluno atingiu a média de {media} e foi {status}.")