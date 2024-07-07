contador  = 0

# while contador <= 10:
#     print(f'Estamos no passo {contador}.')
#     contador += 1

# print('O loop acabou!')

# while contador <= 10:
#     print(f'Estamos no passo {contador}.')
#     contador += 1
#     if contador == 5:
#         break

# print('O loop acabou!\n\n\n')

# for n in range(-5, 6):
#     print(n)
#     if n == 0:
#         continue
#     resultado = 1 / n
#     print(f'O resultado é {resultado}.')

while True:
    try:
        opt = int(input('1 para Cadastro \n2 para Consulta \n3 para Sair\nEscolha uma opção: '))
        if opt == 1:
            print('Sessão de cadastro')
            # Adicione aqui o código para a sessão de cadastro
        elif opt == 2:
            print('Sessão de consulta')
            # Adicione aqui o código para a sessão de consulta
        elif opt == 3:
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida!')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número.')
print('Fim')

