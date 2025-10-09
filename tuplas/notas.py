notas = []

for i in range(5):
    notas.append(input('Informe uma nota -> '))

t_notas = tuple(notas)

print(f'A menor nota é {min(t_notas)}')
print(f'A maior nota é {max(t_notas)}')
