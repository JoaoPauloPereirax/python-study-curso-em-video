'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
    1. para binário
    2. para octal
    3. para hexadecimal
===Etapas===
1. Pedir para digitar um número e guardar o valor em uma variável.
2. Pedir para escolher a base para a conversão.
3. Aninnhamento das condições.

'''
numero=int(input('\nDigite um número inteiro:'))
base=int(input('Escolha a base para a conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
if (base == 1):
    print('Binário de {} é {}'.format(numero,bin(numero)))
elif (base == 2):
    print('Octal de {} é {}'.format(numero,oct(numero)))
elif (base == 3):
    print('Hexadecimal de {} é {}'.format(numero,hex(numero)))
    
else:
    print('Opção inválida')