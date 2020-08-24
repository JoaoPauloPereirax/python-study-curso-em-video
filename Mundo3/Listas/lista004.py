'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''
lista=[]
numeros=0
while True:
    num=int(input('\nDigite um número: '))
    lista.append(num)
    numeros+=1  
    while True:
        opcao=str(input('\nVoçê deseja continuar(S/N)?')).upper()
        if opcao=='S' or opcao=='N':
            break
    if opcao=='N':
        break
lista.sort(reverse=True)
print(f'\nForam digitados: {numeros} números\nLista ordenada de forma crescente: {lista}')
if 5 in lista:
    print('O número 5 está na lista!\n')
else:
    print('O número 5 não está na lista!\n')