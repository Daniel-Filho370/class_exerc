print('6-crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
numero = int(input('Digite um valor:'))
d = numero * 2
t = numero * 3
r = numero ** (1/2)
print(f'numero={numero}\ndobro={d}\ntriplo={t}\nraiz quadrada={r:.1f}')
