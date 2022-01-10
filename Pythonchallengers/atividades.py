print('====================== Atividade 01 ===============================')
print('1 - faça um programa que leia um número inteiro e o imprima')
inteiro = int(input('Qual sua idade ?'))
print(f'\nSua idade é {inteiro}\n')

print('====================== Atividade 02 ===============================')
print('2 - faça um programa que leia um número real e o imprima')
real = float(input('Qual o seu peso?'))
print(f'\nSeu peso é {real}\n')

print('====================== Atividade 03 ===============================')
print('3 - Peça ao Usuário para digitar 3 valores inteiros e imprima a soma deles.')
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite um segundo valor:'))
n3 = int(input('Digite um terceiro valor:'))
print(f'\n{n1}+{n2}+{n3}={n1+n2+n3}\n')

print('====================== Atividade 04 ===============================')
print('4 - Leia um número real e imprima o resultado do quadrado desse número')
real1 = float(input('Digite um número real:'))
print(f'\nO resultado da raiz quadrada de {real1} é igual a {real1**2}\n')

print('====================== Atividade 05 ===============================')
print('5 - Leia um número real e imprima a raiz quadrada desse número')
real2 = float(input('Digite um número real:'))
print(f'\nA raiz quadrada é {real2**0.5:.2f}\n')

print('====================== Atividade 06 ===============================')
print('6 - Leia um número real e imprima a quinta parte deste número')
valor = float(input('Digite um número real:'))
print(f'\nA quinta parte de {valor} é {valor/5}')

print('====================== Atividade 07 ===============================')
print('7 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.'
      '\nA fórmula de conversão é F =  C * (9.0 / 5.0) + 32.0. F é Fahrenheit e C é Celsius.')
C = float(input('Quantos graus Celsius?\n'))
print(f'\n{C} grau celsius = {C*(9.0/5.0)+32.0} Fahrenheit')

print('====================== Atividade 08 ===============================')
print('8 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. '
      '\nA fórmula de conversão é C = 5.0 * (F - 32.0) / 9.0 F é  e C é Celsius.')
F = float(input('Quantos graus Fahrenheit?\n'))
print(f'\n{F} graus Fahrenheit = {5.0*(F - 32.0) / 9.0} Celsius\n')

print('====================== Atividade 09 ===============================')
print('9 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. '
      '\nA fórmula de conversão é C = K - 273.15, sendo C Celsius e K kelvin.')
kelvin = float(input('\nQuantos graus Kelvin?\n'))
print(f'{kelvin} kelvin = {kelvin - 273.15} Celsius')

print('====================== Atividade 10 ===============================')
print('10 -  Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.'
      '\nA fórmula de conversão é K = C + 273.15. Sendo C Celsius e K Kelvin.')
C1 = float(input('\nQuantos graus Celcius?\n'))
print(f'{C1} Celsius = {C1 + 273.15}')

print('====================== Atividade 11 ===============================')
print('11 - Leia uma velocidade em Km/h (Kilometro por hora) e apresente-a convertida em m/s (metro por segundo). '
      '\nA formula de conversão é m = k/3.6, sendo k a velocidade em km/h e m a velocidade em m/s.')
kilometro = int(input('\nQuantos km/h?\n'))
print(f'{kilometro}km/h = {kilometro/3.6} m/s')
