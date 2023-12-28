nome = input('qual seu nome?  ')
print('')
print('ola',nome,',prazer te conhecer!')
print('')
idade = input('qual sua idade?  ')
print('bom',idade,', estou correto?  ')
print('')
resposta = str(input(''))
if resposta=='sim':                                  #se ou caso
    print('obrigado')
else:                                                #se não ou caso não
    idade = input('qual sua idade?  ')
print('')
resposta = str(input(''))
if resposta=='sim':
    print('obrigado')
else:
    print('erro')