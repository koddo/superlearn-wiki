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

except E as e:
    foo

# equivalent 

except E as e:
    try:
        foo
    finally:
        del e
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
    print('1')
    os.remove('1.tmp')
    os.remove('2.tmp')
    print('2')
```

<https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions>
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>

<https://hg.python.org/cpython/file/3.5/Objects/exceptions.c#l24>


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

<https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>:

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

# `with` statement

<https://docs.python.org/3/reference/compound_stmts.html#the-with-statement>

<http://www.dan-gittik.com/post/deconstructing-context-managers>
<https://pymotw.com/3/contextlib/index.html>

``` Python
try:
    f = open("document.txt")
except FileNotFoundError:
    print("document.txt file is missing")
except PermissionError:
    print("You are not allowed to read document.txt")
else:
    try:
        with f:
            content = f.read()
    except Exception:
        ...

try:
    f = open(my_file)

    try:
        do_stuff_that_fails()
    except EXPECTED_EXCEPTION_TYPES as e:
        do_stuff_when_it_doesnt_work()
    finally:
        f.close()
except (IOError, OSError) as e:
    do_other_stuff_when_it_we_have_file_IO_problems()
    
try:
    file = open(...)
except OpenErrors...:
    # handle open exceptions
else:
    try:
        # do stuff with file
    finally:
        file.close()
```

``` Python
with open('filename') as f:
    ...
    
f = open('filename')
try:
    ...
finally:
    f.close()
```


``` Python
with A() as a, B() as b:
    suite

with A() as a:
    with B() as b:
        suite
```

TODO: - q: How to write a custom context manager?
<https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator>
<https://docs.python.org/3/library/contextlib.html#using-a-context-manager-as-a-function-decorator>

We can write custom context managers as classes or as @contextmanager decorated functions.

``` Python
@contextmanager
def chdir(dir):
    cwd = os.getcwd()
    try:
        os.chdir(dir)
        yield
    finally:
        os.chdir(cwd)
        
with chdir('/tmp'):
    print(os.getcwd())
```

Another example:

``` Python
@contextmanager
def closing(thing):    # equivalent to contextlib.closing
    try:
        yield thing
    finally:
        thing.close()
        
with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)
```


``` Python
with open() as a, open() as b, open() as c:
    ...

with contextlib.ExitStack as stack:
    a = stack.enter_context(open())
    b = stack.enter_context(open())
    c = stack.enter_context(open())
    ...
```

But it's not too benefitial that way. It really shines when you want to have nested contexts of a depth unknown in advance.

``` Python
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    ...
```

``` Python
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    stack_opened = stack.pop_all()
    
with stack_opened:
    ...
```

``` Python
with ExitStack() as stack:
    tempdirs = []
    for i in range(3):
        tempdir = tempfile.mkdtemp()
        stack.callback(shutil.rmtree, tempdir)
        tempdirs.append(tempdir)
    # Do something with the tempdirs
```



<https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack>
<https://www.wefearchange.org/2013/05/resource-management-in-python-33-or.html>
<https://www.rath.org/on-the-beauty-of-pythons-exitstack.html>


`contextlib.closing`

``` Python
with contextlib.suppress(NotFoundError):
    ...

try:
    ...
except NotFoundError:
    pass
```

Beware though, the following code will ignore the second line after an exception in the first one:

``` Python
with suppress(FileNotFoundError):
    os.remove('1.tmp')       # exception here
    os.remove('2.tmp')       # this line not run
```

<https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout>
<https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stderr>

`contextlib.redirect_stdout` and `contextlib.redirect_stderr`

<https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/>

Mostly for utility scripts. Not suitable for use in library code and most threaded applications. It also has no effect on the output of subprocesses.

``` Python
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
```

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- with statement">
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



# traceback

- q: What is exception chaining? --- a: `except ValueException as exc: raise RuntimeError("Something bad happened") from exc` --- this will give a nice trace back which mentions that `ValueException` is a direct cause of the `RuntimeError("Something bad happened")`. And we have `exc.__cause__`.
- q: What are `exception.__context__` and `exception.__cause__`? --- a: When raising (or re-raising) an exception in an `except` or `finally` clause `__context__` is automatically set to the last exception caught. `raise new_exc from original_exc` sets `new_exc.__cause__`.
- q: How to print traceback of an exception? --- a: In the except block: `traceback.print_exc()`
- q: How to log traceback of an exception? --- a: Use `traceback.format_exc()` and your favorite logger.

# asserts

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










