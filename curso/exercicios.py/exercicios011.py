#faça um programa que leia a largura e a altura de uma paredeem metros. calcule a sua area e a necessaria para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2metros quadrados.

pa = int(input('qual a o altura da sua parde'))
pl = int(input('qual a o largura da sua parde'))
t = (pl * pa)/2

print('a quantidade de tinta necessaria sera de {} litros'.format(t))

