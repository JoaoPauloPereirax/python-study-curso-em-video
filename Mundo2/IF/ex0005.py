'''
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.1 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
===Etapas===
1. Pedir as duas notas do aluno.
'''
nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('\nDigite a segunda nota: '))
if ((nota1 or nota2) > 10) or ((nota1 or nota2)<0):
    print('Nota inválida')
else:
    media = (nota1+nota2)/2
    if media<5:
        print('Status: Reprovado')
    elif 5<media<7:
        print('Status: Recuperação')
    else:
        print('Status: Aprovado')