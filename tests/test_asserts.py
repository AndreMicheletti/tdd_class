import pytest


def test_somar():
    """
        Sintaxe do assert
    """
    assert 2 + 2 == 3, "a soma deve resultar 4"


def test_assertion():
    """
        Use assert sem condição com muito cuidado
    """
    for i in range(3):
        assert i


def test_exception_raise():
    """
        pytest.raises
    """

    with pytest.raises(ZeroDivisionError):
        vai_dar_ruim = 2 / 0

    vai_dar_bom = 2 / 2
    assert vai_dar_bom == 1
