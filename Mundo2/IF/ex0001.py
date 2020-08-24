'''
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado(desconsiderando os juros).
Etapas
1.Perguntar e guardar o valor da casa.
2.Perguntar e guardar o salário do comprador.
3.Perguntar e guardar em quanto tempo vai pagar a casa(anos).
4.Calcule o valor da prestação mensal.
5.Condição do salário.
'''
valorCasa = float(input('\nDigite o valor da casa: '))
salaraioComprador=float(input('\nQual o salário do comprador:'))
anos=int(input('\nEm quantos anos vai pagar:'))
prestacao=(valorCasa/(anos*12))
if prestacao<0.3*salaraioComprador:
    print('\nEmpréstimo aprovado!')
else:
    print('Empréstimo recusado!')
print('Valor da casa:R${:.2f}\nSalário do comprador:R${:.2f}\nTempo:{}meses\nValor da parcela:R${:.2f}\n'.format(valorCasa,salaraioComprador,anos*12,prestacao))