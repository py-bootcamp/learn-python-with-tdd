# Lists

**[You can find all the code for this chapter here](https://github.com/py-bootcamp/learn-python-with-tdd/tree/master/lists)**

Lists allow you to store multiple elements of different types in a particular order.

When you have a lists, it is very common to have to iterate over them. So let's
use [our new-found knowledge of `for`](iteration.md) to make a `sum_numbers` function. `sum_numbers` will
take a list of numbers and return the total.

Let's use our TDD skills

## Write the test first

In `test_sum.py`

```python
from sum_numbers import sum_numbers


def test_sum():
    numbers = [1, 2, 3, 4, 5]

    got = sum_numbers(numbers)
    want = 15

    assert got == want
```

Lists are not fixed, you can add new elements dynamically. We can create a list in two ways:

```python
numbers = []
numbers = list()
```

## Try to run the test

By running `pytest -v .` the test will fail with `ModuleNotFoundError: No module named 'sum'`

## Write the minimal amount of code for the test to run and check the failing test output

In `sum_numbers.py`

```python
def sum_numbers(numbers):
    return 0
```

Your test should now fail with _a clear error message_

`assert 0 == 15`

## Write enough code to make it pass

```python
def sum_numbers(numbers):
	"Calculate the total from a list of numbers."
    total = 0

    for index, number in enumerate(numbers):
        total += numbers[index]

    return total
```

To get the value out of a list at a particular index, use `list[index]`
syntax. In this case, we are using `for` to iterate 5 times to work through the
list and add each item onto `total`.

## Refactor

While the first implementation of `sum_numbers` pass our test it's not really _idiomatic_.

It's rare to access list elements inside a loop with indexes in Python.
We can remove enumerate and use `for number in numbers`:

```python
def sum_numbers(numbers):
	"Calculate the total from a list of numbers."
    total = 0

    for number in numbers:
        total += number

    return total
```

the for-loop assign an item of `numbers` to `number` during each cycle.

The `for-in` works with any object that is [`iterable`](https://docs.python.org/3/glossary.html#term-iterable).


### Another refactor

We can make our function a bit more expressive by adding types:

```python
from typing import List


def sum_numbers(numbers: List[int]) -> int:
	"Calculate the total from a list of numbers."
    total = 0

    for number in numbers:
        total += number

    return total
```

`sum_numbers` accepts a list of numbers and return an integer.

## Extend our tests to cover an edge case

We want to extend our tests to cover two test cases:

- if the pass an empty list the sum should be zero
- `sum_numbers` should work also with `float`

```python
from sum_numbers import sum_numbers


def test_sum():
    numbers = [1, 2, 3, 4, 5]

    got = sum_numbers(numbers)
    want = 15

    assert got == want


def test_sum_empty_list():
    numbers = []

    got = sum_numbers(numbers)
    want = 0

    assert got == want


def test_sum_with_floats():
    numbers = [1.5, 2.0, 3.5]

    got = sum_numbers(numbers)
    want = 7.0

    assert got == want
```

Tests should still pass, well done!

## Refactor types

We added more tests and though we didn't change the implementation we just discovered that `sum_numbers` works also with `floats.`


```python
from typing import List


def sum_numbers(numbers: List[float]) -> float:
    total = 0.0

    for number in numbers:
        total += number

    return total
```

From a type perspective, `float` includes `int` (https://www.python.org/dev/peps/pep-0484/#id27),
so the new annotation says that `numbers` can be a list of floats or ints, and `sum_numbers` returns a float.

## Refactor tests

We had already refactored `sum_numbers` so there's not a lot to do here. Remember that we must not neglect our test code in the refactoring stage and we have some to do here.

```python
from sum_numbers import sum_numbers


def test_sum():
    numbers = [1, 2, 3, 4, 5]

    got = sum_numbers(numbers)
    want = 15

    assert got == want


def test_sum_empty_list():
    numbers = []

    got = sum_numbers(numbers)
    want = 0

    assert got == want


def test_sum_with_floats():
    numbers = [1.5, 2.0, 3.5]

    got = sum_numbers(numbers)
    want = 7.0

    assert got == want
```

It is important to question the value of your tests. It should not be a goal to
have as many tests as possible, but rather to have as much _confidence_ as
possible in your code base. Having too many tests can turn in to a real problem
and it just adds more overhead in maintenance. **Every test has a cost**.

In our case, you can see that having two tests for this function is redundant.
If it works for a list of ints it's very likely it'll work for a list of
any floats.

`Pytest` support test coverage with the plugin [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html), which can help identify areas of your code you have not covered. I do want to stress that having 100% coverage should not be your goal, it's just a tool to give you an idea of your coverage. If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway.

With your virtual environment active, try running

```bash
pip install pytest-cov
pytest --cov . -v .
```

You should see

```bash
test_sum.py::test_sum PASSED             [ 33%]
test_sum.py::test_sum_empty_list PASSED  [ 66%]
test_sum.py::test_sum_with_floats PASSED [100%]

---------- coverage: platform darwin, python 3.7.6-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
sum_numbers.py       6      0   100%
test_sum.py         16      0   100%
------------------------------------
TOTAL               22      0   100%
```

Now delete one of the tests and check the coverage again.

We can try to group tests together, using `parametrize`.

```python
import pytest
from sum_numbers import sum_numbers


@pytest.mark.parametrize(
    "numbers,want",
    [([1, 2, 3, 4.0, 5.0], 15), ([], 0)],
)
def test_sum_numbers(numbers, want):
    got = sum_numbers(numbers)
    assert got == want
```

`paramatrize` is really handy when you want to test a function and verify the behaviour comparing inputs and outputs. Using `parametrize` is similar to table driven tests.

`pytest` enriches the test output including each test case

```bash
test_sum.py::test_sum_numbers[numbers0-15] PASSED  [ 50%]
test_sum.py::test_sum_numbers[numbers1-0] PASSED   [100%]

---------- coverage: platform darwin, python 3.7.6-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
sum_numbers.py       6      0   100%
test_sum.py          5      0   100%
------------------------------------
TOTAL               11      0   100%
```

Now that we are happy we have a well-tested function you should commit your
great work before taking on the next challenge.

We need a new function called `sum_all` which will take a varying number of
lists, returning a new list containing the totals for each list passed in.

For example

`sum_all([1,2], [0,9])` would return `[3, 9]`

or

`sum_all([1, 1, 1])` would return `[3]`

## Write the test first

```python
def test_sum_all():
    got = sum_all([1, 2], [0, 9])
    want = [3, 9]

    assert got == want
```

## Try and run the test

`NameError: name 'sum_all' is not defined`

## Write the minimal amount of code for the test to run and check the failing test output

We need to define sum_all according to what our test wants.

Python can let you write [_variadic functions_](https://en.wikipedia.org/wiki/Variadic_function) that can take a variable number of arguments.

```python
def sum_all(*numbers_to_sum):
    return
```

It runs, but the test fails:

`assert None == [3, 9]`

`*numbers_to_sum` collects all the positional arguments that we use to call the `sum_all` function.

`numbers_to_sum` is a tuple that contains `[1, 2], [0, 9]`.

## Write enough code to make it pass

What we need to do is iterate over `numbers_to_sum`, calculate the sum using our
`sum_numbers` function from before and then add it to the list we will return

```python
def sum_all(*numbers_to_sum):
    sums = []

    for numbers in numbers_to_sum:
        result = sum_numbers(numbers)
        sums.append(result)

    return sums
```

Lots of new things to learn!

First we create an empty list with the `[]` notation. Then we loop over our collection of list of numbers.

We then `append` result, adding a new entry to the `sums` list.

The tests should now pass.

## Refactor

There are a few things we can improve in the `sum_all` function: we can add type annotations and use [list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

`List comprehensions provide a concise way to create lists`, we can generate and return the `sums` list directly

```python
def sum_all(*numbers_to_sum: List[float]) -> List[float]:
    return [sum_numbers(numbers) for numbers in numbers_to_sum]
```

Our next requirement is to change `sum_all` to `sum_all_tails`, where it now
calculates the totals of the "tails" of each list. The tail of a collection is
all the items apart from the first one \(the "head"\).

## Write the test first

```python
def test_sum_empty_tails():
    got = sum_all_tails([1, 2], [0, 9])
    want = [2, 9]

    assert got == want
```

## Try and run the test

`NameError: name 'sum_all_tails' is not defined`

## Write the minimal amount of code for the test to run and check the failing test output

Rename the function to `sum_all_tails` and re-run the test

`assert [3.0, 9.0] == [2, 9]`

## Write enough code to make it pass

```python
def sum_all_tails(*numbers_to_sum: List[float]) -> List[float]:
    return [sum_numbers(numbers[1:]) for numbers in numbers_to_sum]
```

Lists can be sliced! The syntax is `list[low:high]` If you omit the value on
one of the sides of the `:` it captures everything to the side of it. In our
case, we are saying "take from 1 to the end" with `numbers[1:]`. You might want to
invest some time in writing other tests around lists and experimenting with the
slice operator so you can be familiar with it.

## Refactor

Not a lot to refactor this time.

What do you think would happen if you passed in an empty list into our
function? What is the "tail" of an empty list? What happens when you tell Python to
capture all elements from `my_empty_list[1:]`?

## Write the test first

```python
def test_sum_empty_tails():
    got = sum_all_tails([], [])
    want = [0, 0]

    assert got == want
```

## Refactor

Our tests have some repeated code around assertion again, let's extract that into a function

```python
@pytest.mark.parametrize(
    "numbers_1,numbers_2,want",
    [([1, 2], [0, 9], [2, 9]), ([], [], [0, 0])],
)
def test_sum_all_tails(numbers_1, numbers_2, want):
    got = sum_all_tails(numbers_1, numbers_2)
    assert got == want
```

## Wrapping up

We have covered

* Lists
  * The various ways to make them
  * How you can _append` items to a list
  * How to slice, lists!
* Test coverage tool

We've used lists with integers and floats but they work with any other type
too, including lists. So you can list of lists of lists.

[Check out the Python documentation on lists][documentation-lists] for an in-depth look into
lists. Try writing more tests to demonstrate what you learn from reading it.

[for]: ../iteration.md#
[documentation-lists]: https://docs.python.org/3/library/stdtypes.html#lists
