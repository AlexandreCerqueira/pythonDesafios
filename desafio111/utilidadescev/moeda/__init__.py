def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Manipula um valor digitado
    :param preco: O valor digitado
    :param taxa: A taxa em % que ira aumentar a var preco
    :param formato: Formatacao automatica para R$ e valor dividido por ,
    :return: valor formatado
    """
    res = preco + (preco*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Manipula um valor digitado
    :param preco: O valor digitado
    :param taxa: A taxa em % que ira diminuir a var preco
    :param formato: Formatacao automatica para R$ e valor dividido por ,
    :return: valor formatado
    """
    res = preco - (preco*taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Dobra o valor digitado
    :param preco: O valor digitado
    :param formato: Formatacao automatica para R$ e valor dividido por ,
    :return: valor formatado
    """
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    """
    -> Divide por 2 o valor digitado
    :param preco: O valor digitado
    :param formato: Formatacao automatica para R$ e valor dividido por ,
    :return: valor formatado
    """
    res = preco/2
    return res if not formato else moeda(res)#mesmo que 'return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Formata o output para R$ e valor dividido por ,
    :param preco: O valor digitado
    :param moeda: Formatacao com R$
    :return: retorna o valor com R$
    """
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('+='*20)
    print('RESUMO DO VALOR'.center(40))
    print('+='*20)
    print(f'Preco analisado \t{moeda(preco)}')
    print(f'Dobro do preco \t\t{dobro(preco, formato=True)}')
    print(f'Metade do preco \t{metade(preco, formato=True)}')
    print(f'Mais {taxaa}% do preco \t{aumentar(preco, taxaa, formato=True)}')
    print(f'Menos {taxar}% do preco \t{diminuir(preco, taxar, formato=True)}')
    print('+='*20)

