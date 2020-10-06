from colorama import (init, Fore, Style)
from src.scripts.inicia_sistema import inicia_sistema
from src.scripts.envia_email import envia_email
from src.scripts.cria_planilhas import cria_planilha_apelidos


OPCOES_SISTEMA = """
Digite o número de uma das opções a seguir:

1. Iniciar sistema
2. Sair

Digite aqui: """
    

DICT_OPCOES = {
    '1': inicia_sistema,
    '2': 'sair'
}

def main():

    while(True):
        opcao = seleciona_opcao()

        if opcao == '2':
            print('Até a próxima!')
            break
        else:
            DICT_OPCOES[opcao]()


def seleciona_opcao():
    opcao_selecionada = str(input(OPCOES_SISTEMA)).replace(' ', '')

    if opcao_selecionada not in DICT_OPCOES.keys():
        print('--------------------------')
        print(Fore.RED + 'Selecione uma opção válida')
        print('--------------------------')

        opcao_selecionada = seleciona_opcao()

    return opcao_selecionada

if __name__ == '__main__':
    init(autoreset=True)
    main()
    # envia_email(emails_apelidos)
