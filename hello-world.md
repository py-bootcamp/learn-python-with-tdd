# Hello, World

[**You can find all the code for this chapter here**](https://github.com/py-bootcamp/learn-python-with-tdd/tree/master/hello-world)

It is traditional for your first program in a new language to be [Hello, World](https://en.m.wikipedia.org/wiki/%22Hello,_World!%22_program).

In the [previous chapter](install-python.md#python-environment) we discussed how to setup your local environment.

It's time to create a new folder for our project.

So if you're on a unix based OS and you could run `mkdir -p learn-python-with-tdd/hello-world`.

For subsequent chapters, you can make a new folder with whatever name you like to put the code in e.g `learn-python-with-tdd/integers` for the next chapter might be sensible. it's up to you how you structure your folders.

Create a file in this directory called `hello.py` and write this code. To run it type `python hello.py`.

```python
print("Hello World")
```

## How it works

Python programs end in `*.py`, `print` is a built-in function, always available without having to import it.

## How to test

How do you test this? It is good to separate your _domain_ code from the outside world \(side-effects\). The `print` is a side effect \(printing to a text stream file\) and the string we send in is our domain.

So let's separate _these concerns_ so it's easier to test

```python
def hello() -> str:
    """Return a greeting."""
    return "Hello, world"


print(hello())
```

We have created a new function with `def` called `hello`, this function doesn't accept any parameter but returns a `string` \(str\).

> Python is a dynamically-typed language, while types are optionals and not used at runtime they help describing your code.

On line 2 we have a docstring, which is how you can document your code in Python.

Now create a new file called `hello_test.py` where we are going to write a test for our `hello` function

```python
from hello import hello


def test_hello():
    got = hello()
    want = "Hello, world"

    assert got == want
```

Before explaining, let's just run the code. Run `pytest` in your terminal. It should've passed! Just to check, try deliberately breaking the test by changing the `want` string.

### Writing tests

Writing a test is just like writing a function, with a few rules

* It needs to be in a file with a name like `xxx_test.py` or `test_xxx.py`
* The test function must start with the word `test`

We've covered some new topics:

#### Imports

`from hello import hello` imports the `hello` function from the `hello.py` inside our test file.

#### Declaring variables

We're declaring some variables with the syntax `var_name = value`, which lets us re-use some values in our test for readability.

#### Assertions

We are calling the `assert` statement. `assert` is a reserved keyword in Python, you can't type `assert = 1`. `assert` evaluates the condition `got == want` and if it's false raises an error.

In the test above we are evaluating that both strings are the same.

### Hello, YOU

Now that we have a test we can iterate on our software _safely_. We can improve `def hello()` or add new functionalities while being sure that old features work the same way.

In the last example we wrote the test _after_ the code had been written just so you could get an example of how to write a test and declare a function. From this point on we will be _writing tests first_.

Our next requirement is to let us specify the recipient of the greeting.

Let's start by capturing these requirements in a test. This is basic test driven development and allows us to make sure our test is _actually_ testing what we want. When you retrospectively write tests there is the risk that your test may continue to pass even if the code doesn't work as intended.

```python
from hello import hello


def test_hello():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want
```

Now run `pytest`, you should have an error

```text
    def test_hello():
>       got = hello("Christian")
E       TypeError: hello() takes 0 positional arguments but 1 was given
```

Python provides great error messages. In this case Python is telling you what you need to do to continue. We have to change our function `Hello` to accept an argument.

Edit the `hello` function to accept an argument of type str \(string\)

```python
def hello(name: str) -> str:
    """Return a greeting."""
    return "Hello, world"
```

If you try and run `python hello.py` will fail because you're not passing an argument. Send in "world" to make it pass.

```python
print(hello("world"))
```

Now when you run your tests you should see something like

```text
AssertionError: assert 'Hello, world' == 'Hello, Christian'
```

We finally have a working program but it is not meeting our requirements according to the test.

Let's make the test pass by interpolating the parameter `name` inside the return

```python
def hello(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}"
```

When you run the tests they should now pass. Normally as part of the TDD cycle we should now _refactor_.

### A note on source control

At this point, if you are using source control \(which you should!\) I would `commit` the code as it is. We have working software backed by a test.

I _wouldn't_ push to master though, because I plan to refactor next. It is nice to commit at this point in case you somehow get into a mess with refactoring - you can always go back to the working version.

There's not a lot to refactor here, but we can introduce another language feature, _constants_.

### Constants

You can't really define constants in Python, but there's a convention on how to represent variables that are meant to be constant: `all capital letters with underscores separating words` \([more here](https://www.python.org/dev/peps/pep-0008/#constants)\)

We can now refactor our code

```python
ENGLISH_HELLO_PREFIX = "Hello"


def hello(name: str) -> str:
    """Return a personalized greeting."""
    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

After refactoring, re-run your tests to make sure you haven't broken anything.

## Hello, world... again

The next requirement is when our function is called with an empty string it defaults to printing "Hello, World", rather than "Hello, ".

Start by writing a new failing test

```python
def test_hello_without_name():
    got = hello()
    want = "Hello, World"

    assert got == want

def test_hello_with_name():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want
```

Now that we have a well-written failing test, let's fix the code, using an `if`.

```python
ENGLISH_HELLO_PREFIX = "Hello"


def hello(name: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

The function signature is different!

`name: str = None` tells Python that in case we don't pass a value for `name` when we call the function we should use `None` as default.

If we run our tests we should see it satisfies the new requirement and we haven't accidentally broken the other functionality.

### Back to source control

Now we are happy with the code I would amend the previous commit so we only check in the lovely version of our code with its test.

### Discipline

Let's go over the cycle again

* Write a test
* Run the test, see that it fails and check the error message is meaningful
* Write enough code to make the test pass
* Refactor

On the face of it this may seem tedious but sticking to the feedback loop is important.

Not only does it ensure that you have _relevant tests_, it helps ensure _you design good software_ by refactoring with the safety of tests.

Seeing the test fail is an important check because it also lets you see what the error message looks like. As a developer it can be very hard to work with a codebase when failing tests do not give a clear idea as to what the problem is.

By ensuring your tests are _fast_ and setting up your tools so that running tests is simple you can get in to a state of flow when writing your code.

By not writing tests you are committing to manually checking your code by running your software which breaks your state of flow and you won't be saving yourself any time, especially in the long run.

## Keep going! More requirements

Goodness me, we have more requirements. We now need to support a second parameter, specifying the language of the greeting. If a language is passed in that we do not recognize, just default to English.

We should be confident that we can use TDD to flesh out this functionality easily!

Write a test for a user passing in Spanish. Add it to the existing suite.

```python
def test_hello_in_spanish():
    got = hello("Christian", "Spanish")
    want = "Hola, Christian"

    assert got == want
```

Remember not to cheat! _Test first_. When you try and run the test, Python _should_ complain because you are calling `hello` with two arguments rather than one.

```text
    def test_hello_in_spanish():
>       got = hello("Christian", "Spanish")
E       TypeError: hello() takes from 0 to 1 positional arguments but 2 were given
```

Fix the problems by adding another string argument to `def hello`

```python
def hello(name: str = None, language: str) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

Docstrings should follow function's behaviors, this is a good time to update function's docstring.s

When you run the test again it will complain again about the order of the parameters in our `hello` function

```text
E       def hello(name: str = None, language: str) -> str:
E                ^
E   SyntaxError: non-default argument follows default argument
```

We can fix this error by making `language` optional as well

```python
def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

Now all your tests should pass, apart from our new scenario

```text
AssertionError: assert 'Hello, Christian' == 'Hola, Christian'
```

We can use `if` here to check the language is equal to "Spanish" and if so change the message

```python
def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    if language == "Spanish":
        return f"Hola, {name}"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

The tests should now pass.

Now it is time to _refactor_. You should see some problems in the code, "magic" strings, some of which are repeated. Try and refactor it yourself, with every change make sure you re-run the tests to make sure your refactoring isn't breaking anything.

```python
SPANISH = "Spanish"
ENGLISH_HELLO_PREFIX = "Hello"
SPANISH_HELLO_PREFIX = "Hola"


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    if language == SPANISH:
        return f"{SPANISH_HELLO_PREFIX}, {name}"

    return f"{ENGLISH_HELLO_PREFIX}, {name}"
```

### French

* Write a test asserting that if you pass in `"French"` you get `"Bonjour, "`
* See it fail, check the error message is easy to read
* Do the smallest reasonable change in the code

You may have written something that looks roughly like this

```python
def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    prefix = ENGLISH_HELLO_PREFIX

    if language == SPANISH:
        prefix = SPANISH_HELLO_PREFIX

    if language == FRENCH:
        prefix = FRENCH_HELLO_PREFIX

    return f"{prefix}, {name}"
```

## `Dict`

When you have lots of `if` statements checking a particular value and returning it is common to use a `dictionary` to hold values. A dictionary is a collection of keys/values. We can use a `dictionary` to refactor the code to make it easier to read and more extensible if we wish to add more language support later

```python
ENGLISH_HELLO_PREFIX = "Hello"
LANGUAGES = {
    "Spanish": "Hola",
    "French": "Bonjour",
}


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    prefix = LANGUAGES.get(language, ENGLISH_HELLO_PREFIX)

    return f"{prefix}, {name}"
```

A dictionary offers lots of handy functionalities, in this case we are using the `get` method look for a key \(`language`\) and in case is not available return a default \(`ENGLISH_HELLO_PREFIX`\).

Write a test to now include a greeting in the language of your choice and you should see how simple it is to extend our _amazing_ function.

### one...last...refactor?

You could argue that maybe our function is getting a little big. The simplest refactor for this would be to extract out some functionality into another function.

```python
def prefix(language: str) -> str:
    return LANGUAGES.get(language, ENGLISH_HELLO_PREFIX)


def hello(name: str = None, language: str = None) -> str:
    """Return a personalized greeting.
    Defaulting to `Hello, World` if no name and language are passed.
    """
    if not name:
        name = "World"

    return f"{prefix(language)}, {name}"
```

### one....really...last refactor?

If you look at tests you can see that some of them a replicated....usually that's a good sign for a refactor.

Sometimes it is useful to group tests around a "thing" and then have parameters describing different scenarios.

A benefit of this approach is you can set up shared code that can be used in the other tests.

Refactoring is not _just_ for the production code!

It is important that your tests _are clear specifications_ of what the code needs to do.

We can and should refactor our tests.

```python
import pytest

from hello import hello


def test_hello_without_name():
    got = hello()
    want = "Hello, World"

    assert got == want


def test_hello_with_name():
    got = hello("Christian")
    want = "Hello, Christian"

    assert got == want


@pytest.mark.parametrize(
    "name, language, want",
    [
        ("Elodie", "Spanish", "Hola, Elodie"),
        ("Lauren", "French", "Bonjour, Lauren"),
        ("Alice", None, "Hello, Alice"),
    ],
)
def test_hello_with_name_and_language(name, language, want):
    got = hello(name, language)

    assert got == want
```

What have we done here?

We refactored test with `parametrize`, a way to parametrize your test using a collection of values.

`parametrize` is a utils coming from the `pytest` suite, it reduces duplication by running the same test with different parameters.

## Wrapping up

Who knew you could get so much out of `Hello, world`?

By now you should have some understanding of:

### Some of Python's syntax around

* Writing tests
* Declaring functions, with arguments and return types
* `if`, `dictionary` and `parametrize`
* Declaring variables and constants

### The TDD process and _why_ the steps are important

* _Write a failing test and see it fail_ so we know we have written a _relevant_ test for our requirements and seen that it produces an _easy to understand description of the failure_
* Writing the smallest amount of code to make it pass so we know we have working software
* _Then_ refactor, backed with the safety of our tests to ensure we have well-crafted code that is easy to work with

In our case we've gone from `hello()` to `hello("name")`, to `hello("name", "French")` in small, easy to understand steps.

This is of course trivial compared to "real world" software but the principles still stand. TDD is a skill that needs practice to develop but by being able to break problems down into smaller components that you can test you will have a much easier time writing software.

