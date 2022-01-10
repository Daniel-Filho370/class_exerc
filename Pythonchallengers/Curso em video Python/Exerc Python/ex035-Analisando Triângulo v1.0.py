print('''
1-Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triangulo\n''')


print('-=' * 15, '\nAnalisador de Triângulos\n', '-=' * 15)

segmentoA = float(input('Primeiro segmento:\n'))
segmentoB = float(input('Segundo segmento:\n'))
segmentoC = float(input('Terceiro segmento:\n'))

segmento_AB = segmentoA + segmentoB
segmento_BC = segmentoB + segmentoC
segmento_AC = segmentoA + segmentoC

if segmento_AB > segmentoC and segmento_BC > segmentoA and segmento_AC > segmentoB:
    print('Os segmentos acima PODEM FORMAR triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
