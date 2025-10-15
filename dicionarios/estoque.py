estoque = {
    'caderno': 10,
    'lapis': 25,
    'mochila': 87
}

print('Estoque Atualizado')
for chave, valor in estoque.items():
    print(f'Produto - {chave} | Qtd produto - {valor}')

estoque.update({'mochila': 50, 'caderno': 0})
print('Vendas efetuadas com sucesso!')

print('Estoque Atualizado')
for chave, valor in estoque.items():
    print(f'Produto - {chave} | Qtd produto - {valor}')

print('Adicionando um novo item ao estoque')
estoque['corretivo'] = 45

print('Estoque Atualizado')
for chave, valor in estoque.items():
    print(f'Produto - {chave} | Qtd produto - {valor}')

print('Removendo um produto do estoque')
del estoque['lapis']

print('Estoque Atualizado')
for chave, valor in estoque.items():
    print(f'Produto - {chave} | Qtd produto - {valor}')

print('Limpando o estoque')
estoque.clear()
print(f'Estoque Limpo - {estoque}')
