import json

def abre_json(caminho):
    arquivo_json = open(caminho, 'r')
    dict_dados_json = json.load(arquivo_json)
    arquivo_json.close()
    return dict_dados_json

def grava_json(caminho, conteudo):
    arquivo_json = open(caminho, 'w')
    json.dump(conteudo, arquivo_json)
    arquivo_json.close()
    return abre_json(caminho)
