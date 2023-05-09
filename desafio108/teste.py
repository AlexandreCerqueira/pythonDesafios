import moeda

preco = float(input('Digite o preco: R$  '))
ta = float(input('Taxa de aumento em %: '))
tr = float(input('Taxa de redução em %: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Com um aumento de {ta}% é {moeda.moeda(moeda.aumentar(preco, ta))}')
print(f'Com uma redução de {tr}% é {moeda.moeda(moeda.diminuir(preco, tr))}')
