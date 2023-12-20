import random
import time

escolha = str(input('Digite se escolhe Pedra, Papel, Tesoura:')).upper()
'escolhe aleatoriamente'
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 11)
if escolha == 'PEDRA' or escolha == 'PAPEL' or escolha == 'TESOURA':
    # Condição para Pedra
    if escolha == 'PEDRA' and computador == 'PEDRA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Empate!'))

    elif escolha == 'PEDRA' and computador == 'PAPEL':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Derrota!'))

    elif escolha == 'PEDRA' and computador == 'TESOURA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Vitoria!'))

    # Condição para Papel
    if escolha == 'PAPEL' and computador == 'PEDRA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Vitoria!'))

    elif escolha == 'PAPEL' and computador == 'PAPEL':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Empate!'))

    elif escolha == 'PAPEL' and computador == 'TESOURA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Derrota!'))

    # Condição para Tesoura
    if escolha == 'TESOURA' and computador == 'PEDRA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Derrota!'))

    elif escolha == 'TESOURA' and computador == 'PAPEL':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Vitoria!'))

    elif escolha == 'TESOURA' and computador == 'TESOURA':
        escolha = escolha.capitalize()
        computador = computador.capitalize()
        print('Você: {} \nAdversario: {} \nResultado: {}'.format(escolha, computador, 'Empate!'))
else:
    print('Digite Pedra, Papel ou Tesoura corretamente.')
print('-=' * 11)
