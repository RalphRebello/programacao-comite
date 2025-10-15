carros = {
    'marca': 'Fiat',
    'modelo': 'Uno R',
    'ano': '2002'
}

for chave in carros.keys():
    print(f'Chave {chave} |', end=' ')
print()

for chave in carros.values():
    print(f'Valor {chave} |', end=' ')
print()

for chave, valor in carros.items():
    print(f'Chave {chave} | Valor {valor}')
