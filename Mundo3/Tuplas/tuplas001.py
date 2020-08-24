'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.'''
numeros=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        numeroEscolhido=int(input('\nDigite um número entre 0 e 20: '))
        if 0<=numeroEscolhido<=20:
            break
        else:
            print('Número inválido!')
    print(f'\nNúmero escolhido: {numeroEscolhido}\nNúmero em extenso: {numeros[numeroEscolhido]}')
    while True:
        continuar=str(input('\nDeseja continuar(S/N)? ')).upper()
        if continuar=='S' or continuar=='N':
            break
        else:
            print('\nOpção inválida!')
    if continuar=='N':
        break