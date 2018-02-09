---
title:   "Basics"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}

# True, False, and comparisons

``` python
if () or [] or {} or None or 0 or '':
    'this line is skipped'
```

From <https://docs.python.org/3/library/stdtypes.html#truth-value-testing>:
> Considered false: instances with `__bool__()` returning False or `__len__()` returning zero. Built-ins:
> - `False`, `None`
> - zeroes of any numeric type: `0`, `0.0`, `Decimal(0)`, `Fraction(0, 1)`, `0j`
> - empty sequences and collections: `''`, `()`, `[]`, `{}`, `{}`, `set()`, `range(0)`

As in many languages, `and` and `or` are short-circuit operators, second argument is not evaluated here:
``` python
if False and whatever():
    'this line is skipped, whatever() is not evaluated'
```

Comparison operators look quite standard: `==`, `!=` (`<>` was removed from the language), `<`, `>`, `<=`, `>=`. And for object identity: `is`, `is not`.
> Behavior of the `is` and `is not` operators cannot be customized; also they can be applied to any two objects and never raise an exception.

Objects of different _built-in_ types never compare equal (except different numeric types), e.g., `'1' == 1` is false. `<`, `>`, `<=`, `>=` raise `TypeError` exception when the objects are of different types that cannot be compared.
``` python
>>> 'abc' > 1000
TypeError: unorderable types: str() > int()
```

`x < y < z` is equivalent to `x < y and y < z`, except `y` is evaluated only once. In both cases `z` is not evaluated at all when `x < y` is found to be false

Most importantly:

Use `if x`. Rarely `if x == True and type(x) is bool` when needed. Never `if x is True`, because `bool` is a subclass of `int`, this fails in obscure cases.

Same for `not x` and `False`.

An edge case is comparison to `None`. Use `if x is None`, never `x == None`. From [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations):
> Comparisons to singletons like None should always be done with is or is not , never the equality operators. 

Good:
```
if x:
  ...
if not x:
  ...
if x == True and type(x) is bool:
  ...
if x == False and type(x) is bool:
  ...
if x is None:
  ...
```

Bad:

```
if x is True:
  ...
if x is False:
  ...
if x == True:
  ...
if x == False:
  ...
if x == None:
  ...
```

There is a thing in python, operator chaining. It's for things like `x < y < z`, which is roughly equivalent to `x < y and y < z`. \\
Except `y` is evaluated only once here. \\
Btw, in both cases `z` is not evaluated at all when `x < y` is false. \\
Be careful, with operator chaining, `1 == 1 in [1]` is unreadable and it's not obvios that it's an operator chaining.

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20true,%20false,%20and%20comparisons">
    <p>Your browser does not support iframes.</p>
</iframe>

TODO: `True + 1 == 2`, `False + 1 == 0`
TODO: <https://github.com/satwikkansal/wtfpython#-be-careful-with-chained-operations>

TODO: <http://canonical.org/~kragen/isinstance/>
<https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python>
- q: `type(s) is str` vs `type(s) == str` vs `isinstance(s, str)` -- a: Virtually no difference between `is` and `==` here, but people tend to use `is`. Type comparison answers the strict question: is this a type of object. `isinstance(o, cls)` considers type hierarcy.

<br />
<br />


# identity

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20identity">
    <p>Your browser does not support iframes.</p>
</iframe>


# functions

<https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions>

<http://effbot.org/zone/default-values.htm>
<https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument>
<https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules>

<https://docs.python.org/2/library/functions.html#apply>
Deprecated since version 2.3: Use function(*args, **keywords) instead of apply(function, args, keywords) (see Unpacking Argument Lists).

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20functions">
    <p>Your browser does not support iframes.</p>
</iframe>


# lambda

No return statement in lambdas: <https://docs.python.org/3/reference/expressions.html#lambda>

<https://stackoverflow.com/questions/862412/is-it-possible-to-have-multiple-statements-in-a-python-lambda-expression>
just use a tuple: `lambda x: ( f(x), g(x) )`

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20lambda">
    <p>Your browser does not support iframes.</p>
</iframe>


