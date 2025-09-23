nomes = ['Francisco', 'Shevchenko', 'Andry', 'Jao',
         'Ana', 'Eduardo', 'Alan']

for nome in nomes:
    for letra in nome:
        if letra == 'A':
            print(nome)
            break
