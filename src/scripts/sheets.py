import gspread


gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1dBC8d7zBAy0TnL_2PC58DvXK9FKgSE8ljVsiGh-xWKk')
worksheet = sh.sheet1

res = worksheet.get_all_records()
entrada = float(input("Digite os centavos:  "))
adiciona = [entrada]
linha_sheets = 5
worksheet.insert_row(adiciona, linha_sheets)