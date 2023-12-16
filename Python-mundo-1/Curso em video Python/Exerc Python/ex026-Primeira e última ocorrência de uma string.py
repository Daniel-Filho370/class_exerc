print('''Faça um programa que leia uma frase pelo teclado e mostre:
 1-QUANTAS VEZES APARECE A LETRA "A"
 2-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
 3-EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ''')

frase = input('Digite um frase qualquer: ').upper()

frase1 = frase.split()
frasejunta = ''.join(frase1)

conta_a = frasejunta.count('A')
start = frasejunta.find('A')
final = frasejunta.rfind('A')


print(f'''
Olá {frase}:
1- A letra "A" aparece {conta_a} vezes no seu nome.
2-A letra "A" aparece a primeira vez na letra de indice: {start+1}
3-A letra "A" aparece a ultima vez na letra de indice(Retirando espaços): {final+1}''')
