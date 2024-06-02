# and (e), or (ou) e not (não)

# verdadeiro = True
# falso = False

# print('verdadeiro and verdadeiro = ',verdadeiro and verdadeiro)
# print('verdadeiro and falso = ',verdadeiro and falso)
# print('verdadeiro and falso = ',falso and falso)
# print('verdadeiro or verdadeiro = ',verdadeiro or verdadeiro)
# print('verdadeiro or falso = ',verdadeiro or falso)
# print('verdadeiro or falso = ',falso or falso)
# print('not verdadeiro = ', not verdadeiro)
# print('not falso = ', not falso)


print('Merenda 2.0!')
nome = input('Digite o seu nome:   ')
fome = input('Está com fome?   ')
dispensa = input('Tem comida em casa?   ')

def verificar(value):
    if value.lower() == 'sim':
        return True
    elif value.lower() == 'não':
        return False
    return None  # Caso a entrada seja diferente de 'sim' ou 'não'

fome = verificar(fome)
dispensa = verificar(dispensa)

if fome is None or dispensa is None:
    print('Respostas inválidas. Por favor, responda apenas "sim" ou "não".')
elif fome and dispensa:
    print('Preparando uma refeição!')
    print('Comendo...')
elif fome and not dispensa:
    print('Ir até o super mercado')
    print('Preparando uma refeição!')
    print('Comendo...')
elif not fome:
    print(f'{nome}, você está sem fome no momento, prepare a refeição mais tarde!')

print('Fim do programa...')
   
