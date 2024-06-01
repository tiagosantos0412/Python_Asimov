"""Desafio:

    Crie um programa que:
    Peça pelo seu nome e idade
    Da oi pra você
    Conta quantas letras o seu nome possui
    Fala quantos anos você tem e quantos terá daqui a 5 anos
"""

print('Entrevista')

nome = input('Qual o seu nome?   ')
idade = int(input('Qual a sua idade?   '))

print('Oi ', nome)
caracteres = len(nome)
print(f'Seu nome possui {caracteres} caracteres.')
idade_acrescida = idade + 5
print(f'{nome}, você tem {idade} anos e daqui a 5 anos terá {idade_acrescida} anos de idade.')