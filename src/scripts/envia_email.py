import smtplib
import getpass
import json

def open_json():
    arquivo_json = open('src/data/dict_emails_apelidos.json', 'r')
    dict_dados_json = json.load(arquivo_json)
    return dict_dados_json

def envia_email():

    for dest, apelido in open_json().items():

        remetente = str(input("Informe o e-mail do remetente: ")).lstrip()
        senha = getpass.getpass(prompt="\nInforme a senha de e-mail do remetente: ").lstrip()

        destinatario = dest
        mensagem = "Oi, esse eh o seu apelido na planilha centavos.xlsx" 
        msg = f"{mensagem} : {str(apelido)}"
        email_text = f"""\

        From: {remetente}
        To: {destinatario}

        {msg}
        """

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario,
                            f'Subject: Apelido planilha de centavos LOAC\n{email_text}')
            server.close()
            print(f'\nEmail enviado com sucesso para: {dest} \n')
        except:
            print(f'O email não foi enviado para: {dest} \n')

