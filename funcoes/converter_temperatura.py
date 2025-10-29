def converter(temp):
    return temp * 1.8 + 32


def main():
    temp_f = converter(float(input('Informe a temperatura'
                                   'em °C -> ')))
    print(f'a temperatura em °F é {temp_f}')


main()
