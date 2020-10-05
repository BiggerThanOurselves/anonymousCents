from colorama import (init, Fore, Style)
from src.data import constantes
from src.scripts.envia_email import envia_email
from src.scripts.cria_planilhas import cria_planilha_apelidos_emails
import gspread


dicionario = {"leandra.silva@ccc.ufcg.edu.br": "263125"}
endereco_planilha = '1dBC8d7zBAy0TnL_2PC58DvXK9FKgSE8ljVsiGh-xWKk'

with open('./src/data/emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)

def main():
    opcao = seleciona_opcao()   

    if opcao == '2':
        print('Até a próxima!')
    else:
        print(opcao)
        cria_planilha_apelidos_emails(dicionario, endereco_planilha)    


def seleciona_opcao():
    opcao_selecionada = str(input(constantes.OPCOES_SISTEMA)).replace(' ', '')

    if opcao_selecionada not in constantes.DICT_OPCOES.keys():
        print(Fore.RED + 'Selecione uma opção válida')
        seleciona_opcao()

    return opcao_selecionada

if __name__ == '__main__':
    init(autoreset=True)
    main()




