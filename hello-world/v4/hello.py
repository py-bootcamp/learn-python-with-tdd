ENGLISH_HELLO_PREFIX = "Hello"


def hello(name: str) -> str:
    """Return a personalized greeting."""
    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(hello("world"))
