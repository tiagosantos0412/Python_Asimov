print('Merenda!')
nome = input('Digite o seu nome:   ')
fome = input('Está com fome?   ')
dispensa = input('Tem comida em casa?   ')

def verificar(value):
    if value == 'sim' or value == 'Sim':
        value = True
    elif value == 'não' or 'Não':
        value = False
    return value

fome = verificar(fome)
dispensa = verificar(dispensa)


if fome == True:
    if dispensa == True:
        print('Preparando uma refeição!')
        print('Comendo...')
    else:
        print('Ir até o super mercado')
        print('Preparando uma refeição!')
        print('Comendo...')
else:
    print(f'{nome}, você está sem fome no momento, prepare a refeição mais tarde!')

print('Fim do programa...')    