coordenadas = []
cont = 0

# Cria coordenadas
for linha in range(3):
    temp = []
    for coluna in range(2):
        temp.append(cont + 1)
        cont += 1

    coordenadas.append(tuple(temp))

coordenadas = tuple(coordenadas)
print(coordenadas, '\n')

# forma 1
for l in coordenadas:
    cont = 0
    x = 0
    y = 0

    for c in l:
        if cont == 0:
            x = c
        else:
            y = c
        cont += 1

    print(f'Ponto: x={x}, y={y}')

print()

# forma 2
for linha in coordenadas:
    print(f'Ponto: x={linha[0]}, y={linha[1]}')

print()

# forma 3
for x, y in coordenadas:
    print(f'Ponto: x={x}, y={y}')
