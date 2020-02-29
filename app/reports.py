

def gerar_dados():
    return {"title": "bora", "description": "ta daora"}


def fazer_upload_do_arquivo(dados):

    if True:
        raise Exception("COULD NOT CONNECT TO AMAZON AWS")

    print(dados)
    return "arquivo.xls"


def gerar_relatorio():

    dados = gerar_dados()
    arquivo = fazer_upload_do_arquivo(dados)

    return arquivo
