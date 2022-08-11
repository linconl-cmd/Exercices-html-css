velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 84:
    print('\033[4;31mMULTADO!\033[m Você excedeu o limite permitido que é 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {}R$:{:.2f}{}!'.format('\033[32m',multa,'\033[m'    ))
else:
    print('\033[32mTenha um bom dia! Dirija com cuidado!')

