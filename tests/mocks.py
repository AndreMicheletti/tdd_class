import pytest


@pytest.fixture()
def mock_todo_gen():
    from app.controllers import insert_todo

    def todo_gen(title, description=None, due_date=None):
        res = insert_todo(title, description, due_date)

        if res is not True:
            raise RuntimeError("Erro ao inserir TODO usando o mock_todo_gen")
    return todo_gen


@pytest.fixture()
def mock_todo(mock_todo_gen):

    mock_todo_gen("default", "criado automaticamente pelo mock", None)
