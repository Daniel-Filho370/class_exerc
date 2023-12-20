print('''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a 
média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO\n''')

nota1 = float(input('Digite a nota da primeira avaliação:'))
nota2 = float(input('Digite a nota da segunda avaliação:'))

media = (nota1 + nota2) / 2

print('\nTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO!')
elif media >= 7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')
