from math import radians, sin, cos, tan
print('Faça um programa que leia um ângulo qualquer e mostre na tela o seno,cosseno e tangente desse ângulo.')
ang = float(input('Digite um ângulo:\n'))  # ângulo
se = sin(radians(ang))  # seno
co = cos(radians(ang))  # Cosseno
ta = tan(radians(ang))  # Tangente
print(f'Seno: {se:.2f}°\nCosseno: {co:.2f}°\nTangente: {ta:.2f}°')

