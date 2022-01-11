print('''Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem que ele foi multado

A multa vai custar R$7,00 por cada Km acima do limite.''')

# ler a velocidade do carro
velocidade = float(input('Qual a velocidade do carro? '))
# multa por 7,00
multa = 7.00 * velocidade
# se ultrapassar 80km mostrar multa
if velocidade > 80.00:
    print('Você foi multado no valor de {} por ter ultrapassado '
          'o limite de velocidade, sua velocidade {}'.format(multa, velocidade))
