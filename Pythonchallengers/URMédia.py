print('''Cálculo de Média Desenvolva um código que peça ao usuário o número (N) de dados
que ele quer entrar para calcular a média. Depois vai pedir N vezes para ele inserir um número que
será somado aos outros e usado para calcular a média final. ''')


qtd = int(input('Quantidade de números que deseja calcular: '))
i = 0
somaM = 0
while i < qtd:
    num = float(input('Digite o número:'))
    somaM += num
    i += 1
mediaNotas = somaM / qtd
print('Média das idades é: ', mediaNotas)
