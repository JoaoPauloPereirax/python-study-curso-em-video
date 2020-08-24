lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))
for comida in lanche:
    print('{}\n'.format(comida))
    print(f'{comida}\n')
print('Outra forma\n')

for cont in range(0,len(lanche)):
    print(lanche[cont])
print('\n')
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} que está guardada na posição {posicao}\n')
    print('Eu vou comer {} que está guardada na posição {}'.format(comida,posicao))
    