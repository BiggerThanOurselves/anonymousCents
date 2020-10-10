import json
import smtplib
import getpass
from decouple import config
from colorama import Fore
from src.scripts.util.manipular_json import abre_json

def envia_email():
    emails_apelidos = abre_json('src/data/dict_emails_apelidos.json')

    remetente = str(input("\nInforme o e-mail do remetente: ")).lstrip()
    senha = getpass.getpass(prompt="Informe a senha de e-mail do remetente: ").lstrip()

    for dest, apelido in emails_apelidos.items():

        link_planilha = 'e vamos de link'
        destinatario = dest

        email_text = f"""\
Oi, esse eh o seu apelido na planilha centavos.xlsx {apelido}.
Link para a planilha: https://docs.google.com/spreadsheets/d/{config('TOKEN_CENTAVOS')}\
"""
        envia(remetente, senha, destinatario, email_text)


def envia(remetente, senha, destinatario, email_text):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario,
                                f'Subject: Apelido planilha de centavos LOAC\n{email_text}')
        server.close()
        print(Fore.GREEN + f'\nEmail enviado com sucesso para: {destinatario}')

    except Exception as err:
        print(str(err))
        print(Fore.RED + f'\nO email não foi enviado para: {destinatario}')

def envia_email_unico(destinatario, apelido):

    remetente = str(input("\nInforme o e-mail do remetente: ")).lstrip()
    senha = getpass.getpass(prompt="Informe a senha de e-mail do remetente: ").lstrip()

    mensagem = f"Oi, esse eh o seu apelido na planilha centavos.xlsx {apelido}."
    email_text = f"""\
{mensagem}
Link para a planilha: https://docs.google.com/spreadsheets/d/{config('TOKEN_CENTAVOS')}\
"""
    envia(remetente, senha, destinatario, email_text)
