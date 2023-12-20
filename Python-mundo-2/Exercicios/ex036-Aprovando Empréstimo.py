print('''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado.
''')

valor_casa = float(input('Valor da casa:\n'))
salario = float(input('Salário do comprador:\n'))
anos = int(input('Quantos anos de financiamento:\n'))

parcelas = anos * 12
prestaçao = valor_casa / parcelas
minimo = salario * 0.30

if prestaçao > minimo:
    print(f'Para pagar uma casa de {valor_casa} em {anos} anos a prestação será de R$ {prestaçao:.2f}')
    print('Emprestimo negado por exceder o valor de 30% do seu salário.')

else:
    print(f'Para pagar uma casa de R$ {valor_casa} em {anos} anos a prestação será de {prestaçao:.2f}')
    print('Parabéns, emprestimo aprovado!')
