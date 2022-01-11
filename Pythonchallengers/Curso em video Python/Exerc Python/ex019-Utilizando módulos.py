from random import choice
print('Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,\n'
      'lendo o nome deles e escrevendo o nome do escolhido.')
a1 = str(input('nome do primeiro aluno:')) #nome do 1° aluno
a2 = str(input('nome do segundo aluno:')) #nome do 2° aluno
a3 = str(input('nome do terceiro aluno:')) #nome do 3° aluno
a4 = str(input('nome do quarto aluno:')) #nome do 4° aluno
lista = choice([a1,a2,a3,a4])
print(f'O escolhido foi {lista} a apagar o quadro.')
