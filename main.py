from colorama import (init, Fore, Style)
from src.data import constantes
from src.scripts.envia_email import envia_email
from src.scripts.cria_planilhas import cria_planilhas

with open('./src/data/emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)

def main():
    opcao = seleciona_opcao()   

    if opcao == '5':
        print('Até a próxima!')
    else:
        print(opcao)
        main()

def seleciona_opcao():
    opcao_selecionada = str(input(constantes.OPCOES_SISTEMA)).replace(' ', '')

    if opcao_selecionada not in constantes.DICT_OPCOES.keys():
        print(Fore.RED + 'Seleciona uma opção válida')
        seleciona_opcao()

    return opcao_selecionada

if __name__ == '__main__':
    init(autoreset=True)
    main()
    # emails_apelidos = cria_planilhas(emails)
    # envia_email(emails_apelidos)
