import pytest
from .mocks import *


def pytest_addoption(parser):
    """
        ISSO É UM HOOK DO PYTEST
    """
    # https://docs.pytest.org/en/latest/example/simple.html
    parser.addoption(
        "--sonic", action="store_true", default=False, help="se for passado esse parametro, nao rodar testes lentos"
    )
    parser.addoption(
        "--myname", action="store", default="john doe", help="seu nome"
    )


@pytest.fixture
def sonic_param(request):
    return request.config.getoption("--sonic")


@pytest.fixture
def tester_name(request):
    return request.config.getoption("--myname")


@pytest.fixture(scope="session")
def flask_app():
    from app.app import create_flask_app

    flsk = create_flask_app()
    flsk.testing = True

    class ClientTest(object):

        def get(self, *args, **kwargs):
            with flsk.test_client() as c:
                return c.get(*args, **kwargs)

        def post(self, *args, **kwargs):
            with flsk.test_client() as c:
                return c.post(*args, **kwargs)

        def delete(self, *args, **kwargs):
            with flsk.test_client() as c:
                return c.delete(*args, **kwargs)

    client_test = ClientTest()
    return client_test


@pytest.fixture(autouse=True)
def cleanup():
    from app.app import todos_list, logs

    keys = list(todos_list.keys())
    for t in keys:
        del todos_list[t]

    size = range(len(logs))
    for i in size:
        del logs[i]