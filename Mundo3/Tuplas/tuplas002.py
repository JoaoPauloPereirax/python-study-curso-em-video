'''Crie uma tupla preenchida como os 20 primeiros colocados da tabela do Campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

    a) Apenas os 5 primeiros colocados.

    b) Os últimos 4 colocados.

    c) Uma lista com os times em ordem alfabética.

    d) Em que posição na tabela está o time do Grêmio.'''
    
brasileiro=('ATLETICOPARANAENSE','SPORTRECIFE','ATLETICOMINEIRO', 'GREMIO', 'INTERNACIONAL', 'BRAGANTINO', 'SANTOS', 'ATLETICOGOIANIENSE', 'BAHIA', 'BOTAFOGO', 'CORINTHIANS', 'GOIAS', 'PALMEIRAS', 'SAOPAULO', 'VASCODAGAMA', 'CEARASC', 'CORITIBA', 'FLAMENGO', 'FLUMINENSE', 'FORTALEZA')
#Os cinco primeros
print('\nOs 5 primeros colocados')
for ate in range(0,4,1):
    print('{}° {}'.format(ate+1,brasileiro[ate]))
#Os ultimos 4 colocados
print('\nOs 4 últimos colocados')
for cont1 in range(16,20,1):
    print('{}° {}'.format(cont1+1,brasileiro[cont1]))
#Ordem alfabética
print('\nOrdem alfabética')
tuplaOrdenada=sorted(brasileiro)
for cont2 in tuplaOrdenada:
    print(cont2)
#Gremio
print('\nO Time do Grêmio está em {}° lugar\n'.format(brasileiro.index('GREMIO')+1))