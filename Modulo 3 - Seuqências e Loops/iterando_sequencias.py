numeros = [5, 2, 36, -74, 85, -42]
nomes = ['Tiago', 'Marcio', 'Caroline', 'Rubia']

for i in numeros:
    print(f'O índice está no número {i}')

for i in nomes:
    print(f'O indice está no nome {i}')

clientes = [
    (1, 'Tiago', '25412365884', 'tiago@gmail.com'),
    (2, 'Danilo', '12545874563', 'danilo@gmail.com'),
    (3, 'Roberta', '56325478996', 'roberta@gmail.com'),
    (4, 'Miriam', '45236547745', 'miriam@gmail.com')
]

# for cliente in clientes:
#     id = cliente[0]
#     nome = cliente[1]
#     cpf = cliente[2]
#     email = cliente[3]
#     print(f'Cliente: {id}\nNome: {nome}\nCPF: {cpf}\nE-mail: {email}\n')

for cliente in clientes:
    id, nome, cpf, email = cliente
    print(f'Cliente: {id}\nNome: {nome}\nCPF: {cpf}\nE-mail: {email}\n')