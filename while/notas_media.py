nota = 0
soma_notas = 0
qtd_notas = 0

while nota >= 0:
    nota = int(input('Informe uma nota -> '))
    soma_notas += nota
    qtd_notas += 1

print(f'A média das notas é {soma_notas / qtd_notas}')
