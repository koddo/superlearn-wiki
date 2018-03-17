---
title:   "Python"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}



# todo

- q: How to pass `+`, `**`, `[3:5]`, `.field` as a function? --- a: The operator module have all these operators: <https://docs.python.org/3/library/operator.html>
TODO: `None` is a singleton
TODO: trailing comma, https://stackoverflow.com/questions/11597901/why-are-trailing-commas-allowed-in-a-list

<https://www.tutorialspoint.com/python/python_interview_questions.htm>

<https://www.reddit.com/r/Python/comments/6cvx0s/the_meaning_of_underscores_in_python>

<https://github.com/satwikkansal/wtfPython>, <https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python/>

pprint
to a file

<https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python>






<https://docs.python.org/3/library/stdtypes.html#string-methods>







TODO: `Ellipsis` object --- <http://stackoverflow.com/questions/118370/how-do-you-use-the-ellipsis-slicing-syntax-in-python/118508#118508>
TODO: `NotImplemented` object










try logbook module -- <http://logbook.readthedocs.io/en/stable/>


``` python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```


- q: How to generate a list of packages into `requirements.txt`? --- a: `pip freeze > requirements.txt`
- q: How to install packages from requirements.txt? --- a: `$ pip install -r requirements.txt`

TODO: complexity of all operations for lists, dicts, sets, deques considering their internal structure

