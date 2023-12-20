print('''1-Elabore um programa que calcule o valor a ser pago por um produto, consegirando o seu preço normal e
 condicação de pagamento:
1-Á vista em dinheiro/cheque:10% de desconto
2-Á vista no cartão:5% de desconto
3-Em até 2x no cartão:preço normal
4-3x ou mais no cartão:20% de juros\n''')


preço = float(input("Digite o preço das compras: R$"))
condiçao = int(input("Digite a condição de pagamento:"))


if condiçao == 1:
    valor_desconto = preço * 0.9
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preço, valor_desconto))
elif condiçao == 2:
    valor_desconto = preço * 0.95
    print('Sua compra de R${} vai custar R${:.2f} no final.'.format(preço, valor_desconto))
elif condiçao == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcela, preço))
elif condiçao == 4:
    valor_juros = preço * 1.20
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = valor_juros / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, valor_parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor_juros))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
