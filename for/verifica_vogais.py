palavra = input("Informe uma palavra -> ")
vogais = 0

for letra in palavra:
    if letra == 'a' or \
       letra == 'e' or \
       letra == 'i' or \
       letra == 'o' or \
       letra == 'u':
        vogais += 1

print(f'A palavra {palavra} tem {vogais} vogais')
