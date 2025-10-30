def contar_vogais(texto):
    vogais = ('a', 'e', 'i', 'o', 'u')
    cont_vogais = 0
    for letra in texto:
        if letra in vogais:
            cont_vogais += 1

    return cont_vogais


def main():
    qtd_vogais = contar_vogais(input('Digite o texto -> '))
    print(f'O texto digitado tem {qtd_vogais} vogais!')


main()
