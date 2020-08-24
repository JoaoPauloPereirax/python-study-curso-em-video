'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo='a'
while (sexo.upper()!='M' or sexo.upper()!='F'):
    sexo=str(input('Digite seu sexo(m/f): '))
print('Fim do programa')