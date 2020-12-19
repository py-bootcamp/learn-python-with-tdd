# Install Python

If Python is not already available on your system you can download Python from [here](https://www.python.org/downloads/).

## Installation

You can check whether Python is available on you system with this command \(from a terminal\):

```bash
$ python --version
Python 3.7.6
```

Any Python version &gt; `3.6` is good.

## Python Environment

### Python virtual environment

Citing the [Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments):

> Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally

and that's the approach with want to have, we will use `venv` to create a new Python virtual environment:

```bash
mkdir learn-python-with-tdd
cd learn-python-with-tdd
python -m venv .venv
```

Now we need to activate the environment

```bash
source .venv/bin/activate
```

To deactivate

```bash
deactivate
```

### Python dependencies

Python's dependencies are managed through [pip](https://packaging.python.org/tutorials/installing-packages/).

Once you created a new virtual environment and activated it, we can run

```bash
pip install pytest
```

[Pytest](https://docs.pytest.org/en/stable/) is a test runner, and the the only external dependency we need.

## Python Editor

Editors are like ice creams flavors, the choice is really personal and you'll have to find one that fits your need. If you don't have one I suggest you to check [VSCodium](https://github.com/VSCodium/vscodium), [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).

Both VSCodium and VSCode have a really good [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Refactoring and your tooling

A big emphasis of this book is around the importance of refactoring.

Your tools can help you do bigger refactoring with confidence.

You should be familiar enough with your editor to perform the following with a simple key combination:

* **Extract/Inline variable**. Being able to take magic values and give them a name lets you simplify your code quickly
* **Extract method/function**. It is vital to be able to take a section of code and extract functions/methods
* **Rename**. You should be able to confidently rename symbols across files.
* **Run tests**. It goes without saying that you should be able to do any of the above and then quickly re-run your tests to ensure your refactoring hasn't broken anything

In addition, to help you work with your code you should be able to:

* **View function signature** - You should never be unsure how to call a function in Python. Your IDE should describe a function in terms of its documentation, its parameters and what it returns.
* **View function definition** - If it's still not clear what a function does, you should be able to jump to the source code and try and figure it out yourself.
* **Find usages of a symbol** - Being able to see the context of a function being called can help your decision process when refactoring.

Mastering your tools will help you concentrate on the code and reduce context switching.

## Wrapping up

At this point you should have Python installed, an editor available and some basic tooling in place.

