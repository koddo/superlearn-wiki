---
title:   "Basics2"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# TODO

<https://docs.python.org/3.6/library/contextlib.html>


# mutable default arguments
- q: What happens if you have a mutable object as a default parameter, like `def f(l = []): ...`, and you mutate the list, e.g., append values to it inside the function?
- q: When you have a mutable object as a default value, like `def f(l = []): ...`, how to make sure it's not shared between function calls? --- a: `def f(l = None): if l is None: l = [] ...`
- q: What is mutable defaults in functional programming terms? --- a: let over lambda
- q: Why is python designed this why that is has mutable default arguments?

# scope
- q: How to have a closure in python? --- `nonlocal`
- q: What is `nonlocal` for? --- a: For closures.
- q: Can you access global variables in a function by declaring them `nonlocal`? --- a: No. `nonlocal` specifically excludes the global scope. See _LEGB_ scope resolution rule.
- q: What is _LEGB_ scope resolution rule?
- q: Why a function can read global variables without declaring them `global`? --- _LEGB_ scope resolution rule.
- q: How o to access a global variable in a function? --- a: To read them just read them. To modify mark them `global`.
- q: Should you mark a variable `global` in a function to access the global? --- a: Well, no. To read them just read them. To modify mark them `global`.



TODO: configure my editor to highlight default values with a bright red color with an overlay that reminds about dangers of mutable default values

# docstrings

PEP 257 -- Docstring Conventions: <https://www.python.org/dev/peps/pep-0257/>

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python%20--%20docstrings">
    <p>Your browser does not support iframes.</p>
</iframe>




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





