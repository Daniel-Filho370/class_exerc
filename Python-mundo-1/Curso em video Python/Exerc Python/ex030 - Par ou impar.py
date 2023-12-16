print('Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.')

n = int(input('Digite um número inteiro: '))

par = n % 2

if par == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')
