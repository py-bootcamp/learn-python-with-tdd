englishHelloPrefix = "Hello"


def Hello(name: str) -> str:
    """Hello returns a personalised greeting, defaulting to Hello, world if an empty name is passed."""
    if not name:
        name = "World"

    return f"{englishHelloPrefix}, {name}"


print(Hello("world"))
