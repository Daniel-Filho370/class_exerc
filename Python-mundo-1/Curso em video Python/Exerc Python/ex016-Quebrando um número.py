from math import trunc
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.')
num = float(input('Digite um número real qualquer:\n'))
inteiro = trunc(num)
print(f'O valor digitado foi {num} e a sua porção inteira é {inteiro}')
