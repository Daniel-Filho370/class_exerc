print('''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
para salário superiores a R$ 1.250,00 calcule um aumento de 10%
para os inferiores ou iguais, o aumento é de 15%
''')

salario = float(input('Digite o seu salário para aumento: '))

if salario > 1250.00:
    aumento = salario * 0.10
    salario += aumento
    print('Salário com aumento de 10%: R$', salario)
else:
    aumento = salario * 0.15
    salario += aumento
    print('Salário com aumento de 15%: R$', salario)
