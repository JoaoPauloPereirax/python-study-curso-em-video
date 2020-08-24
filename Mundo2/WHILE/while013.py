'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra. 
b) Quantos produtos custam mais de R$ 1000,00.
c) Qual é o nome do produto mais barato.'''
print(10*'='+'Lojão do João'+10*'=')
total=0
produto1000=0
produtoBarato='Sem nome'
pprodutoBarato=100000000000000000
while True:
    produto=str(input('Digite o nome do produto: '))
    while True:
        preco=float(input('Digite o preço do produto: '))
        if preco>0:
            break
        print('Preço inválido!')
    total+=preco
    if preco>1000:
        produto1000+=1
    if pprodutoBarato>preco:
        pprodutoBarato=preco
        produtoBarato=produto
    while True:
        continuar=str(input('Deseja continuar(S/N)? ')).upper()
        if continuar=='S' or continuar=='N':
            break
    if continuar=='N':
        break
print('\nTotal da compra: R${:.2f}\nQuantidade de produtos que custam mais que R$1000: {}\nProduto mais barato: {} custa R${:.2f}'.format(total,produto1000,produtoBarato,pprodutoBarato))
print('Fim do programa!')