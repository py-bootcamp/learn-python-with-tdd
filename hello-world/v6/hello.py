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

    if language == spanish:
        return f"{spanishHelloPrefix}, {name}"

    if language == french:
        return f"{frenchHelloPrefix}, {name}"

    if language == italian:
        return f"{italianHelloPrefix}, {name}"

    return f"{englishHelloPrefix}, {name}"


print(Hello("world", ""))
