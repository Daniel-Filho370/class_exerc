import random
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.\n'
      'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
a1 = str(input('Digite o nome primeiro aluno:'))
a2 = str(input('Digite o nome do segundo aluno:'))
a3 = str(input('Digite o nome do terceiro aluno:'))
a4 = str(input('Digite o nome quarto aluno:'))
r = random.sample([a1, a2, a3, a4], k=4) #resultado
print(f'Os alunos {r} vão apresentar agora!')
