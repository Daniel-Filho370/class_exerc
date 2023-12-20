print('''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.''')

num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.''')
conversao = int(input('Sua opção:'))

if conversao == 1:
    n = bin(num)
    print('{} convertido para BINÁRIO é igual a {}'.format(num, n[2:]))
elif conversao == 2:
    n = oct(num)
    print('{} convertido para OCTAL é igual a {}'.format(num, n[2:]))
elif conversao == 3:
    n = hex(num)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, n[2:]))
else:
    print('Opção invalida. Tente novamente.')
