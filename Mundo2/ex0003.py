'''
Escreva em um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é o maior!
-O segundo valor é o maior!
-Não existe valor maior, os dois são iguais!
===Etapas===
1. Pedir pera o usuário digitar dois números em duas etapas.

'''
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('\nDigite o segundo número: '))
if numero1>numero2:
    print('O primeiro valor é o maior!')
elif numero1<numero2:
    print('O segundo valor é o maior!')
else:
    print('Não existe valor maior, os dois são iguais!')