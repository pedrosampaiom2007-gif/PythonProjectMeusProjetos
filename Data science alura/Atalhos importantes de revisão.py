# Lista inicial
frutas = ["banana", "maçã", "uva"]

print("Lista inicial:", frutas)

# --------------------------------------------------
# APPEND -> adiciona UM elemento ao final da lista
# --------------------------------------------------
frutas.append("laranja")
print("\nApós append('laranja'):")
print(frutas)

# --------------------------------------------------
# INSERT -> adiciona um elemento em uma posição específica
# --------------------------------------------------
frutas.insert(1, "abacaxi")
print("\nApós insert(1, 'abacaxi'):")
print(frutas)

# --------------------------------------------------
# EXTEND -> adiciona vários elementos de outra lista
# --------------------------------------------------
frutas.extend(["manga", "kiwi"])
print("\nApós extend(['manga', 'kiwi']):")
print(frutas)

# --------------------------------------------------
# INDEX -> encontra a posição de um valor
# --------------------------------------------------
posicao = frutas.index("uva")
print("\nPosição de 'uva':")
print(posicao)

# --------------------------------------------------
# REMOVE -> remove pelo valor
# --------------------------------------------------
frutas.remove("kiwi")
print("\nApós remove('kiwi'):")
print(frutas)

# --------------------------------------------------
# POP -> remove por índice e devolve o elemento removido
# --------------------------------------------------
removido = frutas.pop(2)
print("\nElemento removido com pop(2):")
print(removido)

print("Lista após pop:")
print(frutas)

# --------------------------------------------------
# SORT -> ordena a lista
# --------------------------------------------------
frutas.sort()
print("\nApós sort():")
print(frutas)