'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- Entre 25 e 30: Sobrepeso.
- Entre 30 e 40: Obesidade.
- Acima de 40: Obesidade Mórbida.
'''
peso=float(input('Digite o peso: '))
if peso<0:
    print('valor inválido')
else:
    altura=float(input('Digite a altura: '))
    if altura<0:
        print('valor inválido')
    else:        
        imc=peso/(altura**2)
        if imc<18.5:
            print('Abaixo do peso.')
        elif 18.5<=imc<25:
            print('Peso ideal.')
        elif 25<=imc<30:
            print('Sobrepeso')
        elif 30<=imc<40:
            print('Obesidade')
        else:
            print('Obesidade Mórbida')