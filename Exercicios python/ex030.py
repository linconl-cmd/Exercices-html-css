número = int(input('Me dia um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é \033[31mPAR\033[m'.format(número))
else:
    print('O número é {} \033[35mIMPAR\033[m'.format(número))
