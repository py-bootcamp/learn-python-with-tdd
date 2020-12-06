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

    prefix = ENGLISH_HELLO_PREFIX

    if language == SPANISH:
        prefix = SPANISH_HELLO_PREFIX

    if language == FRENCH:
        prefix = FRENCH_HELLO_PREFIX

    return f"{prefix}, {name}"


print(hello("world"))
