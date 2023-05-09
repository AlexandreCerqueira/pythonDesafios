def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero inteiro valido\033[m!')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dado(s) interrompida pelo usuario\033[m!')
            return 'NULO'
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('\033[32mSua opção:\033[m ')
    return opc

