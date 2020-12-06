ENGLISH_HELLO_PREFIX = "Hello"


def Hello(name: str = None) -> str:
    """Hello returns a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(Hello("world"))
