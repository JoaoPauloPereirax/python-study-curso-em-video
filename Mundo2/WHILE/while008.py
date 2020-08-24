'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag(999))'''
numero=int(input('Digite um número(999 para sair): '))
soma=0
quantidade=0
while numero!=999:
    soma+=numero
    quantidade+=1
    numero=int(input('Digite um número(999 para sair): '))
print('\nQuantidade de números: {}\nA soma entre eles: {}'.format(quantidade,soma))