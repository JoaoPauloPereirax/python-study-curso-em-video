'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes aparece o valor 9.

b) Em que posição foi digitado o primeiro valor 3.

c) Quais foram os números pares.'''
num=(int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(num)
print('\nO número 9 aparece {} vezes'.format(num.count(9)))
if num.count(3)>0:
    print('\nO número 3 aparece na posição {}.'.format(num.index(3)+1))
else:
    print('\nO número 3 não aparece na tupla.')
print('\nos números pares são: ',end=' ')
for cont in num:
    if cont%2==0:
        print(cont, end=' ')