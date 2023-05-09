import moeda

preco = float(input('Digite o preco: R$  '))
ta = float(input('Taxa de aumento em %: '))
tr = float(input('Taxa de redução em %: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, formato=True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, formato=True)}')
print(f'Com um aumento de {ta}% é {moeda.aumentar(preco, ta, formato=True)}')
print(f'Com uma redução de {tr}% é {moeda.diminuir(preco, tr, formato=True)}')
