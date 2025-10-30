def fatorial(numero):
    fat = 1
    for n in range(1, numero+1):
        fat *= n

    return fat


def main():
    n = int(input('Informe um numero ->'))
    print(f'O fatoria do numero é {fatorial(n)}')


main()
