import os


def listar_arquivos():
    items = os.listdir('.')
    for item in items:
        print(item)


def main():
    listar_arquivos()


main()
