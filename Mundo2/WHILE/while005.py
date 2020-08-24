'''Desenvolva um programa que leia o primeiro termo  e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão usando a estrutura while.'''
primeiroTermo=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
n=0
while n!=10:
    print(primeiroTermo+n*razao)
    n+=1