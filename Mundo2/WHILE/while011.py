'''Faça um programa que jogue par ou ímpar com o computador. O jogo será encerrado quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
computador=0
vitorias=0
while True:
    jogador=str(input('Par ou ímpar(P/I): ')).upper()
    if jogador==('I'):
        computador=randint(1,11)
        numero=int(input('Digite um número: '))
        if (numero+computador)%2==1:
            print('Você venceu!\nVocê {} x {} Computador'.format(numero,computador))
            vitorias+=1
        else:
            print('Você perdeu!\nVocê {} x {} Computador'.format(numero,computador))
            break
    elif jogador=='P':
        computador=randint(1,2)
        numero=int(input('Digite um número: '))
        if (numero+computador)%2==0:
            print('Você venceu!\nVocê {} x {} Computador'.format(numero,computador))
            vitorias+=1
        else:
            print('Você perdeu!\nVocê {} x {} Computador'.format(numero,computador))
            break
    else:
        print('Opção inválida!')
print('Total de vitórias consecutivas: {}'.format(vitorias))