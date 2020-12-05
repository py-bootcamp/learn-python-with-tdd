SPANISH = "Spanish"
FRENCH = "French"
ENGLISH_HELLO_PREFIX = "Hello"
SPANISH_HELLO_PREFIX = "Hola"
FRENCH_HELLO_PREFIX = "Bonjour"


def Hello(name: str = None, language: str = None) -> str:
    """Hello returns a personalized greeting in a given language."""
    if not name:
        name = "World"

    prefix = ENGLISH_HELLO_PREFIX

    if language == SPANISH:
        prefix = SPANISH_HELLO_PREFIX

    if language == FRENCH:
        prefix = FRENCH_HELLO_PREFIX

    return f"{prefix}, {name}"


print(Hello("world"))
