'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''
quantidade=0
opcao='y'
soma=0
maior=-1000000000000000000
menor=10000000000000000
while opcao!=('N'):
    numero=int(input('Digite um número inteiro: '))
    quantidade+=1
    soma+=numero
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    opcao=str(input('Deseja continuar(S/N)?')).upper()
print('\nMédia: {}\nMaior: {}\nMenor: {}\n'.format(soma/quantidade,maior,menor))