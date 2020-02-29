
def test_hello(flask_app):

    response = flask_app.get("/hello")

    assert response.data == b"hello world"


def test_insert_todo(flask_app):

    response = flask_app.post("/todo", json={"title": "oi"})

    response_data = response.json

    assert response.status_code == 200
    assert response_data == "inserted"

