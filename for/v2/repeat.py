COUNTER: int = 5

def repeat(character: str) -> str:
    """Repeat returns character repeated 5 times."""
    word = ""
    for counter in range(COUNTER):
        word += character

    return word
