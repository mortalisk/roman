from main import roman


def test_1():
    assert roman(1) == "I"


def test_10():
    assert roman(10) == "X"


def test_7():
    assert roman(7) == "VII"


def test_bigger_than_10():
    assert roman(11) == "XI"


def test_12():
    assert roman(12) == "XII"


def test_9():
    assert roman(9) == "IX"


def test_8():
    assert roman(8) == "VIII"


def test_random_fixed_list():
    range_size = 5
    results = ["I", "II", "III", "IV"]
    romans = []
    for i in range(1, range_size):
        romans.append(roman(i))

    assert romans == results
    #assert len(romans) == range_size