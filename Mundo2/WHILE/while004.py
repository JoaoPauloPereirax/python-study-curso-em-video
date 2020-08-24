'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1=120'''
escolha=int(input('Digite um número: '))
fatorial=escolha
fat=1
while fatorial!=1:
    fat=fat*fatorial
    fatorial-=1
print('{}!={}'.format(escolha,fat))