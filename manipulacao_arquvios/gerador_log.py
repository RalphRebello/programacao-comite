from datetime import datetime


def gerar_logs():
    with open('log.txt', 'w') as arquivo:
        for i in range(200):
            agora = datetime.now()
            arquivo.write(f'{agora} LOG {i+1} \n')

    print('Log gerado com sucesso!')


def main():
    gerar_logs()


# antony
main()
