import pytest

from hello import hello


def test_hello_without_name():
    got = hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want


@pytest.mark.parametrize(
    "name, language, want",
    [
        ("Christian", "", "Hello, Christian"),
        ("", "", "Hello, World"),
        ("Elodie", "Spanish", "Hola, Elodie"),
        ("Lauren", "French", "Bonjour, Lauren"),
    ],
)
def test_hello(name, language, want):
    got = hello(name, language)

    assert got == want
