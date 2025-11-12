def contar_linhas():
    try:
        with open('log.txt') as arquivo:
            return len(arquivo.readlines())
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO!!!')


def main():
    qtd_linhas = contar_linhas()
    print(f"O arquivo lido tem {qtd_linhas} linhas!")


main()
