---
title:   "Basics"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# hello world

<iframe class="autoresize" src="http://superlearn.it:8080/ht/cards/"><p>Your browser does not support iframes.</p></iframe>



# true, false, and comparisons

{% comment %}
{% endcomment %}

``` python
if () or [] or {} or None:
    'this line is skipped'
```
<https://docs.python.org/3/library/stdtypes.html#truth-value-testing>


<br/>

The interesting thing in python: `b == not a` is a syntax error.
`not` has a lower priority than non-boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `b == not a` is a syntax error.
<https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not>

<br/>

as always, `and` and `or` are short-circuit operators, second argument is not evaluated here:

``` python
if False and whatever():
    'this line is skipped, whatever() is not evaluated'
```

<br/>

`x < y <= z` is equivalent to `x < y and y <= z`, except `y` is evaluated only once
in both cases `z` is not evaluated at all when `x < y` is found to be false

<br/>

comparison operators look quite standard: `==`, `!=`, `<`, `>`, `<=`, `>=`
and for object identity: `is`, `is not`
objects of different _built-in_ types never compare equal (except different numeric types), but we can define an object with `__eq__` --- <http://stackoverflow.com/questions/12379840/python-comparison-between-built-in-and-user-defined-types>
`<`, `>`, `<=`, `>=` raise `TypeError` exception when the objects are of different types that cannot be compared, or in other cases where there is no defined ordering

``` python
>>> 'abc' > 1000
TypeError: unorderable types: str() > int()
```

behavior of the `is` and `is not` operators cannot be customized; also they can be applied to any two objects and never raise an exception

<https://docs.python.org/3/library/stdtypes.html#comparisons>

<br/>

generally you only want to be using `is` with mutable objects (or None, which is the exception)
`x is None` vs `x == None`: [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations)
> Comparisons to singletons like None should always be done with is or is not , never the equality operators. 


<http://stackoverflow.com/questions/9494404/use-of-true-false-and-none-as-return-values-in-python-functions>


``` Python
class A(object):
    def __eq__(self, other):
        print( "A __eq__ called: %r == %r ?" % (self, other) )
        return self.value == other.value
class B(object):
    def __eq__(self, other):
        print( "B __eq__ called: %r == %r ?" % (self, other) )
        return self.value == other.value

a = A()
a.value = 3
b = B()
b.value = 4
a == b
```


<div class="ryctoic-questions" markdown="1">
deck:
python --- true, false, and comparisons

TODO:

- q: `==` vs `__eq__()` --- a:
- q: Why `__eq__()` returns `NotImplemented`? --- a: 
- q: What happens when you compare incomparable types?

<https://docs.python.org/3/reference/datamodel.html#object.__eq__>

<https://docs.python.org/3/library/constants.html#NotImplemented>

<https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons>

- q: What values are considered false in python? --- a: `False`, `None`, any numeric zero, empty sequence, empty dict, instance with `__bool__()` returning False or `__len__()` returning zero
- q: `not a == b` vs `not (a == b)` vs `b == not a` --- a: `not` has a lower priority than non-boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `b == not a` is a syntax error
- q: short-circuiting behavior of boolean operators --- a: `if False and whatever(): 'this line is skipped, whatever() is not evaluated'`
- q: `x < y <= z` vs `x < y and y <= z` --- a: `x < y <= z` is equivalent to `x < y and y <= z`, except `y` is evaluated only once, and in both cases `z` is not evaluated at all when `x < y` is found to be false
- q: What are equal and not equal operators? --- a: `==`, `!=`, the `<>` was removed
- q: What are less, more, less or equal, more or equal operators? --- a: `<`, `>`, `<=`, `>=`
- q: How to test for object identity? --- a: `is`, `is not`
- q: How to customize behavior of `is` and `is not`? --- a: Behavior of the `is` and `is not` operators cannot be customized.
- q: What objects can be tested for identity with the `is` ans `is not` operators? --- a: The `is` and `is not` operators can be applied to any two objects and never raise an exception.
- q: When does the `is` operator throw an exception? --- a: The `is` and `is not` operators can be applied to any two objects and never raise an exception.
- q: `if x` vs `if x == True` vs `if x is True` --- a: Use `if x`; and in extremely rare cases when you really want to explicitly distinguish if `x` is, for example, not `1`, not `[]`, but boolean `True`, check it with `x == True and type(x) is bool`; don't use `x is True`, it will fail in some obscure cases, because `bool` is subclass of `int`.
- q: `if not x` vs `x is None` vs `x == None` --- a: Use the `if not x`; and in cases when you really want to explicitly distinguish `None` and other false values, use `x is None`; don't use `x == None`, because PEP 8.
- q: `x is y` vs `id(x) == id(y)` --- a: Use the former. Don't use `id(x) == id(y)`, because id of an object in CPython being the location in memory is an implementation detail, this may change.
- q: When two objects of different _built-in_ types compare equal? --- a: Objects of different _built-in_ types, except different numeric types, never compare equal.
- q: What happens when you compare objects of different _built-in_ types, e.g, `'a' == 1` and `'abc' > 10`? a: Except for numeric types, `==` and `!=` always return `False` for objects of different _build-in_ types, `<`, `>`, `<=`, `>=` raise `TypeError` exception.
- q: What happens when you sort a heterogeneous list? --- a: All the elements must be comparable to each other, otherwise the `TypeError` is thrown. If `.sort()` is used for in-place sorting, then the list is modified until the occurrence of the error.
</div>

<br />
<br />


<iframe class="autoresize" src="https://vagrant.local:8443/api/v0/deck/4db66f7c-cee0-4de3-84c7-fdd28b030a82"><p>Your browser does not support iframes.</p></iframe>


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

<iframe class="autoresize" src="https://vagrant.local:8443/api/v0/deck/aeb6a5dd-3ff7-4856-bbe2-f201004d82e2"><p>Your browser does not support iframes.</p></iframe>

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

