print('====================== Desafio 022 ===============================')
print('''Crie um programa que leia o nome completo de uma pessoa e mostre:\n
01-O nome com todas as letras maiúsculas.
02-O nome com todas as letras minúsculas
03-Quantas letras ao todo (sem considerar espaços)
04-Quantas letras tem o primeiro nome.''')

name = str(input('Digite seu nome completo: '))

print(f'''Analisando seu nome...
Seu nome em maiúsculo é {name.upper()}
Seu nome em minúsculo é {name.lower()}''')

lista = name.strip().split()
name2 = ''.join(lista)

print(f'Seu nome "{name}" tem {name2.__len__()} letras (sem considerar espaços)')

print(f'Seu primeiro nome é {lista[0]} e ele tem: {lista[0].__len__()} letras')
