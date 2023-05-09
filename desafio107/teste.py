import moeda

preco = float(input('Digite o preco: R$  '))
ta = float(input('Taxa de aumento em %: '))
tr = float(input('Taxa de redução em %: '))
print(f'O dobro de R$ {preco} é R$ {moeda.dobro(preco)}')
print(f'A metade de R$ {preco} é R$ {moeda.metade(preco)}')
print(f'Com um aumento de {ta}% é R$ {moeda.aumentar(preco, ta)}')
print(f'Com uma redução de {tr}% é R$ {moeda.diminuir(preco, tr)}')
