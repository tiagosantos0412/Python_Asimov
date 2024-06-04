# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

usuario_bd = 'tiago0412'
senha_bd = 'minh@Senha2024'
usuario = ''
senha = ''
msg_usuario_nao_encontrado = 'Erro de login! Usuário não cadastrado.'
msg_senha_invalida = 'Erro de login! Senha inválida.'

print('-' * 60)
print('-               Autenticação de Usuário                    - ')
print('-' * 60)
usuario = input('Digite o seu login.....: ')
senha = input('Digite a sua senha.......: ')

if usuario == usuario_bd and senha == senha_bd:
    msg_sucesso = f'Bem vindo {usuario}.'
    print(msg_sucesso)
elif usuario != usuario_bd:
    print(msg_usuario_nao_encontrado)
elif senha != senha_bd:
    print(msg_senha_invalida)

print('-' * 60)
print('-               Fim do programa                             -')
print('-' * 60)