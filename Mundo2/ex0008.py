'''
Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento.
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- Em até 3x ou mais no cartão: 20% de juros
'''
precoProduto = float(input('\nDigite o preço do produto: '))
condicaoPagamento = int(input('\n1 - À vista dinheiro/cheque: 10% de desconto\n2 - À vista no cartão: 5% de desconto\n3 - Em até 2x no cartão: Preço normal\n4 - Em até 3x ou mais no cartão: 20% de juros\nEscolha acondição de pagamento: '))
if condicaoPagamento == 1:
    print('\nCondição escolhida: À vista dinheiro/cheque\nPreço: R$ {:.2f}'.format(precoProduto*0.9))
elif condicaoPagamento == 2:
    print('\nCondição escolhida:  vista no cartão\nPreço: R$ {:.2f}'.format(precoProduto*0.95))
elif condicaoPagamento == 3:
    print('\nCondição escolhida:  Em até 2x no cartão\nPreço: R$ {:.2f}'.format(precoProduto))
elif condicaoPagamento == 4:
    print('\nCondição escolhida:  Em até 3x ou mais no cartão\nPreço: R$ {:.2f}'.format(precoProduto*1.2))