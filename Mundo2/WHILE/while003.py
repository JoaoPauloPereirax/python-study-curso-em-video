'''Crie um programa que leia dois valores e mostre um menu na tela
[1] Somar

[2] Multiplicar

[3] Maior

[4] Novos números

[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
valor1=int(input('Digite o valor1: '))
valor2=int(input('Digite o valor2: '))
escolha=0
while escolha!=5:
    escolha=int(input('ESCOLHA A OPÇÃO DESEJADA\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair'))
    if escolha==1:
        print('\n{}+{}={}\n'.format(valor1,valor2,valor1+valor2))
    elif escolha==2:
        print('\n{}x{}={}\n'.format(valor1,valor2,valor1*valor2))
    elif escolha==3:
        if valor1==valor2:
            print('São iguais!')
        else:
            if valor1>valor2:
                print('Entre {} e {} o maior é {}'.format(valor1,valor2,valor1))
            else:
                print('Entre {} e {} o maior é {}'.format(valor1,valor2,valor2))
    elif escolha==4:
        valor1=int(input('Digite o valor1: '))
        valor2=int(input('Digite o valor2: '))
    elif escolha==5:
        print('Fim do programa!')
    else:
        print('Opção inválida!')
        