'''Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.'''
peso=0
pesoMaior=0
pesoMenor=100000
for cont in range(0,5):
    peso=float(input('Digite o peso da pessoa {}: '.format(cont+1)))
    if peso>pesoMaior:
        pesoMaior=peso
    if peso<pesoMenor:
        pesoMenor=peso
        
print('\nPeso maior: {:.2f}\nPeso Menor: {:.2f}\n'.format(pesoMaior,pesoMenor))