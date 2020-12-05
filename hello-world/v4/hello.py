ENGLISH_HELLO_PREFIX = "Hello"


def Hello(name: str) -> str:
    """Hello returns a personalized greeting."""
    return f"{ENGLISH_HELLO_PREFIX}, {name}"


print(Hello("world"))
