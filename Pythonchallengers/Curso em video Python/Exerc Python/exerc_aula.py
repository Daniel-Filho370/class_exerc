print('''
Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior.
a. Faça um programa que determine o salário atual desse funcionário.
b. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.''')
print('')

porc = 0.015
salario = int(input('Digite o salario inicial do funcionario: '))
ano = 1995

while ano < 2021:
    salario_final = salario + salario * porc
    ano += 1
    print('Ano: {} salario: {} porcentagem: {}'.format(ano, salario_final, porc))
    porc = porc * 2
