import xlsxwriter
import random
import smtplib


with open('emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)


def main(emails):
    planilha_centavos, pagina_planilha_centavos = cria_planilha_emails(
        'centavos')
    planilha_apelidos, pagina_planilha_apelidos = cria_planilha_emails(
        'apelidos')

    email_apelido = {}
    random.seed(1098)
    
    raiz_apelido = random.randint(200, 300)
    for indice, email in enumerate(emails):

        chave_apelido = indice + 2
        apelido = raiz_apelido + chave_apelido

        linha_email = f'A{chave_apelido}'
        linha_apelido = f'B{chave_apelido}'

        pagina_planilha_apelidos.write(linha_email, email)
        pagina_planilha_centavos.write(linha_email, email)

        pagina_planilha_apelidos.write(linha_apelido, apelido)
        email_apelido[email] = apelido

    planilha_centavos.close()
    planilha_apelidos.close()

    lista_emails = email_apelido.keys()
    print("Os emails estão sendo enviados para: \n{}\n".format(list(lista_emails)))
    return email_apelido


def cria_planilha_emails(nome):
    planilha = xlsxwriter.Workbook(f'{nome}.xlsx')
    pagina_planilha = planilha.add_worksheet()

    bold = planilha.add_format({'bold': True})
    pagina_planilha.set_column('A:A', 50, bold)

    pagina_planilha.write('A1', 'E-mails')

    return (planilha, pagina_planilha)


def envia_email(emails_e_apelidos):

    for dest, apelido in emails_e_apelidos.items():

        remetente = 'leandra.silva@ccc.ufcg.edu.br'
        senha = 'leandrinha1717'

        destinatario = dest
        mensagem = "Oi, esse eh o seu apelido na planilha centavos.xlsx : " + str(apelido)
        email_text = """\

        From: %s
        To: %s

        %s
        """ % (remetente, destinatario, mensagem)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(remetente, senha)
            server.sendmail(remetente,destinatario ,'Subject: Apelido planilha de centavos LOAC\n{}'.format(email_text))
            server.close()
            print(f'Email enviado com sucesso para: {dest} \n')
        except:
            print(f'O email não foi enviado para: {dest} \n')

if __name__ == '__main__':
    emails_e_apelidos = main(emails)
    envia_email(emails_e_apelidos)