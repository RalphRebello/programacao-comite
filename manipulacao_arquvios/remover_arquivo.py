import os


def remover_arquivo(nome_arquivo):
    try:
        os.remove(nome_arquivo)
        print('ARQUIVO APAGADO!')
    except FileNotFoundError:
        print('Arquivo não existe ou já foi apagado!!!')


def main():
    remover_arquivo(input('Qual arquivo deseja apagar? -> '))


main()
