from desafio115.Lib.interface import *
from desafio115.Lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opcao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opcao de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m!')
    sleep(2)

