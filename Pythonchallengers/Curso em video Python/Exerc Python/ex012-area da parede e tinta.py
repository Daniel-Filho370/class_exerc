print('11-Faça um programa que leia a largura e a altura de uma parede em metros. calcule a sua área e a quantidade '
      'de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2')
largura = float(input('Qual a largura da parede?\n'))
altura = float(input('Qual a altura da parede?\n'))
area = largura * altura
tinta = area / 2
print(f'sua parede tem a dimensão {largura:.0f}x{altura:.0f} totalizando área de:{area:.0f}m²')
print(f'Quantidade de latas de tinta necessárias:{tinta:.0f}')
