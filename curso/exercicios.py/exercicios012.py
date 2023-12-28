#faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('diga o preço do produto'))
pc = (p*5)/100
print('o preço do produto sera {}'.format(p-pc))