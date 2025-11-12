def saudacao(nome, idade):
    return f'Olá {nome}, parabéns pelos seus {idade} anos!'


def main():
    nome = input('Informe seu nome -> ')
    idade = int(input('Informe sua idade -> '))

    boas_vindas = saudacao(nome, idade)

    print(boas_vindas)


main()
