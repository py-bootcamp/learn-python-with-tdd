ENGLISH_HELLO_PREFIX = "Hello"


def Hello(name: str = None) -> str:
    """
    Hello returns a personalized greeting.
    Defaulting to Hello, world if an empty name is passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(Hello("world"))
