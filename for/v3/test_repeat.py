from repeat import repeat


def test_repeat():
    got = repeat("a", 4)
    want = "aaaa"

    assert got == want
