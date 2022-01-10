print('-'*50)

valor_original = int(input('Qual o debito original:'))
atraso = int(input('Dias de atraso além dos 30 dias, se não houver atraso digite 0:'))
parcelas = int(input('Parcelas para o pagamento:(Se não for parcelas digite 1)'))

# Multa de 10% independente do tempo
multa = valor_original * 0.10
# Valor do juros
jurospordia = valor_original * (0.0033 * atraso)
# Valor do pagamento + parcelas + juros + multa
valor_pagar = valor_original + jurospordia + multa / parcelas
# Valor original com as parcelas
debitoparcelado = valor_original // parcelas

if atraso > 0:
    print(f'Como houve atraso de {atraso} dias, o valor a ser pago é de {valor_pagar:.2f} reais em {parcelas} parcelas')

else:
    print(f'Como o pagamento foi feito em dia o valor a ser pago é de:{debitoparcelado} reais')

print('-'*50)
