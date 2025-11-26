import time
import sys


def mostrar_hora():
    while True:
        agora = time.strftime("%H:%M:%S")
        sys.stdout.write("\r⏰  " + agora)
        sys.stdout.flush()
        time.sleep(1)


def main():
    try:
        mostrar_hora()

    except KeyboardInterrupt:
        print('\nPROGRAMA ENCERRADO PELO USUÁRIO!')


main()
