'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final mostre uma listagem de preços organizando os dados em forma tabular.'''
compras=('Caneta',1.99,'Caderno',20.00,'Mochila',60.00)
print('-'*40)
print(f'{"lista de compras":^40}')
print('-'*40)
for pos in range(0,len(compras)):
    if pos%2==0:
        print('\n{:.<30}'.format(compras[pos]),end=' ')
    else:
        print('R${:.2f}'.format(compras[pos]))
