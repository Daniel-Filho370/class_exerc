print('-'*50)
Qmesa = int(input('Digite quantos pessoas estão a mesa:'))
Qchopps = int(input('Digite quantidade de chopps pedidos:'))
Qpizza = int(input('Digite quantidade de pizzas pedidas:'))
Qcobertura = int(input('Digite quantidade de coberturas pedidas:'))

# Valor cobrado dos chopps pedidas
Vchopps = 0.80 * Qchopps
# Valor cobrado das pizzas pedidas
Vpizza = 10 * Qpizza
# Valor cobrado das coberturas pedidas
Vcobertura = 1.50 * Qcobertura
# 10% do garçom
garcom = (Vchopps + Vpizza + Vcobertura) * 0.10
# Conta inteira
Conta = Vchopps + Vpizza + Vcobertura + garcom
# Conta divididade pela mesa
DConta = (Vchopps + Vpizza + Vcobertura + garcom) / Qmesa


print(f'SEGUE ABAIXO A CONTA: \nConta inteira:{Conta:.2f} \nConta:{DConta:.2f} para ser dividido em {Qmesa} pessoas. '
f'\nFATURA: \nChopps:{Vchopps:.2f} R$ \nPizza:{Vpizza:.2f} R$ \nCobertura:{Vcobertura:.2f} R$ \n10% do garçom:{garcom:.2f} R$')
print('-'*50)
