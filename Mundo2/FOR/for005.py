'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.'''
soma=0
for cont in range(1,7):
    numeroUsiario=int(input('Digite o num{}: '.format(cont)))
    if numeroUsiario%2==0:
        soma+=numeroUsiario
print('A soma de todos os números pares digitados é: {}'.format(soma))