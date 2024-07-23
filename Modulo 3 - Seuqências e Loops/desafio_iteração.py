# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !
soma = 0
media = 0
auxiliar = 0
notas = [10, 5, 7, 8]
for nota in notas:
   soma += nota
   auxiliar += 1
print(soma)
media = soma / auxiliar
print(f'A Média das notas do aluno é: {media}')

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !
maior_nota = -1
notas = [10, 5, 7, 8]
for i in notas:
   if i > maior_nota:
      maior_nota = i
print(f'A maior nota foi: {maior_nota}.')

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 8 caracteres.
palavras = ['Abacate', 'Enciclopedia', 'Panela', 'Mexerica']
maiores_palavras = []
print(palavras)
for palavra in palavras:
    if len(palavra) >= 8:
       maiores_palavras.append(palavra)
print(f'As maiores palavras encontradas foram: {maiores_palavras}')
