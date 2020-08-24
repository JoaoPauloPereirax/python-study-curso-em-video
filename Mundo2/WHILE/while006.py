'''Melhore o exercício anterior, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa termina quando ele disser que quer mostrar 0 termos.'''
primeiroTermo=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da PA: '))
continua=10
n=0
aux=0
while continua!=0:
    while n!=(continua+aux):
        print(primeiroTermo+n*razao)
        n+=1
    aux=n
    continua=int(input('mais quantos elementos quer mostrar(0 para sair)?'))
print('Fim do programa!')