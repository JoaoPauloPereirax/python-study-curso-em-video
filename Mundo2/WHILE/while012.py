'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
a) Quantas pessoas têm mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres têm menos de 20 anos.'''
maiores=0
homens=0
mulheres20=0
while True:
    while True:
        idade=int(input('Digite a idade: '))
        if idade>0:
            break
    if idade>18:
        maiores+=1
    while True:
        sexo=str(input('Sexo: ')).upper()
        if sexo=='M' or sexo=='F':
            break
        print('Opção inválida!')
    if sexo=='M':
        homens+=1
    if sexo=='F' and idade<20:
        mulheres20+=1
    while True:
        continuar=str(input('Deseja continuar(S/N)?')).upper()
        if continuar=='S' or continuar=='N':
            break
        print('Opção inválida!')
    if continuar=='N':
        break
print('Maiores de 18 anos: {}\nHomens: {}\nMulheres menores de 20 anos: {}'.format(maiores,homens,mulheres20))