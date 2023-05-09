d = float(input('Quantos dias alugados? '))
k = float(input('Quantos KM rodados? '))
td = d * 60
tk = k * 0.15
print('Total a pagar é de R${:.2f}'.format(td + tk))
