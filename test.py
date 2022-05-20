from main import roman


def test_1():
    assert roman(1) == "I"


def test_10():
    assert roman(10) == "X"

def test_7():
    assert roman(7) ==