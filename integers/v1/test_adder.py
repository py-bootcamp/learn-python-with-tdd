from adder import add


def test_add():
    sum = add(2, 2)
    expected = 4

    assert sum == expected
