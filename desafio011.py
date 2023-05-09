a = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
ar = a * l
tt = ar / 2
print('O total da area da parede é {:.2f}m, sera necessario {:.2f} litros de tinta papa pinta-la!'.format(ar, tt))
