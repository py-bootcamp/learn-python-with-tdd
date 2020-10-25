from .hello import Hello
import pytest


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
