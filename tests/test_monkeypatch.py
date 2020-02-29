

def test_gerar_relatorio(monkeypatch):

    from app import reports

    def nova_function(dados):
        return "arquivo_monkey.xls"

    monkeypatch.setattr(reports, "fazer_upload_do_arquivo", nova_function)

    relatorio = reports.gerar_relatorio()

    assert relatorio == "arquivo_monkey.xls"
