print('-'*35)
print('Curso Python #09 - Manipulando Texto')
print('-'*35)
print('\nFatiamento de String:\n')
print('No python uma frase é fatiada cada letra em um espaço na memória começando do 0 e contando com espaços, '
      'na frase "Curso em Video Python"\npor exemplo existe 21 letras na memória  \n')

frase = str('Curso em Video Python')  # Código
print('Exemplos:\n')
print('frase[9]         1º Escolhe a letra que está no espaço 9')
print('frase[9:21]      2º Começa pela nona letra e termina na 20')
print('frase[9:21:2]    3º Começa pela nona letra e vai pulando de 2 em 2 até a vigésima letra')
print('frase[:5]        4º Começa do caractere 0 quando não coloca onde vai começar')
print('frase[15:]       5º Começa da decima quinta letra e vai até o final quando não especifica o final')
print('frase[9::3]      6º Começa pela nona e vai até o final pulando de 3 em 3')
print('-'*100)

print('Análise de String:\n')

print('1-leng(frase):\nlenght que significa comprimento, portanto, Mostra o comprimento da frase.')
print('\nExemplo:\n')
print('print(len(frase))')
print(f'Comprimento da String "{frase}": {len(frase)}')


print('\n2-variável.count("letra contada").count Conta quantas vezes o que for especificado aparece na string\n')
print('Exemplo:\n')
print('print(frase.count("o"))')
print(f'Quantidades de "o" na string "{frase}": {frase.count("o")}\n')
print('frase.count("o",0,13)   1º Conta quantas letras "o" tem do 0 até o 13\n')


print('\n3-variável.find("especifica uma palavra") 1º Encontra "o que foi especificado" na string e mostra onde começa')
print('frase.find("Android") 2º Quando coloca uma string que não existe ele retorna -1 que significado que não foi '
      'encontrado\n')

print('\n"4-Curso" in frase 1º o "in" diz se é True  ou False\n')
print('\nExemplo:\n')
print('print(f"A palavra curso está na string {frase}? {"Curso" in frase})"\n')
print(f'A palavra curso está na string {frase}? {"Curso" in frase}')

print('-'*100)

print('Transformação de string:\n')

print('frase.replace("Python","Android") 1º Pega o Python da variável frase e troca por Android\n')

print('frase.upper() #O método upper coloca toda a string em Maisculo')
print('frase.lower() #O método lower coloca toda a string em Minuscula')
print('frase.capitalize() #O método capitalize coloca toda a string em Minuscula e apenas a primeira letra da frase '
      'fica Maisculo')
print('frase.title() O método title analisa quantas palavras tem a string e faz o capitalize palavra por palavra\n')

frase1 = '   Aprenda python  '
print(f'Nova variável de Exemplo:\n {frase1}\n')

print('frase.strip() remove todos os espaços inuteis no inicio e final da string')
print('print(f"Exemplo:{frase1.strip()}")')
print(f'Exemplo:{frase1.strip()}\n')
print('frase.rstrip() e frase.ltrip() colocando o "r" e o "l" para remover os espaços inuteis apenas na direita ou '
      'esquerda')

print('-'*100)

print('\nDivisão de String:\n')

print('frase.split() #Divide a String onde estiver espaços\n')
print(frase.split())

print('\n.join() ')
print('Exemplo:')
print("'-'.join(frase) #Se tiver nomes separados em listas pode-se utilizar o join para juntar tudo com algo ou nada")
print('Exemplo:')
print("'-'.join(frase)")
print('-'.join(frase))