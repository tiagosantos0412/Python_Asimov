# Strings se comportam como listas de caracteres, retornando somente o índice de uma string
nome = 'Tiago'
print(nome[1])

# Convertendo uma lista para uma tupla
lista = [1,2,3,4]
tupla = tuple(lista)
print(tupla, type(tupla))

# Convertendo de tupla para lista
tupla = list(tuple(tupla))
print(tupla, type(tupla))