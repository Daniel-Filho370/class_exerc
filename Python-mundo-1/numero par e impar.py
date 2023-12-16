num = input('Digite um número para saber se é par ou impar: ')

if num.isdecimal() == False:
    num = input('Valor invalido. Digite novamente:')

num = float(num) % 2

if num == 0:
    print('Par')
else:
    print('impar')
