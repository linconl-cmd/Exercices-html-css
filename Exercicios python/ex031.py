distância = float(input('Qual é a distância da sua viagem? '))
print('A distância da sua viagem é de{}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
