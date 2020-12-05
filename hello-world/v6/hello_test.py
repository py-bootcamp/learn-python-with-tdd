import pytest

from .hello import Hello


@pytest.mark.parametrize(
    "name, language, want",
    [
        ("Christian", "", "Hello, Christian"),
        ("", "", "Hello, World"),
        ("Elodie", "Spanish", "Hola, Elodie"),
        ("Lauren", "French", "Bonjour, Lauren"),
        ("Francesca", "Italian", "Ciao, Francesca"),
    ],
)
def test_hello(name, language, want):
    got = Hello(name, language)

    assert got == want
