'''Desenvolva um programa que leia o primeiro termo  e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.'''
primeiroTermo=int(input('Digite o primeiro termo da PA: '))
razaoPA=int(input('Digite a razão da PA: '))
print('Dez primeiros termos:\n')
for cont in range(0,10):
    print(primeiroTermo+razaoPA*cont)