'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas'''
lista=[]
pares=[]
impares=[]
while True:
    num=int(input('\nDigite um número: '))
    if num in lista:
        pass #não faz nada, pode ser usado quando a sintaxe exige um comando       
    else:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    lista.append(num)
    while True:
        opcao=str(input('\nDeseja continuar(S/N)? ')).upper()
        if opcao=='S' or opcao=='N':
            break
    if opcao=='N':
        break
print(f'\nLista: {lista}\nPares: {pares}\nImpares: {impares}\n\n')