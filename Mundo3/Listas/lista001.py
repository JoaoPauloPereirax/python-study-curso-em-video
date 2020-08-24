'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista=[]
for pos in range(0,5,1):
    lis=int(input('Digite um número: '))
    lista.insert(pos,lis)
maior=lista[0]
menor=lista[0]
for pos2 in range(0,5,1):
    if lista[pos2]>maior:
        maior=lista[pos2]
    if lista[pos2]<menor:
        menor=lista[pos2] 
print(f'\nO maior foi: {maior}\nO menor foi: {menor}\n')
for pos3 in range(0,5,1):
    print(f'Numero: {lista[pos3]} Posição: {pos3}')