from shutil import copy


def copiar_arquivo():
    copy('teste.txt', 'bkp_teste.txt')


def main():
    copiar_arquivo()


main()
