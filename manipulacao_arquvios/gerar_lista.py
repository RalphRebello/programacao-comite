def gerar_lista(arquivo):
    lista = []
    try:
        with open(arquivo) as arq:
            for linha in arq:
                lista.append(linha.strip())
        return lista
    except FileNotFoundError:
        print('Arquivo não encontrado! ')


def main():
    lista = []
    arquivo = 'frutas.txt'
    lista = gerar_lista(arquivo)
    print(lista)


main()