[bool](https://docs.python.org/3/library/functions.html#bool)
[object](https://docs.python.org/3/library/functions.html#object)
[id](https://docs.python.org/3/library/functions.html#id)
[hash](https://docs.python.org/3/library/functions.html#hash)

abstract base classes for containers <https://docs.python.org/3/library/collections.abc.html>

q: how to assign an attribute to the built-in object class? a: prohibited, intentionally --- <http://stackoverflow.com/questions/5741699/attribute-assignment-to-built-in-object/22103924#22103924>, <http://stackoverflow.com/questions/1529002/cant-set-attributes-of-object-class/1529099#1529099>

q: what does `@something('whatever') def myfunc()` mean? --- a: this is called pie syntax for decorators, this is a fancy way of doing this: `def myfunc(): pass; myfunc = something('whatever')(myfunc)` 
q: what is a decorator? --- a: it's a function that gets a function and returns it decorated 


q: what does `map()` return?

<https://www.quora.com/What-are-good-Python-interview-questions>
<http://www.ilian.io/python-interview-question-and-answers/>
<http://career.guru99.com/top-25-python-interview-questions/>

<http://www.tutorialspoint.com/python/python_interview_questions.htm>



q: declare main() in python --- a: `if __name__ == '__main__': ...`

TODO: how to measure time
$ python -m timeit "'somestring'.find('str', 2, 9)"
$ python -m timeit "'somestring'[2:9].find('str')"


TODO: shallow and deep copies

q: how to get an integer `111...1` of lenght `n` without using string operations? --- a: `10**n//9`
q: how to get a palindrome number like `123454321` up to `9` in the middle? --- a: `111..11` to the power of `2`

- q: What does the `pass` do?

TODO: add questions like this: in which module the `deque` is?

TODO: __slots__
TODO: <https://pypi.python.org/pypi/PyMonad/>
TODO: persistent data structures <https://github.com/tobgu/pyrsistent>
TODO: <http://stackoverflow.com/questions/101268/hidden-features-of-python>
TODO: <http://www.asmeurer.com/python3-presentation/slides.html#1>
TODO: <https://github.com/sfermigier/awesome-functional-python>, <https://www.reddit.com/r/Python/comments/5iuj70/awesome_functional_python/>
TODO: generate random number


- q: Default character encoding of python3 files? -- a: `utf-8`

- q: How to run a simple http server to serve static files? -- a: `$ cd path && python3 -m http.server 4001`

<https://www.reddit.com/r/Python/comments/5zk97l/what_are_some_wtfs_still_in_python_3/>

parallelism lib named dask

- q: A question on semicolon: what is going to be printed in this example when the condition is false? `if x < y < z: print(x); print(y); print(z)` --- a: Semicolons are introduced to language to write simple one-liners like this. Don't overuse them.










# collections module

TODO: q:
ChainMap -- constructing `O(n)`, lookup `O(n)`
using dict update chain -- constructing `O(nm)`, lookup `O(1)`
This means that if you construct often and only perform a few lookups each time, or if M is big, ChainMap's lazy-construction approach works in your favor.
<http://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap/23441777#23441777>

q: create a named tuple --- a: `Point = collections.namedtuple('Point', 'x, y')`


q: get a dict, which which counts distinct elements in a list --- a: `collections.Counter(list)`




# bytes and bytearrays

[bytearray](https://docs.python.org/3/library/functions.html#bytearray)
[bytes](https://docs.python.org/3/library/functions.html#bytes)
[memoryview](https://docs.python.org/3/library/functions.html#memoryview)


The methods on bytes and bytearray objects don’t accept strings as their arguments, and vice versa:

``` python
a = b"abc"
b = a.replace(b"a", b"f")
```

join

decode

count
startswith, endswith
(r)find
(r)index
(r)partition
replace
translate, maketrans

these produce new objects:
center 
(lr)just
(l)strip
(r)split

capitalize
expandtabs
splitlines

- q: `bytes` vs `bytearray` -- a: `bytes` are immutable, just like strings, while `bytearray` objects are mutable and algorightms with them can be faster when we have lots of modifications, because we avoid lots of copying.

# arrays

<https://docs.python.org/3/library/array.html#module-array>

<http://stackoverflow.com/questions/2214651/efficient-python-array-with-100-million-zeros>
<http://stackoverflow.com/questions/2214651/efficient-python-array-with-100-million-zeros#comment2167466_2214771>: indexing a Python list is a very fast operation: it just fetches the object already in the internal array. array.array and numpy.array objects do not contain Python objects, so the actual datatype stored in the array needs to be converted on access. It's the price for the much, much lower memory use and actual contiguous block of data
<http://stackoverflow.com/questions/3214288/what-is-the-fastest-way-to-initialize-an-integer-array-in-python/3214343#3214343>

- q: How to initialize a large array? --- a: `from array import array; a = array('i', [0]) * 1000`
- q: `list` vs `array.array`? --- a: `array` defines an object type which can _compactly_ represent an array of basic values: characters, integers, floating point numbers. At the cost of speed.


# math

``` python
math.pi
math.e
math.inf   # equivalent to float('inf)
math.nan   # equivalent to float('nan')

math.floor(0.7)
math.ceil(0.7)

math.gcd(8,12) == 4
math.factorial(5) == 120

math.isfinite(5)
math.isinf( math.inf )
math.isnan( math.nan )

math.degrees( math.pi/2 )
math.radians( 90 ) == math.pi/2
math.isclose( math.sin( math.pi/6 ), 0.5 ) == True

math.pow(3.0, 2.0) == 9.0
math.log2(8.0) == 3
math.log(100.0, 10) == 2.0
math.sqrt(25.0) == 5.0
```

TODO: all these funcs

## complex numbers

in python `j` is used instead of `i` for complex unit, because they decided `j` is easier to read and it follows engineering convention for complex numbers
whatever
<http://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i>

q: why `j` instead of `i` for imaginary unit in complex numbers? --- a: they decided `j` is easier to read and it follows engineering convention for complex numbers
q: convert a comlex number to polar coordinates --- a: `r, phi = cmath.polar(c)`


# python built-ins

arbitrarily grouped

# numbers
[max](https://docs.python.org/3/library/functions.html#max)
[min](https://docs.python.org/3/library/functions.html#min)
[abs](https://docs.python.org/3/library/functions.html#abs)
[round](https://docs.python.org/3/library/functions.html#round)
[sum](https://docs.python.org/3/library/functions.html#sum)
[pow](https://docs.python.org/3/library/functions.html#pow)
[divmod](https://docs.python.org/3/library/functions.html#divmod)

[bin](https://docs.python.org/3/library/functions.html#bin)
[hex](https://docs.python.org/3/library/functions.html#hex)
[oct](https://docs.python.org/3/library/functions.html#oct)

[int](https://docs.python.org/3/library/functions.html#int)
[float](https://docs.python.org/3/library/functions.html#float)
[complex](https://docs.python.org/3/library/functions.html#complex)

`pow(3, 2, 2) == 1`


`q, r = (n // d, n % d)` vs `q, r = divmod(n, d)`:
<http://stackoverflow.com/questions/30079879/is-divmod-faster-than-using-the-and-operators>


q: get absolute value of `x` --- a: `abs(x)`
q: get number `x` rounded to nearest integer --- a: `round(2.77) == 3`
q: get number `x` rounded to `n` digits from the decimal point --- a: `round(2,33, 1) == 2.3`
q: get sum of sequence of numbers --- a: `sum()` or `math.fsum()`
q: get `x` raised to the power of `y`, a: `x**y`
q: get `a` raised to the power of b, modulo m, a: `x**y % m` or `pow(a, b, m)`, the latter is faster
q: get quotient and remainder using integer division, a: `q, r = (n // d, n % d)` or `q, r = divmod(n, d)`
q: `q, r = (n // d, n % d)` vs `q, r = divmod(n, d)` speed, a: the latter is slower for native integers because of function call overhead, but faster for large numbers
q: get remainder after integer devision `a` by `b` --- a: `5 % 2 == 1`
q: float division vs integer division --- a: `5/2 == 2.5` vs `5 // 2 == 2`


q: convert an integer to a binary string
q: convert an integer to a hexadecimal string
q: convert an integer to a octal string (base 8)

q: convert a string to an integer
q: convert a string to a float

q: construct a complex number

## fractions

``` python
from fractions import Fraction
from decimal   import Decimal

Fraction(5, 3)
Fraction( Decimal('1.1') )
Fraction( '9/16' )

Fraction(1, 2) + 1   == Fraction(3, 2)
Fraction(1, 2) + 1.0 == 1.5

f = Fraction(1, 2)
n, d = (f.numerator, f.denominator)
print(n, d)
```

q: get a fraction from nominator/demnominator pair, decimal, and string --- a: `fractions.Fraction(5, 3)`, and `Fraction( decimal.Decimal('1.1') )`, and `Fraction('9/16')`
q: what are `fractions.Fraction(1, 2) + 1` and `Fraction(1, 2) + 1.0` --- a: `Fraction(3, 2)` and `1.5`
q: get numerator and denominator of a `f = fractions.Fraction(1, 2)` --- a: `n, d = (f.numerator, f.denominator)`
q: get greatest common divisor of two numbers --- a: `math.gcd(a, b)`


# structs and iteration

[filter](https://docs.python.org/3/library/functions.html#filter)
[map](https://docs.python.org/3/library/functions.html#map)
[zip](https://docs.python.org/3/library/functions.html#zip)
[len](https://docs.python.org/3/library/functions.html#len)



q: get length of x --- a: [len(x)](https://docs.python.org/3/library/functions.html#len)
q: `len(x)` vs `x.__len__` --- a: TODO: `__len__` is slower than `len()`, because `__len__` involves a dict lookup [link](http://stackoverflow.com/questions/20302558/why-python-function-len-is-faster-than-len-method/20302670#20302670)

- q: Using a `for` loop, how to access the loop index? -- a: `for i, el in enumerate(a_list): ...`
- q: What does the `enumerate(a_list)` return? -- a: An `enumerate object`, for iterating over tuples `(index, element)`.

# input/output

[chr](https://docs.python.org/3/library/functions.html#chr)
[format](https://docs.python.org/3/library/functions.html#format)
[open](https://docs.python.org/3/library/functions.html#open)
[ord](https://docs.python.org/3/library/functions.html#ord)
[print](https://docs.python.org/3/library/functions.html#print)

Don't use file.readlines() in a for-loop, a file object itself is enough: lines = [line.rstrip('\n') for line in file]

# oop

TODO:
- q: `==` vs `__eq__()` --- a:
- q: Why `__eq__()` returns `NotImplemented`? --- a: 
<https://docs.python.org/3/reference/datamodel.html#object.__eq__>
<https://docs.python.org/3/library/constants.html#NotImplemented>
<https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons>


TODO: multimethods, dispatch

[classmethod](https://docs.python.org/3/library/functions.html#classmethod)
[staticmethod](https://docs.python.org/3/library/functions.html#staticmethod)
[property](https://docs.python.org/3/library/functions.html#property)
[super](https://docs.python.org/3/library/functions.html#super)

q: classmethod vs staticmethod, a: <http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner/12179752#12179752>


@property
@name.setter

TODO: maybe later metaclass <http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python/6581949#6581949>

TODO: multiple inherirance and super()
<https://fuhm.net/super-harmful/>
<https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>
<http://blog.codekills.net/2014/04/02/the-sadness-of-pythons-super/>
Порядок разрешения методов в Python, method resolution order <https://habrahabr.ru/post/62203/>

TODO: multiple inheritance vs composition
TODO: multiple inheritance when sets of functions are disjoint


# date and time

q: convert a string like `17.04.1975 14:35` to a datetime --- a: `from datetime import datetime; datetime.strptime(s, '%d.%m.%Y %H:%M')`
q: get difference in seconds between two datetimes --- a: `abs(dt2 - dt1).total_seconds()`, this is equivalent to `diff.seconds + diff.days * 86400`

``` python
'{:%Y-%m-%d %H:%M:%S}'.format(datetime(2010, 7, 4, 12, 15, 58))
```


# files and dirs

- q: get current working directory --- a: `os.getcwd()`
- q: change current working directory --- a: `os.chdir('/usr/bin')`
- q: join `dirname`, `subdirname` and `filename` --- a: `os.path.join(dirname, subdirname, filename)`
- q: expand `~` --- a: `os.path.expanduser('~')`
- q: split absolute path into `dirname` and `filename` --- a: `dirname, filename = os.path.split(abspath)`
- q: split a `filename` into `name` and `extension` --- a: `name, extension = os.path.splittext(filename)`
- q: get a list of filenames matching a wildcard --- a: `import glob; glob.glob('/var/log/*sys*')`
- q: get absolute path of a given file by relative path --- a: `os.path.realpath('python.md')`
- q: get metadata of a file and get modification time and size --- a: `metadata = os.stat('python.md'); time.localtime(metadata.st_mtime); import humanize; humansize.approximate_size(metadata.st_size)`

- q: How to check if a file exists before opening it? --- a: Don't, that leads to race conditions. Just open it in a try or with block.


# iterators and generators

TODO: - q: iterators can be used just once
TODO: - q: `for x in struct: ...` is equivalent to `for x in iter(struct): ...`

<http://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators>
<http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols>

q: `sum([x in x in range(10)])` vs `sum(x in x in range(10))` -- a: The latter uses a generator, has lower memory consumption, because it doesn't create a list.

TODO: reset iterator, tee vs list <http://stackoverflow.com/questions/3266180/can-iterators-be-reset-in-python/3267069#3267069>
TODO: - q: iterator and iterable <http://stackoverflow.com/a/9884501/159149>

for, with, comprehensions, StopIteration <https://www.python.org/dev/peps/pep-0479/>

# coroutines

TODO

# misc


# skipped hackerrank challenges

sets
<https://www.hackerrank.com/challenges/no-idea>
<https://www.hackerrank.com/challenges/py-the-captains-room>

math
<https://www.hackerrank.com/challenges/find-angle> --- python 3 is disabled

collections
<https://www.hackerrank.com/challenges/piling-up> --- deque

classes
<https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers>
<https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle>

functional
<https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter>

regex
all

xml
all

closures
<https://www.hackerrank.com/challenges/decorators-2-name-directory>




# introspection

<https://python-hunter.readthedocs.io/en/latest/readme.html>

[dir](https://docs.python.org/3/library/functions.html#dir)
[vars](https://docs.python.org/3/library/functions.html#vars)
[globals](https://docs.python.org/3/library/functions.html#globals)
[locals](https://docs.python.org/3/library/functions.html#locals)
[getattr, setattr, delattr, hasattr](https://docs.python.org/3/library/functions.html#getattr, setattr, delattr, hasattr)
[type](https://docs.python.org/3/library/functions.html#type)
[isinstance](https://docs.python.org/3/library/functions.html#isinstance)
[issubclass](https://docs.python.org/3/library/functions.html#issubclass)
[callable](https://docs.python.org/3/library/functions.html#callable)
[help](https://docs.python.org/3/library/functions.html#help)

q: dir() vs vars(...).keys() a: <http://stackoverflow.com/questions/980249/difference-between-dir-and-vars-keys-in-python>
q: check the import search path --- a: `sys.path`

- q: What is `vars()` for?
- a: It takes zero or one argument. Without argument `vars()` behaves like `locals()`.

With a argument:

``` Python
class Whatever:
    def __init__(self):
        self.x = 1
        self.y = 2

w = Whatever()
print(vars(w))
# {'x': 1, 'y': 2}
```


# code evaluation

[compile](https://docs.python.org/3/library/functions.html#compile)
[eval](https://docs.python.org/3/library/functions.html#eval)
[exec](https://docs.python.org/3/library/functions.html#exec)

<http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python>






# itertools module

<https://more-itertools.readthedocs.io/en/latest/>

``` python
lst = [('USA', 'LA'), ('Russia', 'Moscow'), ('USA', 'NY'), ('Russia', 'St. Petersburg'), ('England', 'London')]

[(k, list(g)) 
   for k, g in 
   itertools.groupby( sorted(lst), key = lambda x: x[0] )]
             ## [('England', [('England', 'London')]), ('Russia', [('Russia', 'Moscow'), ('Russia', 'St. Petersburg')]), ('USA', [('USA', 'LA'), ('USA', 'NY')])]

[(k, [j for i,j in g]) 
   for k, g in 
   itertools.groupby( sorted(lst), key = lambda x: x[0] )]
             ## [('England', ['London']), ('Russia', ['Moscow', 'St. Petersburg']), ('USA', ['LA', 'NY'])]



```

product
permutations
combinations

count(start=0[, step=1])
cycle(lst)
repeat(elem[, times=10])

groupby
accumulate
chain
dropwhile, takewhile
zip_longest

TODO: compress, better groupby, tee

TODO: `itertools.isslice`

TODO: how to get prev and next values in a loop
if you don't have to look too smart:
```
l = len(timestamps)
for i in range(l):
    if i < l-1:
        result.append(timestamps[i])
        result.append(  (timestamps[i] + timestamps[i+1]) / 2  )
    else:
        result.append(timestamps[i])
```


q: get a cartesian product of two sequences --- a: `itertools.product(s1, s2)`
q: get permutations of length `k` of elements in a list --- a: `itertools.permutations(a_list, k)`
q: get combinations of length `k` of elements in a list --- a: `itertools.combinations(a_list, k)`
q: get combinations with repetitions of length `k` of elements in a list --- a: `itertools.combinations_with_replacement(a_list, k)`
q: divide a string into groups of repeated consecutive elements, e.g., `'AAAABBBCCDAA'` into `['AAAA', 'BBB', 'CC', 'D', 'AA']` --- a: `[''.join(list(g)) for k, g in itertools.groupby('AAAABBBCCDAA')]`
q: group elements of a list by some key, e.g., `[..., ('Russia', 'Moscow'), ..., ('Russia', 'St. Petersburg'), ...]` into  `[..., ('Russia', ['Moscow', 'St. Petersburg']), ...]`--- a: `[(k, [j for i,j in g]) for k, g in itertools.groupby(sorted(lst), lambda x: x[0])]`

q: get an iterator for an infinite sequence of numbers like `10, 15, 20, 25, ...` --- a: `from itertools import count; for i in count(start10, step=5): ...`
q: get an iterator, which infinitely goes through a list like `a, b, c -> a, b, c, a, b, c, a, ...` --- a: `from itertools import cycle; for i in cycle('abc'): ...`
q: get an iterator, which infinitely (or optionally for a given number of times) returns an element --- a: `from itertools import repeat; for i in repeat('a'): ...` or `repeat('a', times=10)`

q: get an iterator, which is similar to reduce, but returns an intermediate results --- a: `itertools.accumulate(lst, operator.mul)`
q: how to iterate over multiple lists, one after another, without concatenating --- a: `itertools.chain( [1, 2, 3], [4, 5, 6] )`
q: `itertools.chain()` vs `itertools.chain.from_iterable()` --- a: the latter gets lazily iterates over input, which can be infinite sequence
q: get rid of head of a list before a predicate becomes false --- a: `list(itertools.dropwhile(lambda x: x<3, [1, 2, 3, 1, 2, 3])) == [3, 1, 2, 3]`
q: get rid of tail of a list after a predicate becomes false --- a: `list(itertools.takewhile(lambda x: x<3, [1, 2, 3, 1, 2, 3])) == [1, 2]`
q: `slice()` vs `itertools.islice()` --- a: the latter is for iterators, which don't support indexing, consumes data on them; in most cases just use the former
q: `map()` vs `itertools.starmap()` --- a: the latter is for data, which has been pre-zipped, `list( itertools.starmap(pow, [(5,2), (3,2), (10,3)]) ) == [25, 9, 1000]`
q: `zip()` two sequences until the longest one is exhauseted, with a given value for missing bits --- a: `itertools.zip_longest(*iterables, fillvalue=None)`
q: `zip()` vs `itertools.zip_longest()` --- a: the former stops when the shortest iterator is exhausted, the latter stops when the longest one is done



# numpy

<https://github.com/Kyubyong/numpy_exercises>

`numpy.array()`: <http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>
`numpy.array()` vs `numpy.asarray()`: <http://stackoverflow.com/questions/14415741/numpy-array-vs-asarray>
numpy arrays vs matrices: <https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html#array-or-matrix-which-should-i-use>
array cheatsheet: <http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/python/arrays.html>

<http://www.scipy-lectures.org/intro/intro.html>

TODO: `numpy.array()` vs `numpy.asarray`

``` python
import numpy

print(numpy.array(['1', '2'], dtype=float))
```
q: numpy arrays vs python lists --- TODO
q: get a numpy array of floats from list of integers --- a: `numpy.array( [1, 2, 3], dtype=float )`
q: get a numpy array of floats from input --- a: `numpy.array( input().split(), dtype=float )`
q: `numpy.array` vs `numpy.ndarray` --- a: `array()` is a function that returns n-dimensional array `ndarray`, the latter shouldn't be used directly
q: `numpy.array` vs `numpy.matrix` --- a: unless you are heavily into linear algebra and want pretty matrix operations, stick with arrays
q: convert a 1x6 numpy array to 3x2 --- a: `numpy.reshape(numpy.array([1, 2, 3, 4, 5, 6]), (3, 2))`
q: what does `-1` mean in `numpy.reshape(a, (3, -1))`? --- a: it means the value is inferred from remaining dimensions
q: transpose a numpy array --- a: `numpy.transpose(a_numpy_array)`
q: convert a numpy array from _n_-dimensional to _1_-dimensional --- a: `a_numpy_array.flatten()`
q: get a numpy array of zeros 3x3x4 --- a: `numpy.zeros((3, 3, 4), dtype=float)`
q: get a numpy array of ones 3x3x4 --- a: `numpy.ones((3, 3, 4), dtype=float)`
q: get a numpy nxn array with ones on the main diagonal --- a: `numpy.identity(n)`
q: get a numpy nxm array with ones on the diagonal below the main one --- a: `numpy.eye(n, m, k=-1)`
q: get an element-wise sum, substraction, multiplication, division, floor, ceil, etc of two numpy arrays
q: get a sum, max, mean, etc of a numpy array along a given axis --- a: `numpy.sum(an_array, axis=0)`
q: get a value of a polynomial with given coefficients at point `x` --- a: numpy.polynomials.polyval(x, [3, 2, 1])
































# context managers

`@cache` implements lru cache
# xml

``` python
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring( s ))

for child in tree.getroot():
    pass

isinstance(tree.getroot().attrib, dict) == True
```












# libs

<https://python-graph-gallery.com/>
# garbage collector

<https://rushter.com/blog/python-garbage-collector/>
<https://rushter.com/blog/python-memory-managment/>




# unpacking

- q: Unpack `[1, [2, 3]]` into three variables `a = 1; b = 2; c = 3`. --- a: `a, (b, c) = [1, [2, 3]]`
- q: advanced unpacking: `a, b, *rest = range(10)`, `a, *rest, b = range(10)`, `first, *_, last = f.readlines()`

<https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking>


