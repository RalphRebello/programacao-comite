def criar_arquivos(nome_arquivo):
    for i in range(5):
        with open(f'{nome_arquivo}{i+1}.txt', 'w') as arquivo:
            arquivo.write(f'Conteudo {i+1}')


def main():
    criar_arquivos('arq')


main()
