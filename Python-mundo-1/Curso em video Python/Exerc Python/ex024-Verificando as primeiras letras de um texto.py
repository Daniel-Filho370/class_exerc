print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"')

# Como eu fiz
city = str(input('Digite o nome da cidade: ')).strip()

city = city.upper().split()
city1 = 'SANTO' in city[0]
print(city1)

# resposta do exercicio do curso em video 024

cid = str(input('Em que cidade você nasceu?'))
print(cid[:5].upper() == 'SANTO')

'''
# Resposta comentario do exercicio.(melhor maneira porque da falso em santori, santos e etc...)

c = input('Digite o nome da cidade: ').split()
print(c[0].upper() == 'SANTO')
'''
