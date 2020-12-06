ENGLISH_HELLO_PREFIX = "Hello"


def hello(name: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(hello("world"))
