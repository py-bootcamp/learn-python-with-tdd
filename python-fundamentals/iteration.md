# Iteration

[**You can find all the code for this chapter here**](https://github.com/py-bootcamp/learn-python-with-tdd/tree/main/for)

To do stuff repeatedly in Python, you'll need `for` or `while`.

Let's write a test for a function that repeats a character 5 times.

There's nothing new so far, so try and write it yourself for practice.

## Write the test first

```python
from repeat import repeat


def test_repeat():
    got = repeat("a")
    want = "aaaaa"

    assert got == want
```

## Try and run the test

`ModuleNotFoundError: No module named 'repeat'`

## Write the minimal amount of code for the test to run and check the failing test output

_Keep the discipline!_ You don't need to know anything new right now to make the test fail properly.

All you need to do right now is enough to make it compile so you can check your test is written well.

```python
def repeat(character: str) -> str:
    """Repeat returns character repeated 5 times."""
    return ""
```

Isn't it nice to know you already know enough Python to write tests for some basic problems? This means you can now play with the production code as much as you like and know it's behaving as you'd hope.

`AssertionError: assert '' == 'aaaaa'`

## Write enough code to make it pass

The `for` syntax is bit different compared to most C-like languages.

You don't have to create counters and increase them, you can use `range`.

```python
def repeat(character: str) -> str:
    """Repeat returns character repeated 5 times."""
    word = ""
    for counter in range(5):
        word = word + character

    return word
```

Unlike other languages like C, Java, or JavaScript there are no braces, Python uses `indentation`.

You might wonder what is happening in the row

```python
    for counter in range(5):
```

`range` returns an iterator, when you consume an iterator you get an element of the iterator.

In this case that line can be translated to

```python
    for counter in [0, 1, 2, 3, 4]:
```

during every cycle of the loop `counter` get assigned an element: 0, 1, 2 and so on.

Once we consumed all the element \(when the iterator is _exhausted_\) we exit the loop.

That's pretty neat! compared to other languages

```go
    for i := 0; i < 5; i++
```

Python can be more _expressive_.

Run the test and it should pass.

If you want to learn more about the for loop you can check [here](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement).

## Refactor

Now it's time to refactor and introduce another construct `+=` assignment operator.

```python
COUNTER: int = 5

def repeat(character: str) -> str:
    """Repeat returns character repeated 5 times."""
    word = ""
    for counter in range(COUNTER):
        word += character

    return word
```

`+=` called _"the Add AND assignment operator"_, adds the right operand to the left operand and assigns the result to left operand. It works with other types like integers.

### Extending repeat functionalities

We want to extend allow the caller to specify how many times the character is repeated:

```python
def test_repeat():
    got = repeat("a", 4)
    want = "aaaa"

    assert got == want
```

Test is failing, let's fix it!

### One last refactor

Python support operator _overloading_. Operators, like `+` or `*`, can have a different behaviour depending on the type of the operands. While `a * 5` doesn't have an arithmetical sense, in Python it does and it repeats `a` five times.

```python
def repeat(character: str, counter: int) -> str:
    """Repeat returns character repeated `counter` times."""
    return character * counter
```

## Practice exercises

* Have a look through the [What is the most efficient way to concatenate many strings together?](https://docs.python.org/3/faq/programming.html#what-is-the-most-efficient-way-to-concatenate-many-strings-together). Try to refactor the code to implement the suggested idiomatic ways.

## Wrapping up

* More TDD practice
* Learned `for`
* Learned about `operator overloading`

