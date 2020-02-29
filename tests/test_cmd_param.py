import pytest


def test_slowpoke(sonic_param):
    from time import sleep

    if sonic_param is True:
        # PYTEST SKIP
        pytest.skip("esse teste é lento demais para o sonic")

    print("slooooooooooooow poke")

    sleep(1)

    assert True


def test_gotta_go_fast():

    assert True


def test_say_my_name(tester_name):

    assert False, f"ai não ein {tester_name}"
