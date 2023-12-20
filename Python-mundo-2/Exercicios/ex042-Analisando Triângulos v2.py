print('-=' * 15, '\nAnalisador de Triângulos\n', '-=' * 15)

A = float(input('Primeiro segmento:\n'))
B = float(input('Segundo segmento:\n'))
C = float(input('Terceiro segmento:\n'))

AB = A + B
BC = B + C
AC = A + C

if AB > C and BC > A and AC > B:
    print('Os segmentos acima PODEM FORMAR triângulo!', end=' ')
    if AB == BC == AC:
        print('Este é um triangulo equilátero.')
    elif AB == BC != AC:
        print('Este é um triangulo isósceles.')
    elif AB != BC != AC:
        print('Este é um triangulo escaleno.')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
