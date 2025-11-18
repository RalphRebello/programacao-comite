import json


def salvar_json(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo, indent=4)


def main():
    dicionario = {'nome': 'Ralph',
                  'idade': 33,
                  'profissao': 'Engenheiro',
                  'pais': 'Brasil'}
    nome_arquivo = 'dados.json'

    salvar_json(dicionario, nome_arquivo)


main()
