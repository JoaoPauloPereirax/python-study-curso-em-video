'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
cont=0
lista=[]
while True:
    num=int(input('\nDigite um número: '))
    if num in lista:
        print(f'\nO numero {num} já está na lista, não será adicionado novamente!')
    else:
        lista.insert(cont,num)
        cont+=1
        print(f'\nO número {num} foi adicionado a lista')
    while True:
        continua=str(input('\nDeseja continuar(S/N)? ').upper())
        if continua=='S' or continua=='N':
            break
    if continua=='N':
        break
lista.sort()#ele faz a alteração na lista original  
print(lista)