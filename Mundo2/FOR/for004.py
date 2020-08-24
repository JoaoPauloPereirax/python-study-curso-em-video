'''Faça a tabuada do número que o usuário escolher.'''
numUsuario=int(input('Digite um número: '))
print('TABUADA')
for cont in range(10,0,-1):
    print('{}X{}={}'.format(cont,numUsuario,numUsuario*cont))