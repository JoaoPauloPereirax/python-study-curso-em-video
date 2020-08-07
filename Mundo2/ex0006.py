'''
A CBX(Confederação Brasileira de Xadrez) precida de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 6 anos: Sub 6
- Até 8 anos: Sub 8
- Até 10 anos: Sub 10
- Até 12 anos: Sub 12
- Até 14 anos: Sub 14
- Até 16 anos: Sub 16
- Até 18 anos: Sub 18
- Acima de 18 anos: Absoluto
'''
anoAtual = 2020
anoNascimento = int(input('\nDigite o ano de nascimento do atleta: '))
if (anoAtual-anoNascimento)<=6:
    print('Categoria: Sub 6')
elif 6<(anoAtual-anoNascimento)<=8:
    print('Categoria: Sub 8')
elif 8<(anoAtual-anoNascimento)<=10:
    print('Categoria: Sub 10')
elif 10<(anoAtual-anoNascimento)<=12:
    print('Categoria: Sub 12')
elif 12<(anoAtual-anoNascimento)<=14:
    print('Categoria: Sub 14')
elif 14<(anoAtual-anoNascimento)<=16:
    print('Categoria: Sub 16')
elif 16<(anoAtual-anoNascimento)<=18:
    print('Categoria: Sub 18')
elif (anoAtual-anoNascimento)>18:
    print('Categoria: Absoluto')
else:
    print('Idade inválida')