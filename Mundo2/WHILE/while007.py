'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros termos de uma sequência de fibonacci.'''
n=int(input('Digite um número: '))
anterior=1
atual = 0
cont=1
while cont!=n:
    print(atual)
    atual+=anterior
    anterior=atual-anterior
    cont+=1
print(atual)