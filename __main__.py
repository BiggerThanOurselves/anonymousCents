from colorama import (init, Fore, Style)
from src.scripts.inicia_sistema import inicia_sistema
from src.scripts.cadastra_email import cadastra_email

OPCOES_SISTEMA = """
--------------------------
Digite o número de uma das opções a seguir:

1. Iniciar sistema
2. Cadastrar apenas um e-mail
3. Sair

Digite aqui: """
    

DICT_OPCOES = {
    '1': inicia_sistema,
    '2': cadastra_email,
    '3': 'sair'
}

def main():

    while(True):
        opcao = seleciona_opcao()

        if opcao == '3':
            print(Fore.GREEN + '\nAté a próxima!')
            break
        else:
            DICT_OPCOES[opcao]()


def seleciona_opcao():
    opcao_selecionada = str(input(OPCOES_SISTEMA)).replace(' ', '')
    print('--------------------------')

    if opcao_selecionada not in DICT_OPCOES.keys():
        print('--------------------------')
        print(Fore.RED + 'Selecione uma opção válida')
        print('--------------------------')

        opcao_selecionada = seleciona_opcao()

    return opcao_selecionada

if __name__ == '__main__':
    init(autoreset=True)
    main()