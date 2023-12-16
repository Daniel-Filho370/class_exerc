print('''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 
R$0,45 para viagens mais longas.''')

#Pergunta a distancia da viagem em Km
viagem = int(input('Qual a distância da viagem? '))

if viagem <= 200:
    passagem = 0.50 * viagem
    print('Valor da Viagem: R${}'.format(passagem))

else:
    passagem = 0.45 * viagem
    print('Valor da viagem: R${}'.format(passagem))
