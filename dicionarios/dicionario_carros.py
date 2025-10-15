carros = {
    'marca': 'Fiat',
    'modelo': 'Uno R',
    'ano': '2002'
}

print(carros['marca'])

carros['cor'] = 'Prata'

print(carros)

##################################

carros.update({'ano': '2007'})
del carros['modelo']
print(carros)
# print(carros['modelo'])
print(carros.get('modelo'))
