peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
  print('Você está abaixo do peso ideial')
elif 18.5 <= imc < 25:
  print('Você está com o peso ideal')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
  print('OBESIDADE')
elif imc >= 40 :
  print('OBESIDADE MÓRBIDA')