palavra_secreta = input("Informe a palavra secreta -> ")
palavra_encontrada = ["-"] * len(palavra_secreta)
chute_letra = ''
tentativas = 4

for tentativa in range(tentativas+1):
    chute_letra = input(f'Chute uma letra {palavra_encontrada} -> ')

    for t in range(len(palavra_secreta)):
        if palavra_secreta[t] == chute_letra:
            palavra_encontrada[t] = chute_letra

    if "-" not in palavra_encontrada:
        print('Você venceu!!!!')
        break

    print(f'Faltam apenas {tentativas - tentativa - 1} tentativas')

else:
    print(f'Você perdeu, a palavra era {palavra_secreta}')
