from hello import hello


def test_hello():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want
