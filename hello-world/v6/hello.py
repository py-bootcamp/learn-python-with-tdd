SPANISH = "Spanish"
FRENCH = "French"
ENGLISH_HELLO_PREFIX = "Hello"
SPANISH_HELLO_PREFIX = "Hola"
FRENCH_HELLO_PREFIX = "Bonjour"


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    if language == SPANISH:
        return f"{SPANISH_HELLO_PREFIX}, {name}"

    if language == FRENCH:
        return f"{FRENCH_HELLO_PREFIX}, {name}"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(hello("world"))
