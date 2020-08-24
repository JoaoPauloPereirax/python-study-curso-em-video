'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso , mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint

while True:
    tuplaAleatoria=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    print(tuplaAleatoria)
    #Menor
    menor=11
    maior=-1
    for cont1 in tuplaAleatoria:
        if cont1<menor:
            menor=cont1
    for cont2 in tuplaAleatoria:
        if cont2>maior:
            maior=cont2
    print('\nMenor: {}\nMaior: {}'.format(menor,maior))
    while True:
        continuar=str(input('\nDeseja continuar(S/N)? ')).upper()
        if continuar=='S' or continuar=='N':
            break
        else:
            print('Opção inválida!')
    if continuar=='N':
        break
