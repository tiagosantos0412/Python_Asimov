print('Convertendo de texto para inteiro:')
numero_texto = '10'
print(numero_texto, type(numero_texto))
numero_inteiro = int(numero_texto)
print(int(numero_inteiro), type(numero_inteiro))

print()

print('Convertendo de inteiro para texto:')
numero_inteiro = 20
print(numero_inteiro, type(numero_inteiro))
numero_texto = str(numero_inteiro)
print(numero_texto, type(numero_texto))

print()

print('Concatenando dois textos:')
texto_1 = 'Meu nome é '
texto_2 = 'Tiago Felipe'
print(texto_1 + texto_2)

print('\nRetornando o tamanho da string: ', len(texto_2))
