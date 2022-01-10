print('-'*50)
fitas = int(input('Quantidade de fitas da locadora?'))
aluguel = int(input('Aluguel das fitas?'))

faturamentoanual = (fitas * 0.33) * (aluguel * 12)
multa = (aluguel * 0.10) * (fitas * 0.1)
fitas_final = (fitas * 0.2) + (fitas * 0.1)

print(f'Faturamento anual sabendo que 1 terço das fitas são alugadas.{faturamentoanual}')
print(f'multa de 10% no atraso de entrega por mês:{multa}')
print(f'Quantidade de fitas que a locadora terá no final do ano: {fitas_final}')
print('-'*50)
