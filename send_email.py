import smtplib

try:
        destinatario  = 'rodrigo.cavalcanti@ccc.ufcg.edu.br'
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        remetente = 'leandra.silva@ccc.ufcg.edu.br'
        senha = 'leandrinha1717'
        smtpObj.login(remetente, senha)
        msg = '''
        Seu apelido na planilha de centavos.xlsx é: 
        '''
        smtpObj.sendmail(remetente,destinatario ,'Subject: Apelido da planilha de centavos LOAC\n{}'.format(msg))
        smtpObj.quit()
        print("Email enviado com sucesso!")
except:
        print("Erro ao enviar e-mail")