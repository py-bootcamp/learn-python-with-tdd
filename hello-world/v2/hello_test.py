from hello import hello


def test_hello():
    got = hello()
    want = "Hello, world"

    assert got == want
