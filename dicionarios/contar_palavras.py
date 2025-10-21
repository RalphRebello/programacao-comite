palavras = ['ola',
            'mundo',
            'python',
            'comite',
            'pinoia',
            'dia'
            ]

qtd_letras = {}

for palavra in palavras:

    if f'qtd_palavras - {len(palavra)}' not in qtd_letras.keys():
        chave = f'qtd_palavras - {len(palavra)}'
        valor = 1

        qtd_letras.update({chave: valor})
    else:
        qtd_letras[f'qtd_palavras - {len(palavra)}'] += 1


for chave, valor in qtd_letras.items():
    print(f'{chave} | {valor}')
