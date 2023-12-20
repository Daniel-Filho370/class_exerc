import random
import time

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada?'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:  # Computador jogou Pedra
    if jogador == 0:  # Jogador jogou Pedra
        print('EMPATE!')
    elif jogador == 1:  # Jogador jogou Papel
        print('JOGADOR VENCE!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:  # Computador jogou Papel
    if jogador == 0:  # Jogador jogou Pedra
        print('COMPUTADOR VENCE!')
    elif jogador == 1:  # Jogador jogou Papel
        print('EMPATE!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0:  # Jogador jogou Pedra
        print('JOGADOR VENCE!')
    elif jogador == 1:  # Jogador jogou Papel
        print('COMPUTADOR VENCE!')
    elif jogador == 2:  # Jogador jogou Tesoura
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
