'''Faça um programa onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador=randint(0,10)
palpite=int(input('Digite um novo palpite(entre 0 e 10): '))
tentantivas=1
while palpite!=computador:
    palpite=int(input('Digite um novo palpite(entre 0 e 10): '))
    tentantivas+=1
print('Você acertou!\nTentativas: {}\nNumero: {}'.format(tentantivas,palpite))