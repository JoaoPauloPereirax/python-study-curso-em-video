'''Faça um programa que faça o computador jogar jokenpô com você.'''
from random import randint
escolhaComputador = randint(1,3)
print('\n 1 - Pedra \n 2 - Papel\n 3 - Tesoura')
escolhaJokempo = int(input('Escolha uma das opções: '))
if escolhaJokempo==1:
    escolhaJokempo='Pedra'
elif escolhaJokempo==2:
    escolhaJokempo='Papel'
elif escolhaJokempo==3:
    escolhaJokempo='Tesoura'
############################
if escolhaComputador==1:
    escolhaComputador='Pedra'
elif escolhaComputador==2:
    escolhaComputador='Papel'
elif escolhaComputador==3:
    escolhaComputador='Tesoura'
################################
if escolhaComputador==escolhaJokempo:
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===EMPATE==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Pedra' and escolhaJokempo=='Papel':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ VENCEU==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Papel' and escolhaJokempo=='Tesoura':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ VENCEU==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Tesoura' and escolhaJokempo=='Pedra':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ VENCEU==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Papel' and escolhaJokempo=='Pedra':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ PERDEU==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Tesoura' and escolhaJokempo=='Papel':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ PERDEU==='.format(escolhaJokempo,escolhaComputador))
elif escolhaComputador=='Pedra' and escolhaJokempo=='Tesoura':
    print('\nVocê escolheu: {}\nO CPU escolheu: {}\n===VOCÊ PERDEU==='.format(escolhaJokempo,escolhaComputador))