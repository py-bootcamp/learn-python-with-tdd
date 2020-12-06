ENGLISH_HELLO_PREFIX = "Hello"
LANGUAGES = {
    "Spanish": "Hola",
    "French": "Bonjour",
}


def prefix(language: str) -> str:
    return LANGUAGES.get(language, ENGLISH_HELLO_PREFIX)


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{prefix(language)}, {name}"


print(hello("world", ""))
