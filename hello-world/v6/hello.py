SPANISH = "Spanish"
FRENCH = "French"
ENGLISH_HELLO_PREFIX = "Hello"
SPANISH_HELLO_PREFIX = "Hola"
FRENCH_HELLO_PREFIX = "Bonjour"


def Hello(name: str = None, language: str = None) -> str:
    """Hello returns a personalized greeting in a given language."""
    if not name:
        name = "World"

    if language == SPANISH:
        return f"{SPANISH_HELLO_PREFIX}, {name}"

    if language == FRENCH:
        return f"{FRENCH_HELLO_PREFIX}, {name}"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(Hello("world"))
