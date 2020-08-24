'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
sleep(1)
for contagemRegressiva in range(10,0,-1):
    print(contagemRegressiva)
    sleep(1)
print('Bummmmmmmmmm')
