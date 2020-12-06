# Integers

**[You can find all the code for this chapter here](https://github.com/py-bootcamp/learn-python-with-tdd/tree/main/integers)**

Integers work as you would expect. Let's write an `add` function to try things out. Create a test file called `test_adder.py` and write this code.

## Write the test first

```python
from adder import add


def test_add():
    sum = add(2, 2)
    expected = 4

    assert sum == expected
```

## Try and run the test

Run the test `pytest`

Inspect the error

```text
test_adder.py:1: in <module>
    from adder import add
E   ModuleNotFoundError: No module named 'adder'
```

## Write the minimal amount of code for the test to run and check the failing test output

Write enough code to satisfy the compiler _and that's all_ - remember we want to check that our tests fail for the correct reason.

```python
def add(x: int, y: int) -> int:
    return 0
```

We have a new type here: `int`.

Now run the tests and we should be happy that the test is correctly reporting what is wrong.

`assert 0 == 4`

## Write enough code to make it pass

In the strictest sense of TDD we should now write the _minimal amount of code to make the test pass_. A pedantic programmer may do this

```python
def add(x: int, y: int) -> int:
    return 4
```

Ah hah! Foiled again, TDD is a sham right?

We could write another test, with some different numbers to force that test to fail but that feels like [a game of cat and mouse](https://en.m.wikipedia.org/wiki/Cat_and_mouse).

Once we're more familiar with Python's syntax I will introduce a technique called *"Property Based Testing"*, which would stop annoying developers and help you find bugs.

For now, let's fix it properly

```python
def add(x: int, y: int) -> int:
    return x + y
```

If you re-run the tests they should pass.

## Refactor

There's not a lot in the _actual_ code we can really improve on here.

We explored earlier the value of doing type annotations (putting `str` and `int`) in the documentation.

This is great because it aids the usability of code you are writing. It is preferable that a user can understand the usage of your code by just looking at the type signature and documentation.

```python
def add(x: int, y: int) -> int:
    """Take two integers and returns the sum of them."""
    return x + y
```

## Wrapping up

What we have covered:

* More practice of the TDD workflow
* Integers, addition
* Writing better documentation so users of our code can understand its usage quickly
