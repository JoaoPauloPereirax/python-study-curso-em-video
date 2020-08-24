'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma=0
for cont in range(0,500):
    if(cont%3==0 and cont%2!=0):
        print(cont)
        soma+=cont
print('A soma é: {}'.format(soma))