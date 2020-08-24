'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas pessoas não atingiram a maioridade e quantas já são maiores.'''
maiores=0
menores=0
for cont in range(0,7):
    idade=int(input('Digite a idade da pessoa {}:  '.format(cont+1)))
    if idade>=18:
        maiores+=1
    else:
        menores+=1
print('Maiores: {}\nMenores: {}'.format(maiores,menores))