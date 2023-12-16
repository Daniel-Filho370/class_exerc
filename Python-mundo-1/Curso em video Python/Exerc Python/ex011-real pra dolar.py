print('10-Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode '
      'comprar.')
carteira = int(input('Quanto você tem na carteira ?R$'))
dolar = carteira / 5.37
print(f'Com R$ {carteira} você pode comprar US${dolar:.2f}')
