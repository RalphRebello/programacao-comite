numero = 1
maior_numero = 0

while numero != 0:
    numero = int(input('Informe um numero -> '))

    if numero > maior_numero:
        maior_numero = numero
    else:
        maior_numero = maior_numero

print(f'O maior numero é {maior_numero}')
