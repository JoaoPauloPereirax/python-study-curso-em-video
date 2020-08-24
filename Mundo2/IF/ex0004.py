'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar no serviço militar.
-Se é hora dele se alistar.
-Se já passou o tempo de alistamento.
OBS: Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
===Etapas===
1. Pedir o ano de nascimento do usuário
2. Verificar em qual condição ele se encontra.
3. Calcular o tempo que falta e mostrar na tela oo resultado.
'''
anoAtual = int(input('\nDigite o ano em que se encontra: '))
anoNascimento = int(input('\nDigite o ano de nascimento: '))
if (anoAtual-anoNascimento)<18:
    print('\nAinda vai se alistar no serviço militar, faltam {} anos para o alistamento'.format(18-(anoAtual-anoNascimento)))
elif (anoAtual-anoNascimento)>18:
    print('\nJá passou o tempo de alistamento no serviço militar, se passaram {} anos desde o alistamento'.format(anoAtual-anoNascimento-18))
else:
    print('\nÉ hora de se alistar.')