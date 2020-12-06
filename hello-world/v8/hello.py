ENGLISH_HELLO_PREFIX = "Hello"
LANGUAGES = {
    "Spanish": "Hola",
    "French": "Bonjour",
}


def prefix(language: str) -> str:
    return LANGUAGES.get(language, ENGLISH_HELLO_PREFIX)


def Hello(name: str = None, language: str = None) -> str:
    """Hello returns a personalized greeting.
    Defaulting to Hello, world if an empty name is passed.
    """
    if not name:
        name = "World"

    return f"{prefix(language)}, {name}"


print(Hello("world", ""))
