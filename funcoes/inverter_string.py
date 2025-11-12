def inverter_string(palavra='Python'):
    palavra_invertida = palavra[::-1]
    print(f'A palavra invertida é {palavra_invertida}')


def main():
    palavra = input('Informe uma palavra -> ')
    inverter_string(palavra)


main()
