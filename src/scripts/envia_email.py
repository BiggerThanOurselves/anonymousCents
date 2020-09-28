import smtplib

def envia_email(emails_apelidos):

    for dest, apelido in emails_apelidos.items():

        remetente = 'fulano.onaluf@ccc.ufcg.edu.br'
        senha = 'minhasenha'

        destinatario = dest
        mensagem = f"Oi, esse eh o seu apelido na planilha centavos.xlsx : {str(apelido)}"
        email_text = f"""\

        From: {remetente}
        To: {destinatario}

        {mensagem}
        """

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario,
                            f'Subject: Apelido planilha de centavos LOAC\n{email_text}')
            server.close()
            print(f'Email enviado com sucesso para: {dest} \n')
        except:
            print(f'O email não foi enviado para: {dest} \n')
