import pytest

from hello import Hello


def test_hello_without_name():
    got = Hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = Hello("Christian")
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
    got = Hello(name, language)

    assert got == want
