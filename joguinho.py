from random import randint
from time import sleep
computador=randint(0,5)
jogador=int(input('em qual numero de 0 a 5 eu esto pensando? '))
print('')
print('processando.')
sleep(1)
print('')                                                        #salve
print('prosessando..')
sleep(1)
print('')
print('prosessando...')
sleep(1)
print('')
if jogador==computador:
    print('bona ragazzo, eu pensei no numero {}'. format (computador))
else:
    print('voce perdeu, eu pensei no numero {}' . format (computador))