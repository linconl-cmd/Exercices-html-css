num = int(input('Digite um número? '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
       print('\033[33m', end='')
       tot += 1
    else:
        print ('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[34mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
  print('O número é PRIMO')
else:
  print('O número NÃO É PRIMO')