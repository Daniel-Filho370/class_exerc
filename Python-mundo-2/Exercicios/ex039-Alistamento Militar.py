from datetime import date

ano = int(input('Digite o ano em que você nasceu:'))

idade = date.today().year - ano

if idade < 18:
    print('Você tem {} anos de idade e tem que se alistar quando completar 18 anos'.format(idade))

elif idade == 18:
    print('Você tem {} anos de idade e está no periodo de alistamento.'.format(idade))

else:
    print('Você tem {} anos de idade e passou do tempo de se alistar'.format(idade))
