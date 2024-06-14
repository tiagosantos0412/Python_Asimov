lista1 = ['João', 'Clara', 'Paulo', 'Maria']

# Retorna o item do índice 0, pois selecionei o elemento do indice de 0 até o ínicio de 1, ignorando todo o restante
print(lista1[0:1])
# Retorna os itens do índice 1 e 2
print(lista1[1:3])
# Retorna o item do índice 4, pois selecionei do 3 até o incio do 4
print(lista1[3:4])
# Retrona o tamanho da lista
print(len(lista1))
# Retrona os itens do índice 1 em diante
print(lista1[1:])
# Atribui à variável n o número que corresponde o tamanho da lista1
n = len(lista1)
# Retorna o valor total da lista com todos os índices
print(lista1[:n])
# Retorna o valor total da lista com todos os índices
print(lista1[:])

nome = 'Tiago'
# Retorna as letras correspondentes aos índices 2 ao 5
print(nome[2:5])

numeros = [1,2,3,4,5,6,7,8,9,10]
# Retrona os dados da lista de números pulando de 2 em 2
print(numeros[0:len(numeros):2])
# Retrona do começo até o final, pulando de 2 em 2
print(numeros[::2])
# Retorna a lista do inicio ao fim
print(numeros[::1])
# Retrona o valor da lista de números de trás para frente
print(numeros[::-1])

