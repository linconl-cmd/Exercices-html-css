from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador 'PENSAR'
print('=^=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('=^=' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('CARREGANDO... ')
sleep(5)
if jogador == computador:
    print('PARABÉNS! você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
