listagem = ('Lápis', 175,
            'Boarracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 5,
            'Livro', 34.90)
print('-' * 40)
print(f'{"Listagens de preço":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')