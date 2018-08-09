---
title:   "Type hinting"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# common

- q: Define a function with function annotations. --- a: `def a_func(a_dict: '{str: int}') -> '[str]': print(a_func.__annotations__); ...`
- q: Type annotations vs type hinting? --- a: With type annotations you can write anything. Type hinting is an application of type annotation, you use latter to write machine readable type hints.

- q: How to mark a function or a var to be ignored by type checker? --- a: `# type: ignore` comment or `@no_type_check` decorator or a custom class or function decorator marked with `@no_type_check_decorator`

# type hinting for functions

- q: How to indicate that a function returns `None`? --- a: `def f() -> None: ...`
- q: How to define an alias for a type? --- a: 
```
Url = str
def go(url: Url):
    ...
```

- q: How to type hint a function argument that has to be a function? --- a:
```
def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    ...
```

- q: How to declare the type of a callable without specifying the call signature? --- a: `def partial(func: Callable[..., str], *args) -> Callable[..., str]: ...`



# generics

- q: 
- a: A TypeVar() expression must always directly be assigned to a variable. The argument to TypeVar() must be a string equal to the variable name to which it is assigned.

- q: How to parameterize a generic function using a `TypeVar`?
- a:
```
T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]
```

- q: How to constrain parametric types to a fixed set of possible types?
- a:
```
AnyStr = TypeVar('AnyStr', str, bytes)

def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y
```

- q:
- a: 

```

class MyStr(str): ...

# see concat above
x = concat(MyStr('apple'), MyStr('pie'))   # type of x will be str, not MyStr
```

- q: Are `List` and `List[Any]` equivalent --- a: yes


https://docs.python.org/3/library/typing.html


# classes

<https://www.python.org/dev/peps/pep-0484/#user-defined-generic-types>

# type hinting for variables

- q: How to add type hinting to older pythons? --- a: `import typing`
- q: stub files

- q: How to annotate a variable? --- a: 
```
var = value # type: annotation
var: annotation; var = value
var: annotation = value
```

- q: How to annotate a variable without initial value? How is it useful? --- a: Being able to omit the initial value allows for easier typing of variables assigned in conditional branches.
```
sane_world: bool
if 2+2 == 4:
    sane_world = True
else:
    sane_world = False
```

- q: How to annotate a tuple packing and unpacking? --- a: although the syntax does allow tuple packing, it does not allow one to annotate the types of variables when tuple unpacking is used
```
# Tuple packing with variable annotation syntax
t: Tuple[int, ...] = (1, 2, 3)

# Tuple unpacking with variable annotation syntax
header: str
kind: int
body: Optional[List[str]]
header, kind, body = message
```

- q: How to annotate a `global` or `nonlocal` var in a function scope? --- a: Illegal, <https://www.python.org/dev/peps/pep-0526/#where-annotations-aren-t-allowed>
- q: How to annotate vars used in a `for` or `with` statement? --- a: 
```
a: int
for a in my_iter:
    ...

f: MyFile
with myfunc() as f:
    ...
```

- q: How to annotate an instance variable? A class variable? --- a: <https://www.python.org/dev/peps/pep-0526/#class-and-instance-variable-annotations>
