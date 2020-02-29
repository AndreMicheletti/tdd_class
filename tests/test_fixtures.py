import pytest


"""
    FIXTURE
 scope = session/function  - default: function
 params = parametros para a fixture
"""


@pytest.fixture(scope="session")
def balde():
    class Balde:
        agua = 0

        def __init__(self):
            self.agua = 0

    balde_obj = Balde()
    return balde_obj


def test_encher_balde(balde):

    balde.agua = 1

    assert balde.agua == 1


def test_balde_vazio(balde):

    assert balde.agua == 0, f"balde tem {balde.agua} de agua mas devia estar vazio"


@pytest.fixture(params=[2, 3, 5, 9])
def numeros_primo(request):
    return request.param


def test_numeros_primos(numeros_primo):

    for div in range(2, numeros_primo):
        assert numeros_primo % div != 0, f"{numeros_primo} é divisivel por {div}"
