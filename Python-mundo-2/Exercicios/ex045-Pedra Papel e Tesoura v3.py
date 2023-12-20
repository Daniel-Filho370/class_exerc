import random
import time
print("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n0 = PEDRA\n1 = PAPEL\n2 = TESOURA\nAgora, digite sua escolha: "))
itens = ('Pedra', 'Papel', 'Tesoura')
b = random.randint(0, 2)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-='*11)
print('Computador jogou {}'.format(itens[b]))
print('Jogador jogou {}'.format(itens[a]))
print('-='*11)
if a == b:
    print("EMPATE!")
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    print("VOCÊ PERDEU!")
else:
    print("VOCÊ GANHOU!")
