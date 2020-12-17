def repeat(character: str, counter: int) -> str:
    """Repeat returns character repeated `counter` times."""
    word = ""
    for counter in range(counter):
        word += character

    return word
