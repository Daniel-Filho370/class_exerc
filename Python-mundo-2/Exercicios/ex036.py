print('''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado.
''')

valor_casa = float(input('Valor da casa:\n'))
salario_comprador = float(input('Salário do comprador:\n'))
anos_pagando = int(input('Quantos anos de financiamento:\n'))

quantidade_parcelas = anos_pagando * 12
prestaçao_mensal = valor_casa / quantidade_parcelas
minimo = salario_comprador * 0.30

if prestaçao_mensal > minimo:
    print(f'Para pagar uma casa de {valor_casa} em {anos_pagando} anos a prestação será de R$ {prestaçao_mensal:.2f}')
    print('Emprestimo negado por exceder o valor de 30% do seu salário.')

else:
    print(f'Para pagar uma casa de R$ {valor_casa} em {anos_pagando} anos a prestação será de {prestaçao_mensal:.2f}')
    print('Parabéns, emprestimo aprovado!')
