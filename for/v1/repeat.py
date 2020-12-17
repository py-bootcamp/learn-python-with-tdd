def repeat(character: str) -> str:
    """Repeat returns character repeated 5 times."""
    word = ""
    for _ in range(5):
        word = word + character

    return word
