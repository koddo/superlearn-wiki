---
title:   "Exceptions"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# exceptions

<https://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program>
<https://docs.python.org/3/library/traceback.html>
<https://stackoverflow.com/questions/34046703/does-python-traceback-print-exc-prints-to-stdout-or-stderr>

``` Python
# http://stackoverflow.com/questions/1611561/can-i-get-the-exception-from-the-finally-block-in-python/1611572#1611572
try:
    whatever
except:
    here sys.exc_info is valid
    to re-raise the exception, use a bare `raise`
else:
    here you know there was no exception
finally:
    and here you can do exception-independent finalization
```


``` Python
# The exception variable is excplicitly deleted after the except block is left.

except E as N:
    foo

# equivalent 

except E as N:
    try:
        foo
    finally:
        del N
```

Exception objects now store their traceback as the `__traceback__` attribute. This means that an exception object now contains all the information pertaining to an exception, and there are fewer reasons to use `sys.exc_info()` (though the latter is not removed).

``` Python
# http://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program/16946886#16946886
import traceback

try:
    raise TypeError("Oups!")
except Exception as err:
    try:
        raise TypeError("Again !?!")
    except:
        pass

    # traceback.print_tb(err.__traceback__)
    traceback.print_exc()

 ### File "e3.py", line 4, in <module>
 ###    raise TypeError("Oups!")
```

``` Python
def func1():
    try:
        return 1
    finally:
        return 2

def func2():
    try:
        raise ValueError()
    except:
        return 1
    finally:
        return 3

func1()   # returns 2
func2()   # returns 3
```

``` Shell
>>> try:
...     print(1 / 0)
... except Exception as exc:
...     raise RuntimeError("Something bad happened") from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: int division or modulo by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
```

``` Python
try:
    self.file = open(filename)
except IOError as e:
    raise DatabaseError('failed to open') from e
```

``` Python
class MyError(Exception):
    """Raise for my specific kind of exception"""
```

``` Python
class Error():
    pass

class InputError(Error):
    def __init__(self, message, expression):
        self.message = message
        self.expression = expression
```

``` Python
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32
```


``` python
from contextlib import suppress
import os
with suppress(FileNotFoundError):
    print(1')
    os.remove('1.tmp')
    os.remove('2.tmp')
    print(2')
```

<https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions>
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>

<https://hg.python.org/cpython/file/3.5/Objects/exceptions.c#l24>

TODO: - q: Write a custom exception class with a value besides message in a portable manner: <http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python> 


TODO: with statement, contextlib
TODO: with pytest.raises(ExpectedException) <http://doc.pytest.org/en/latest/assert.html>
TODO: more from <https://docs.python.org/3/library/traceback.html>


## basics

``` Python
raise ValueError
raise ValueError('Some message')
raise ValueError('Some message', 100)
raise CustomError(100)
raise
raise CustomError from e
```


``` Python
while True:
    try:
        1/0
    except:
        raise
    finally:
        break     # discards the exception

print('hell')     # it does print indeed
```

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- exceptions">
    <p>Your browser does not support iframes.</p>
</iframe>


## custom exception classes

``` Python
class MyError(ValueError):
    def __init__(self, message, field):
        self.message = message
        self.field = field
```

Generally it's a good idea to look for an appropriate existing exception first.

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- custom exceptions">
    <p>Your browser does not support iframes.</p>
</iframe>

## ignoring exceptions

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- ignoring exceptions">
    <p>Your browser does not support iframes.</p>
</iframe>

# built-in exceptions

ArithmeticError --> 

AttributeError --- x.attr, None.attr
TypeError --- None[0]
ValueError --- int('a')
LookupError --> IndexError, KeyError --- l[10]; d['b']

StopIteration
GeneratorExit



## traceback

- q: What is exception chaining? --- a: `except ValueException as exc: raise RuntimeError("Something bad happened") from exc` --- this will give a nice trace back which mentions that `ValueException` is a direct cause of the `RuntimeError("Something bad happened")`. And we have `exc.__cause__`.
- q: What are `exception.__context__` and `exception.__cause__`? --- a: When raising (or re-raising) an exception in an `except` or `finally` clause `__context__` is automatically set to the last exception caught. `raise new_exc from original_exc` sets `new_exc.__cause__`.
- q: How to print traceback of an exception? --- a: In the except block: `traceback.print_exc()`
- q: How to log traceback of an exception? --- a: Use `traceback.format_exc()` and your favorite logger.

## asserts

- q: What is `assert` for? --- a: Asserts should be used to test conditions that should never happen. The purpose is to crash early in the case of a corrupt program state. They add a tiny overhead, but before making a program fast we have to make it work first. And we can turn asserts off when needed with `-O` flag.
- q: What does `assert` do? --- a: `assert cond, message` is roughly equivalent to `if __debug__ and not cond: raise AssertionError(message)`
- q: What happens here? `assert( 2+2==5, 'Houston, we have a problem' )` --- a: `assert`, unlike `print`, which is a function, is still a statement, so this is equivalent to `assert True`, because syntactically we have a non-empty tuple here. Good news is python and lint gives you warning for this.



# sigint

``` Python
def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
```

To ignore the SIGINT:

``` Python
signal.signal(signal.SIGINT, signal.SIG_IGN)
```

