import smtplib
import getpass

def envia_email(emails_apelidos):

    for dest, apelido in emails_apelidos.items():

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
