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

{% comment %}
- q: What values are considered false in python? --- a: `False`, `None`, any numeric zero, empty sequence, empty dict, instance with `__bool__()` returning False or `__len__()` returning zero
- q: What is short-circut behavior of boolean operators `and`, `or`. --- a: `if False and whatever(): 'this line is skipped, whatever() is not evaluated'`
- q: `x < y <= z` vs `x < y and y <= z` --- a: `x < y <= z` is pretty much equivalent to `x < y and y <= z`, except `y` is evaluated only once, and in both cases `z` is not evaluated at all when `x < y` is found to be false
- q: What are equal and not equal operators? --- a: `==`, `!=`
- q: What is `<>`? --- a: It's a _not equal_ opearator in older python versions, was removed from the language. Use `!=` instead.
- q: How to test for object identity? --- a: `is`, `is not`
- q: How to customize behavior of `is` and `is not`? --- a: Not possible.
- q: What objects can be tested for identity with the `is` ans `is not` operators? --- a: The `is` and `is not` operators can be applied to any two objects and never raise an exception.
- q: When does the `is` operator throw an exception? --- a: The `is` and `is not` operators can be applied to any two objects and never raise an exception.
- q: `if x` versus `if x == True` versus `if x is True` --- a: Use `if x`; and in extremely rare cases when you really want to explicitly distinguish if `x` is, for example, not `1`, not `[]`, but boolean `True`, check it with `x == True and type(x) is bool`; don't use `x is True`, it will fail in some obscure cases, because `bool` is subclass of `int`.
- q: How to make sure `x` is really `True`, not `1`, not `[]`, etc? Simple `if x` won't work. --- a: `x == True and type(x) is bool`
- q: `if not x` vs `x is None` vs `x == None` --- a: Use the `if not x`; and in cases when you really want to explicitly distinguish `None` and other false values, use `x is None`; don't use `x == None`.
- q: `if x is not None` or `if not x is None`?
- q: `x is y` vs `id(x) == id(y)` --- a: Use the former. Don't use `id(x) == id(y)`, because id of an object in CPython being the location in memory is an implementation detail, this may change.
- q: When two objects of different _built-in_ types compare equal? --- a: Objects of different _built-in_ types, except different numeric types, never compare equal.
- q: What happens when you compare objects of different _built-in_ types, e.g, `'a' == 1` and `'abc' > 10`? a: Except for numeric types, `==` and `!=` always return `False` for objects of different _build-in_ types, `<`, `>`, `<=`, `>=` raise `TypeError` exception.
- q: What happens when you sort a heterogeneous list? --- a: All the elements must be comparable to each other, otherwise the `TypeError` is thrown. If `.sort()` is used for in-place sorting, then the list is modified until the occurrence of the error.
- q: What happens when you compare incomparable types?
- q: What are the right ways to test a var for True, False, None?
- q: What is operator chaining?
- q: Why is `1 > 0 < 1` true?
- q: What is `True is False == False`?

skipped
- q: `not a == b` vs `not (a == b)` vs `b == not a` --- a: `not` has a lower priority than non-boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `b == not a` is a syntax error
- q: What are _less_, _more_, _less or equal_, _more or equal_ operators? --- a: `<`, `>`, `<=`, `>=`
{% endcomment%}


<br />
<br />


# functions

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20functions">
    <p>Your browser does not support iframes.</p>
</iframe>

<https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions>

<http://effbot.org/zone/default-values.htm>
<https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument>
<https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules>

<https://docs.python.org/2/library/functions.html#apply>
Deprecated since version 2.3: Use function(*args, **keywords) instead of apply(function, args, keywords) (see Unpacking Argument Lists).


<https://www.reddit.com/r/Python/comments/41yr58/let_statement_in_python_2014/>
<https://nvbn.github.io/2014/09/25/let-statement-in-python/>

No return statement in lambdas: <https://docs.python.org/3/reference/expressions.html#lambda>

<https://stackoverflow.com/questions/862412/is-it-possible-to-have-multiple-statements-in-a-python-lambda-expression>
just use a tuple: `lambda x: ( f(x), g(x) )`


{% comment %}
- q: How to define a function? --- a: `def whatever(): ...`
- q: Define a function with an optional argument. --- a: `def whatever(data=0): ...`
- q: Define a function with a docstring.
- q: How to get the docstring of a function? --- a: `help(f)` or `f.__doc__`
- q: How to define a function with a keyword-only arguments?
- q: How to define a function that has both required arguments and keyword-only arguments?
- q: What happens when a required function argument is missing? 
- q: How to call this function? `def f(a, *, b): ...`
- q: How to call this function? `def f(*, a, b): ...`
- q: How to call this function? `def f(*, a=1, b): ...`
- q: Can positional arguments come after keyword arguments? Like `f(a=1, 2)`
- q: Can we pass positional arguments as keyword arguments to a function `def f(a, b): ...`? --- Yes. `f(a=1, b=2)`
- q: Can we pass positional arguments as keyword arguments in different order to a function `def f(a, b): ...`? --- Yes. `f(b=2, a=1)`
- q: How to define a function with an arbitrary argument list? --- a: `def f(*args): ...`
- q: What is this function parameter? `def f(*args): ...` --- a: This is an arbitrary argument list. When called like `f(1, 2, 3)` args is a `(1, 2, 3)` tuple.
- q: What is this function parameter? `def f(**kwargs): ...` --- a: This is a dict of keyword arguments. When called like `f(a=1, b=2, c=3)` kwargs is `{a:1, b:2, c:3}`.
- q: How to define a function with arguments, arbitrary argument list, and keyword arguments? --- a: `def f(a, b, *args, c, d, **kwargs): ...`
- q: Can we have non-optional keyword arguments? --- a: Yes, e.g., `def f(*, a, b, **kwargs): ...`. Variables `a` and `b` here are required, and they are not included in `kwargs` when called like `f(a=1, b=2, c=3, d=4)`.
- q: What type is `args` in `def f(*args): ...`? --- a: `tuple`
- q: How to call a function and pass arguments that follow arbitrary argument list? `def f(*args, sep): sep.join(args)` --- a: `f('a', 'b', sep=',')` Everything that follows `*args` or just `*` are keyword arguments.
- q: Define a function with keyword arguments. --- a: `def foo(**kwargs): ...` or `def f(*, a, b, **kwargs): ...`
- q: Are required or optional keyword arguments included in `**kwargs`? Like `def f(*, a, **kwargs):` --- a: No.
- q: What type is `kwargs` in `def f(**kwargs): ...`? --- a: `dict`
- q: How to pass a list or tuple of arguments `lst=[1, 2, 3]` to a function with an arbitrary argument list `def f(*args): ...`? --- a: `foo(*lst)`
- q: How to pass a dictionary of arguments `dct = {'a' : 1, 'b' : 2 }`to a function with keyword arguments `def f(**kwargs)`? --- a: `foo(**dct)`
- q: What do we do here? `f(*lst)` --- We pass a list of arguments to a function defined like `def f(*args): ...`
- q: What do we do here? `f(**dct)` --- We pass a dict of keyword arguments to a function defined like `def f(**kwargs): ...`
- q: Write a lambda function. --- a: `f = lambda x: x**2`
{% endcomment %}

