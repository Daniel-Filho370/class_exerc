from datetime import date

print('''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
 sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER\n''')

ano = int(input('Digite o ano de nascimento:'))

idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM!')
elif idade <= 14:
    print('Classificação: INFANTIL!')
elif idade <= 19:
    print('Classificação: JUNIOR!')
elif idade <= 25:
    print('Classificação: SÊNIOR!')
else:
    print('Classificação: MASTER!')