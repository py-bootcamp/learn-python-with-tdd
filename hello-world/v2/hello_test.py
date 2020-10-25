from .hello import Hello


def test_hello():
    got = Hello()
    want = "Hello, world"

    assert got == want
