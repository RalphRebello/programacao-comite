matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(matriz[1][1])

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()
