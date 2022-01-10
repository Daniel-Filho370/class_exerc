from math import sqrt, floor #escolhendo modulos do import math com o from
num = int(input('Digite um número: \n'))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')

import math #importa a biblioteca math toda
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
