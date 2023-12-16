print('')

n = int(input('Digite o número inteiro a ser convertido:'))
conversao = int(input('Digite 1 para binario, 2 para octal e 3 para hexadeximal:'))

if conversao == 1:
    n = bin(n)
    print(n[2:])
elif conversao == 2:
    n = oct(n)
    print(n[2:])
elif conversao == 3:
    n = hex(n)
    print(n[2:])
else:
    print('Digite 1 para binario, 2 para octal e 3 para hexadeximal.')
