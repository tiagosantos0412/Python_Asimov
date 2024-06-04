# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

import random

numero = random.randint(0, 10)
tentativas = 1

print('-' * 60)
print('-               Adivinhe o número                    - ')
print('-' * 60)

while tentativas <= 3:
    chute = int(input(f'Esta é a sua {tentativas}ª tentativa, em qual número estou pensando?\n'))
    if chute == numero:
        print(f'Parabéns você acertou!\nEu estava pensando no número {numero}...')
        break  # Sai do loop se acertar
    elif chute > numero:
        print('Você errou! Chute muito alto')
    elif chute < numero:
        print('Você errou! Chute muito baixo')
    tentativas += 1

if chute != numero:
    print(f'Você usou todas as suas tentativas. Eu estava pensando no número {numero}.')

print('-' * 60)
print('Fim do programa!')
print('-' * 60)