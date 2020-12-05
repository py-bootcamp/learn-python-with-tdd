from hello import Hello


def test_hello():
    got = Hello("Christian")
    want = "Hello, Christian"

    assert got == want
