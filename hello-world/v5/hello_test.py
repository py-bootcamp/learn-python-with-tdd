import pytest

from .hello import Hello


@pytest.mark.parametrize(
    "name, want", [("Christian", "Hello, Christian"), ("", "Hello, World")]
)
def test_hello(name, want):
    got = Hello(name)

    assert got == want
