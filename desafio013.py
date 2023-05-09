nome = input('Qual o nome do funcionario? ')
sal = float(input('Qual o salario atual em euros? '))
au = sal * 0.15
ns = sal + au
print('{}, seu salario teve um aumento de 15%, agora sera de {:.2f} euros!'.format(nome, ns))
