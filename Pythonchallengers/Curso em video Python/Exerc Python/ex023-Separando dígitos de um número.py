print('====================== Desafio 023 ===============================')
print('''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex:
Digite um número:1834

Unidade:4
dezena:3
centena:8
milhar:1\n''')

number_str = str(input('Digite um número de 0 a 9999 :'))

print(f'''
Unidade:{number_str[3:4]}
dezena:{number_str[2:3]}
centena:{number_str[1:2]}
milhar:{number_str[0:1]} ''')

#Resolução da forma matematica do exercicio.
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''Analisando o número {num}
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}''')
