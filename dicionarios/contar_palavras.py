palavras = ['ola',
            'mundo',
            'python',
            'comite',
            'pinoia',
            'dia'
            ]

qtd_letras = {}

for palavra in palavras:

    chave = f'qtd_palavras - {len(palavra)}'
    valor += 1

    qtd_letras.update({chave: valor})

for chave, valor in qtd_letras.items():
    print(f'{chave} | {valor}')
