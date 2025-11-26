def gerar_boletim(aluno):
    with open('boletim.txt', 'w') as boletim:
        for chave, valor in aluno.items():
            if type(valor) != float:
                boletim.write(f'{chave} | {valor}\n')
            else:
                boletim.write(f'{chave} | {valor:.2f}\n')

    for chave, valor in aluno.items():
        if type(valor) != float:
            print(f'{chave} | {valor}')
        else:
            print(f'{chave} | {valor:.2f}')


def calcular_boletim(aluno):
    media = (aluno['Nota_1'] + aluno['Nota_2'] + aluno['Nota_3']) / 3
    status_aluno = ''
    if media >= 7:
        status_aluno = 'APROVADO'
    else:
        status_aluno = 'REPROVADO'

    aluno.update({'Média': media,
                  'status_aluno': status_aluno})

    gerar_boletim(aluno)


def obtem_info():
    aluno = {'Nome': '',
             'Nota_1': 0,
             'Nota_2': 0,
             'Nota_3': 0}

    aluno['Nome'] = input('Informe o nome do aluno -> ')
    aluno['Nota_1'] = float(input('Informe a primeira nota -> '))
    aluno['Nota_2'] = float(input('Informe a segunda nota -> '))
    aluno['Nota_3'] = float(input('Informe a terceira nota -> '))

    return aluno


def main():
    aluno = obtem_info()
    calcular_boletim(aluno)


main()
