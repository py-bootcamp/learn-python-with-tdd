# Hello, World

**[You can find all the code for this chapter here](https://github.com/py-bootcamp/learn-python-with-tdd/tree/master/hello-world)**

It is traditional for your first program in a new language to be [Hello, World](https://en.m.wikipedia.org/wiki/%22Hello,_World!%22_program).

In the [previous chapter](install-python.md#python-environment) we discussed how to setup your local enviroment.

Inside the `learn-python-with-tdd` folder make a directory in the following path `hello-world`, `learn-python-with-tdd/hello-world`.

So if you're on a unix based OS and you are happy to stick with Go's conventions about `$GOPATH` (which is the easiest way of setting up) you could run `mkdir -p learn-python-with-tdd/hello-world`.

For subsequent chapters, you can make a new folder with whatever name you like to put the code in e.g `$GOPATH/src/github.com/{your-user-id}/integers` for the next chapter might be sensible. Some readers of this book like to make an enclosing folder for all the work such as "learn-go-with-tests/hello". In short, it's up to you how you structure your folders.

Create a file in this directory called `hello.py` and write this code. To run it type `python hello.go`.

```python
print("Hello World")
```

## How it works

Python programs end in `*.py`, `print` is a built-in function, always available without need to import it.

## How to test

How do you test this? It is good to separate your "domain" code from the outside world \(side-effects\). The `print` is a side effect \(printing to a text stream file\) and the string we send in is our domain.

So let's separate *these concerns* so it's easier to test

```python
def Hello() -> str:
    """Hello returns a greeting."""
    return "Hello, world"


print(Hello())
```

We have created a new function again with `def` called `Hello`, this function doesn't accept any parameter but returns a string. This means this function returns a `string`.

Python is a dynamically-typed language, while types are optionals and not used at runtime the help understing your code.

Now create a new file called `hello_test.py` where we are going to write a test for our `Hello` function

```python
from .hello import Hello


def test_hello():
    got = Hello()
    want = "Hello, world"

    assert got == want
```

Before explaining, let's just run the code. Run `pytest` in your terminal. It should've passed! Just to check, try deliberately breaking the test by changing the `want` string.
