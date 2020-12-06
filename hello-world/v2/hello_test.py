from hello import Hello


def test_hello():
    got = hello()
    want = "Hello, world"

    assert got == want
