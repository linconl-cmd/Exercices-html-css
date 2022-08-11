times = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo',
        'Grêmio','Palmeiras', 'Fluminense', 'Santos', 'Corinthians',
       'Atlético-PR', 'Ceara', 'Atlético-GO', 'Bragatino','Sport Recife',
       'Fortaleza', 'Vasco da Gama', 'Bahia', 'Bahia', 'Goiás', 'Botafogo',
        'Coritiba')
print('=-' * 15)
print(f'Lista de times{times}')
print('=-' * 15)
print(f'O 5 primeiros são {times[0:5]}')
print('=-' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('=-' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 15)
print(f'O Flamengo está na {times.index("Flamengo")+1}° posição')
