from random import choice
print('''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.''')

# escolha de um numero entre 0 e 5 aleatório
n = choice([0, 1, 2, 3, 4, 5])
# usuário escolhendo um número
u = int(input('Tente adivinhar o número escolhido: '))
# condição se venceu ou perdeu e printar na tela
if n == u:
    print('Você acertou o número {} foi escolhido.'.format(n))
else:
    print('Você errou, o número escolhido foi {}'.format(n))
