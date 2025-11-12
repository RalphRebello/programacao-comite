def encontrar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo) as arquivo:
            texto = arquivo.readlines()
            cont = 0
            for linha in texto:
                if palavra.lower() in linha.lower():
                    cont += 1
                    print(
                        f'Palavra "{palavra.lower()}" '
                        f'encontrada! | '
                        f'Qtd palavras encontradas {cont}')
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO!!!')


def main():
    nome_arquivo = 'novo_texto.txt'
    palavra = input('Qual a palavra está procurando? -> ')
    encontrar_palavra(nome_arquivo, palavra)


main()
