print('-'*50)
print('2-Uma certa firma de encanamento paga R$ 20,00 reais por dia trabalhado. Escreva um algoritmo que calcule o\n'
      'salário líquido de um encanador dessa firma, sabendo-se a quantidade de dias que ele trabalhou. Obs.: O\n'
      'salário líquido corresponde ao salário normal, descontados 8% de impostos.\n')
dias = int(input('Quantos dias o encanador trabalhou?'))
salarioliquido = (20 * dias) - 0.8
print(f'O encanador recebe {salarioliquido}')
print('-'*50)
