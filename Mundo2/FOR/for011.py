'''Desenvolva um programa que o nome, idade e sexo de 4 pessoas. No final o programa mostre: 
    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    - Quantas mulheres têm menos de 20 anos.'''
somaIdades=0
maiorIdade=0
mulheresM20=0
for cont in range(0,4):
    nome=str(input('Digite o nome da pessoa: '))
    idade=int(input('Digite a idade desta pessoa: '))
    sexo=str(input('Digite o sexo desta pessoa(m/f): '))
    somaIdades+=idade
    if (sexo=='m' and idade>maiorIdade):
        homemVelho=nome
    if (sexo=='f' and idade<20):
        mulheresM20+=1
    
print('\nIdade Média das pessoas: {}'.format(somaIdades/4))
print('\nNome do homem mais velho: {}'.format(homemVelho))
print('Mulheres com menos de 20 anos: {}'.format(mulheresM20))
    