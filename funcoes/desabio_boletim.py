def boletim(nome, n1, n2, n3):
    dados_aluno = {}
    media = (n1 + n2 + n3) / 3
    status_aluno = ''
    if media >= 7:
        status_aluno = 'APROVADO'
    else:
        status_aluno = 'REPROVADO'

    dados_aluno.update({'nome': nome,
                        'media': media,
                        'status_aluno': status_aluno})

    return dados_aluno


def main():
    nome_aluno = input('Informe o nome do aluno -> ')
    nota1 = float(input('Informe a primeira nota -> '))
    nota2 = float(input('Informe a segunda nota -> '))
    nota3 = float(input('Informe a terceira nota -> '))

    resultado = boletim(nome_aluno, nota1, nota2, nota3)

    print(resultado)


main()
