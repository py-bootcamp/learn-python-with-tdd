from repeat import repeat


def test_repeat():
    got = repeat("a")
    want = "aaaaa"

    assert got == want
