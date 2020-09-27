import xlsxwriter
import random


def cria_planilhas(emails):
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
    planilha = xlsxwriter.Workbook(f'src/data/{nome}.xlsx')
    pagina_planilha = planilha.add_worksheet()

    bold = planilha.add_format({'bold': True})
    pagina_planilha.set_column('A:A', 50, bold)


    return (planilha, pagina_planilha)
