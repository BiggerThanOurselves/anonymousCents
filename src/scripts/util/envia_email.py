import json
import smtplib
import getpass
from decouple import config
from colorama import Fore
from src.scripts.util.manipular_json import open_json

def envia_email():
    emails_apelidos = open_json('src/data/dict_emails_apelidos.json')

    remetente = str(input("\nInforme o e-mail do remetente: ")).lstrip()
    senha = getpass.getpass(prompt="Informe a senha de e-mail do remetente: ").lstrip()
    for dest, apelido in emails_apelidos.items():

        link_planilha = 'e vamos de link'
        destinatario = dest
        mensagem = f"Oi, esse eh o seu apelido na planilha centavos.xlsx {apelido}."
        email_text = f"""\
{mensagem}
Link para a planilha: https://docs.google.com/spreadsheets/d/{config('TOKEN_CENTAVOS')}\
"""

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario,
                            f'Subject: Apelido planilha de centavos LOAC\n{email_text}')
            server.close()
            print(Fore.GREEN + f'\nEmail enviado com sucesso para: {dest}')

        except Exception as err:
            print(Fore.RED + f'\nO email não foi enviado para: {dest}')
