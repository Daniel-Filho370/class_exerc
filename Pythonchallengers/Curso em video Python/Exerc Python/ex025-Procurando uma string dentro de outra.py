print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.')

# 1) Recebo o nome tratado para evitar espaços extras
name = str(input('Qual o seu nome completo? ')).strip()

# 2) Converto o nome para letras maiúsculas, depois
# o divido e guardo a lista em uma nova variável:
divisao = name.upper().split()
# 3) Agora executo o teste para verificar se existe SILVA em
# alguns dos itens da lista criada.
verification = 'SILVA' in divisao

print(f'Seu nome tem Silva? {verification}')
