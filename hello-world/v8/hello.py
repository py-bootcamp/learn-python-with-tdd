spanish = "Spanish"
french = "French"
italian = "Italian"
englishHelloPrefix = "Hello"
spanishHelloPrefix = "Hola"
frenchHelloPrefix = "Bonjour"
italianHelloPrefix = "Ciao"


def prefix(language: str) -> str:
    prefix = englishHelloPrefix

    if language == spanish:
        prefix = spanishHelloPrefix

    if language == french:
        prefix = frenchHelloPrefix

    if language == italian:
        prefix = italianHelloPrefix

    return prefix


def Hello(name: str, language: str) -> str:
    """Hello returns a personalised greeting in a given language."""
    if not name:
        name = "World"

    return f"{prefix(language)}, {name}"


print(Hello("world", ""))
