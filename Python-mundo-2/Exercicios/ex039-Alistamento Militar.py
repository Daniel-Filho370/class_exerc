from datetime import date

print(''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda 
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo.''')

nasc = int(input('Digite o ano em que você nasceu:'))
sexo = str(input('Digite "M" se seu sexo for masculino e "F" se for feminino:')).upper()

atual = date.today().year
idade = atual - nasc


if sexo == 'M':
    if idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Você tem {idade} anos de idade e deverá se alistar em {saldo} anos, faltam {saldo} ano(s) para o alistamento')

    elif idade == 18:
        print(f'Quem nasceu em {nasc} tem {idade} anos em {date.today().year} Vocë tem que se alistar IMEDIATAMENTE!.')

    else:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Você tem {idade} ano(s) de idade e já deveria ter se alistado há {saldo} ano(s).'
              f'\nSeu alistamento foi em  {ano}.')
elif sexo == 'F':
    print('Mulheres nao precisam fazer alistamento obrigatoriamente.')

else:
    print('Digite corretamente: "M" ou "F" para escolher.')
