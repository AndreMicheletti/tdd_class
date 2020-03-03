
def test_hello(flask_app):

    response = flask_app.get("/hello")

    assert response.data == b"hello world"


def test_capitalize_title():
    """ TESTE DE CONTROLLER PURO """
    from app.controllers import capitalize_title

    res = capitalize_title("andre")

    assert res == "ANDRE"

    res = capitalize_title("pytest is daora")

    assert res == "PYTEST IS DAORA"


def test_insert_todo(flask_app):
    """ TESTE DE API """
    from app.app import todos_list

    response = flask_app.post("/todo", json={"title": "tarefa 1"})

    response_data = response.json

    assert response.status_code == 200
    assert response_data == "inserted"
    assert len(todos_list) == 1
    assert "tarefa 1" in todos_list.keys()
