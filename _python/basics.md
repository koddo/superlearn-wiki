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

<iframe class="autoresize" src="http://superlearn.it/ht/asdf?deckname=python%20--%20true,%20false,%20and%20comparisons&c=00e11412-87e7-46c2-873b-4987138e601e&c=43417abc-f022-42c2-ace7-87bd0239ffcb&c=ce477b4f-271f-4027-bae2-7c74c6847a7a&c=f03ca050-a3a0-481a-aec8-86a21b275aef&c=ec27a052-9ff8-4bbe-81ea-ba4264680d5d&c=2f979875-6470-41e8-98a6-57cf4a7544b8&c=36677f91-1d24-4f5d-970b-29ff4ed99fff&c=97839006-432e-445d-96ac-90fb3a7d8e90&c=20185bb1-d359-4e73-8df3-4734abd48e96&c=c0b810e8-0f6d-4537-9532-98d5ffa3a693&c=f1f76e46-9b13-4bac-98c2-28e3fe1f219e&c=d8313271-3c07-4dcb-9e0d-a861fc7b3da9&c=af569036-0c71-48f4-ab00-2d832a3d5fac&c=725bec17-e183-4fd2-894d-3674ca64df8d&c=a6d623af-6854-453e-adec-639e0b95d63b&c=cc8171d5-4c69-4628-afc7-9bf94f58c42c&c=97b7f65d-6a1c-4a51-aa22-b2b95f4e1d42&c=2cab720c-e62a-4c58-a577-8150b3854584&c=5402f205-f981-40fe-b771-3a4c4aff99f2">
    <p>Your browser does not support iframes.</p>
</iframe>


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

skipped
- q: `not a == b` vs `not (a == b)` vs `b == not a` --- a: `not` has a lower priority than non-boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `b == not a` is a syntax error
- q: What are _less_, _more_, _less or equal_, _more or equal_ operators? --- a: `<`, `>`, `<=`, `>=`
{% endcomment%}


<br />
<br />


# functions


<div class="ryctoic-questions" markdown="1">
- q: Define a function. --- a: `def whatever(): ...`
- q: Define a function with an optional argument. --- a: `def whatever(data=0): ...`
- q: Define a function with a docstring. --- a: An example: 

      def whatever():
          """This is a docstring."""
          pass

- q: Get the docstring of a function? --- a: `help(a_func)` or `a_func.__doc__`
- q: Define a function with a keyword-only arguments. --- a: `def foo(*, arg1=10, arg2=20): ...`
- q: Define a function with an arbitraty argument list. --- a: `def concat(*args, sep="/"): return sep.join(args)`
- q: Define a function with keyword arguments. --- a: `def foo(**kwargs): print(kwargs)`, then call it like this: `foo(a=1, b=2)`, this will print `{'a': 1, 'b': 2}`
- q: Pass a list of arguments to a function with an arbitrary argument list. --- a: Given a function `def foo(*args): ...`, unpack the list `foo(*lst)`
- q: Pass a dictionary of arguments to a function with keyword arguments. --- a: Given a function `def foo(**kwargs): ...`, unpack the dict `foo(**dct)`
- q: Define a function with function annotations. --- a: `def a_func(a_dict: '{str: int}') -> '[str]': print(a_func.__annotations__); ...`
- q: Write a lambda function. --- a: `f = lambda x: x**2`
</div>

TODO: mutable default args, and make sure you use immutable types to catch this earlier
TODO: new type hinting
TODO: function annotations: <https://github.com/kennknowles/python-rightarrow>


# conditionals and loops

``` python
if False:
    whatever()
else:
    print('ok')
```

`switch/case` [pep-3103](https://www.python.org/dev/peps/pep-3103/)

``` python
{
    'a': 1,
    'b': 2,
    'c': 3,
}.get(x, 0)
```

these do not support fall through, and this can be good or bad, depends on the point of view and problems you solve


`range()` used to be `xrange()` in python 2

``` python
for n in range(0,100000000):
  pass

int i = 0
while i < 100000000:
  i += 1
```

<http://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop>

``` Python
if condition:
    ...
else:
    ...
```

TODO: what if we do `for i in range(0)`?
TODO: what if we do `for i in ...: else: ... use i`?


<div class="ryctoic-questions" markdown="1">
- q: Write an if-then-else.
- q: Write an one line if-else statement (ternary conditional operator). --- a: `x = 'good' if y else 'bad'`
- q: What is short for else if? --- a: `elif`
- q: What is going to be printed in this example when the condition is false? `if x < y < z: print(x); print(y); print(z)` --- a: Semicolon binds tighter than the colon in this context, so that in this example, either all or none of the print() calls are executed.
- q: Write a switch/case statement. --- a: Python doesn't have this, but we can have an if/elif chain or dict-based dispatch, but those do not support fall through.
- q: `range()` vs `xrange()` --- a: `range()` used to be `xrange()` in python 2.
- q: Write a for loop from 0 to n-1 inclusive. --- a: `for i in range(n): ...`
- q: Write a for loop from 1 to n inclusive. --- a: `for i in range(1, n+1): ...`
- q: What is going to be printed? `for i in range(1, n+1): print(i)` --- a: Numbers from `1` to `n` inclusive.

- q: Get a range with a step --- a: `range(start, end, step)`

- q: Get a range going backwards. --- a: `range(99, 0, -1)`
- q: Get a range from `99` to `0` with a step `2`. --- a: `range(99, 0, -2)`
- q: Get a range from `0` to `-10`. --- a: `range(0, -10, -1)`
- q: `for i in range(10**10): ...` vs `i=0; while i < 10**10: i+=1; ...;`? --- a: The former should be faster, code for `range()` is optimized.
- q: Write a while statement. --- a: `while condition: ...`
- q: What does `else` do after `for` and `while` statements? --- a: The `else` code is executed after the loop ends if there was no `break`.
- q: What are `break` and `continue` for? --- a: `continue` is for moving forward to the next iteration, `break` is for ending the loop.
</div>


# comprehensions

``` python
[(x,y) for x in range(2) for y in range(3)]
```

- q: Write multidimensional list comprehension. --- a: `[ (x,y) for x in ... for y in ... if x>1 if y>1 ]`
- q: Write a list comprehension to get squares of odd numbers from 1 to 8. --- a: `[x**2 for x in range(1, 9) if x%2==1]`
- q: Write a dictionary comprehension. --- a: `l = [1, 1, 2, 3]; d = { x : l.count(x)   for x in l}`; for this particular example there is `collections.Counter(l)` though.
- q: Write a set comprehension. --- a: `set_of_primes = { i for i in range(101) if is_prime(i) }`
- q: Check if any element in a list satisfies some condition. --- a: `any(l == 'x' for l in a_string)`
- q: Check if all elements in a list satisfy some condition. --- a: `all(x > 0 for x in lst)`

