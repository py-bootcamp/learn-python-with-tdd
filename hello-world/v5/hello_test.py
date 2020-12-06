from hello import Hello


def test_hello_without_name():
    got = hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want
