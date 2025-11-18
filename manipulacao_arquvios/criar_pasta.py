import os


def criar_pasta(nome_pasta):
    os.mkdir(nome_pasta)
    print('PASTA CRIADA COM SUCESSO!')


def main():
    criar_pasta(input('Qual da pasta que deseja criar? -> '))


main()
