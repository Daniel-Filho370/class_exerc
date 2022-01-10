import math
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,\n '
      'calcule e mostre o comprimento da hipotenusa.')
CO = float(input('Comprimento do cateto oposto:\n'))
CA = float(input('Comprimento do cateto adjacente:\n'))
HP = math.hypot(CO,CA) #Hipotenusa HP = (co ** 2 + ca ** 2) ** 0.5
print(f'A hipotenusa vai medir {HP:.2f}')
