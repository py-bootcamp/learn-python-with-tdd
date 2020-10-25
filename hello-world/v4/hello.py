englishHelloPrefix = "Hello"


def Hello(name: str) -> str:
    """Hello returns a personalised greeting."""
    return f"{englishHelloPrefix}, {name}"


print(Hello("world"))
