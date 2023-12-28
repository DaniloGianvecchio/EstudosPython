#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = int(input('digite uma medida em metros: '))
c = (m*100)
mi = (m*1000)
print('a medida em centimetros e {}, a medida em milimetros e {}'.format(c, mi))