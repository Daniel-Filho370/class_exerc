print('Faça um programa que leia o nome completo de uma pessoa,'
      ' mostrando em seguida o primeiro e o último nome separadamente.')

nome = str(input('Insira seu nome completo:'))
nomesplit = nome.split()
print(f'''Nome completo:',{nome})
Primeiro:'{nomesplit[0]}
último:'{nomesplit[-1]}''')

'''
# Forma resolvida na atividade do curso em video
n = str(input('Insira seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
'''
