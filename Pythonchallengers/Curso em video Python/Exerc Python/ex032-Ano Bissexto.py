print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')

ano = int(input('Digite o ano: '))

if ano % 4 != 0 and ano % 100 != 0 and ano % 400 != 0:
    print('{} não é um ano bissexto.'.format(ano))
else:
    print('{} é um ano bissexto.'.format(ano))
