spanish = "Spanish"
french = "French"
italian = "Italian"
englishHelloPrefix = "Hello"
spanishHelloPrefix = "Hola"
frenchHelloPrefix = "Bonjour"
italianHelloPrefix = "Ciao"


def Hello(name: str, language: str) -> str:
    """Hello returns a personalised greeting in a given language."""
    if not name:
        name = "World"

    prefix = englishHelloPrefix

    if language == spanish:
        prefix = spanishHelloPrefix

    if language == french:
        prefix = frenchHelloPrefix

    if language == italian:
        prefix = italianHelloPrefix

    return f"{prefix}, {name}"


print(Hello("world", ""))
