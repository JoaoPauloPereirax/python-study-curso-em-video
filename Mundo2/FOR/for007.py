'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
soma=0
numUsuario=int(input("Digite um número inteiro: "))
if numUsuario<0:
    for cont1 in range(numUsuario,-1):
        if numUsuario%cont1==0:
            soma+=cont1
    if soma==numUsuario:
        print('{} é primo!'.format(numUsuario))
    else:
        print('{} não é primo!'.format(numUsuario))    
elif numUsuario>0:
    for cont2 in range(2,numUsuario+1):
        if numUsuario%cont2==0:
            soma+=cont2
    if soma==numUsuario:
        print('{} é primo!'.format(numUsuario))
    else:
        print('{} não é primo!'.format(numUsuario))
else:
    print('{} não é primo!'.format(numUsuario))