import xlsxwriter
import random
import smtplib


def main(emails):
    planilha_centavos, pagina_planilha_centavos = cria_planilha_emails(
        'centavos')
    planilha_apelidos, pagina_planilha_apelidos = cria_planilha_emails(
        'apelidos')

    pagina_planilha_centavos.write('A1', 'Apelido')
    pagina_planilha_apelidos.write('A1', 'Email')
    pagina_planilha_apelidos.write('B1', 'Apelido')

    emails_e_apelidos = cria_dicionario_apelidos(emails)

    indice = 2
    for (email, apelido) in emails_e_apelidos.items():
        coluna_a = f'A{indice}'
        coluna_b = f'B{indice}'

        pagina_planilha_centavos.write(coluna_a, apelido)

        pagina_planilha_apelidos.write(coluna_a, email)
        pagina_planilha_apelidos.write(coluna_b, apelido)
        indice += 1

    planilha_centavos.close()
    planilha_apelidos.close()

    lista_emails = emails_e_apelidos.keys()
    print(f"Os emails estão sendo enviados para: \n{list(lista_emails)}\n")
    return emails_e_apelidos


def cria_dicionario_apelidos(emails):
    dict_apelidos = {}
    for email in emails:
        apelido = gera_apelido_sem_duplicidade(dict_apelidos.values())
        dict_apelidos[email] = apelido
    return dict_apelidos


def gera_apelido_sem_duplicidade(apelidos):
    apelido = random.randint(1000, 3000)
    if apelido in apelidos:
        return gera_apelido_sem_duplicidade(apelidos)
    return str(apelido)


def cria_planilha_emails(nome):
    planilha = xlsxwriter.Workbook(f'{nome}.xlsx')
    pagina_planilha = planilha.add_worksheet()

    bold = planilha.add_format({'bold': True})
    pagina_planilha.set_column('A:A', 50, bold)


    return (planilha, pagina_planilha)


def envia_email(emails_apelidos):

    for dest, apelido in emails_apelidos.items():

        remetente = 'leandra.silva@ccc.ufcg.edu.br'
        senha = 'leandrinha1717'

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


with open('emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)

if __name__ == '__main__':
    emails_apelidos = main(emails)
    envia_email(emails_apelidos)
