from hello import Hello


def test_hello_without_name():
    got = Hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = Hello("Christian")
    want = "Hello, Christian"

    assert got == want


def test_hello_with_name_in_spanish():
    got = Hello("Christian", "Spanish")
    want = "Hola, Christian"

    assert got == want


def test_hello_with_name_in_french():
    got = Hello("Christian", "French")
    want = "Bonjour, Christian"

    assert got == want
