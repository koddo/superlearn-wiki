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


TODO:
casefold?
capitalize
lower
upper
title
swapcase

TODO: <https://docs.python.org/3/library/string.html#string-constants>
isidentifier?
isalnum
isalpha
isdecimal
isdigit
islower
isnumeric
isprintable
isspace
istitle
isupper

q: reverse case of a string, lower case to upper case and vice versa --- a: `string.swapcase(str)`
q: get an alphabet string --- a: `string.ascii_lowercase`
q: get an uppercase alphabet string --- a: `string.ascii_uppercase`
q: get all printable chars --- a: `string.printable`
q: get all punctuation chars --- a: `string.punctuation`


not covered: `expandtabs`, because highly specialized


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


- q: Closures in python. -- a: To capture a binding in the outer scope, use `nonlocal x`.

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


q: what is `None == None`? --- a: `True`
q: what is `None == 0`? --- a: `False`
q: what is `None == ''`? --- a: `False`
q: what is `None == False`? --- a: `False`
q: what if we compare `None` to something? --- a: `None == None` is `True`, while comparing to anything else is `False`

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









# dicts

interesting thing: `d[k]` raises `ValueError` when the `k` is not in the dict, while `d[k] = 'whatever'` sets the new value

``` python
d = {}
d[1]   # raises ValueError 
d[1] = 'whatever'   # sets the value
```

interesting: Due to the way the Python C-level APIs developed, a lot of built-in functions and methods don't actually have names for their arguments. `.get(x, default=0)` throws `TypeError: get() takes no keyword arguments`, but `.get(x, 0)` works


TODO: `iteritems`, `iterkeys`, `itervalues` are no longer supported

q: Create an empty dictionary. --- a: `d = {}`
q: Create an dictionary with key-value pairs `1: 'a', 2: 'b'`. --- a: `d = { 1: 'a', 2: 'b' }`
q: Get a value from dict by a key. --- a: `d['the key']` or `d.get('whatever', 'zero')` when you want a default value. The former raises `KeyError`.
q: what happens when you try to acces a non-existent key in a dict? --- a: it raises `KeyError`
q: del d[key]
q: del d[non_existant_key]
q: what does del d[k] return?

q: Get list of keys of a dict. --- a: `list(a_dict.keys())`, the `.keys()` returns a dictview.

q: What is a `dictview`? --- a: Provids a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. Once it's converted to a list, this property disappears.
q: What does `a_dict.items()` return? --- a: A `dictview` object.
q: What does `a_dict.keys()` return? --- a: A `dictview` object.
q: What does `a_dict.values()` return? --- a: A `dictview` object.
q: What can we do with a `dictview` returned by `dct.items()`, `dct.keys()`, `dct.values()`? --- a: `list(dv)`, `len(dv)`, check `x in dv`; iterate `iter(dv)`; `dct.keys()` and `dct.items()` are set-like, can do `dct.keys() & set(...)`

q: Construct a dict from two lists. -- a: First, make sure they are of same length (or you know what you are doing when not), and then `dict(zip(keys, values))`.
q: Construct a dict from list of 2-lists.  -- a: `dict( [[1, 'a'], [2, 'b']] )`
q: Construct a dict from list of 2-tuples. -- a: `dict( [(1, 'a'), (2, 'b')] )`
q: Convert a dict to a list of 2-tuples. -- a: `list(dct.items())` or a comprehension.
q: Check if a key exists in a dict. --- a: `if k in a_dict: ...` or `not in`
q: Get number of key-value pairs in a dictionary. --- a: `len(d)`



q: Iterate over keys in a dict. --- a: `for k in dct: ...`, equivalent to `for k in dct.keys(): ...`
q: Iterate over sorted keys in a dict. --- a:
q: Iterate over key-value pairs in a dict. --- a: `for k,v in dct.items(): ...`
q: with sorted keys?

q: How to iterate over a dict and remove items based on a condition? -- a: Do not add or remove items from data structures while iterating over them. In the best case this causes `RunTimeError`, sometimes it leads to infinite loop, sometimes to skipping items. For example, given a dict, our choices are: iterate over a copy of keys `for k in list(dct.keys())`; create a list of keys to delete after iteration; use dict comprehension, which creates a new dict.
q: Why can't we simply iterate over keys in a dict to remove some items in the same dict like in `for k in dct.keys(): if cond: del dct[k]`? -- a: Iterators are not informed when a data structure is modified. In the best case this causes `RunTimeError`, sometimes it leads to infinite loop, sometimes to skipping items.
q: Get a value for key in a dict, or default value when not found. --- a: `d.get(k, 0)`; note that `.get(k, default=0)` will throw `TypeError: get() takes no keyword arguments`
q: What happens when you do `a_dict.get(x, default=0)`? --- a: `TypeError: get() takes no keyword arguments`; just write `.get(x, 0)`
q: Set a value for key in a dict. --- a: `d['whatever'] = 1`
q: `a_dict[k]` vs `a_dict.get(k)` --- a: The latter never raises `KeyError`, returns `None` or provided default value, e.g., `a_dict.get(k, 0)`.
q: What does `a_dict.setdefault(k, defaultvalue)` do? --- a: Returns `a_dict[k]` when `k` exists or sets `a_dict[k] = defaultvalue` and then returns it, instead of just returning it like the `.get()` does. Note that `defaultdict` is a modern replacement for the `.setdefault()`, because its name is much more obvious.
q: `a_dict.get(k, defaultvalue)` vs `a_dict.setdefault(k, defaultvalue)` vs `collections.defaultdict(init_func)` --- a: When the key does not exist, `.get()` just returns the `defaultvalue`, `.setdefault()` sets `d[k] = default_value` and then returns it, `defaultdict` does the same, but initializes the value with `init_func`, it's called `defaultfactory` in docs. The `defaultdict` is considered a modern version of `.setdefault()`, since its name is much more obvious.


- q: How to overwrite key/value pairs in a dictionary with ones from another dictionary? --- a: `d.update(d2)`, returns `None`
- q: How to merge two dictionaries? --- a: 
<https://stackoverflow.com/questions/2799064/how-do-i-merge-dictionaries-together-in-python>
<https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression>

- q: What is `a_dict.pop()` for?
- q: What is `a_dict.popitem()` for?

- q: What is `iter(a_dict)` for?

- q: What is `dict.fromkeys()` for?

a_dict.copy()

# collections module

TODO: q:
ChainMap -- constructing `O(n)`, lookup `O(n)`
using dict update chain -- constructing `O(nm)`, lookup `O(1)`
This means that if you construct often and only perform a few lookups each time, or if M is big, ChainMap's lazy-construction approach works in your favor.
<http://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap/23441777#23441777>

q: create a named tuple --- a: `Point = collections.namedtuple('Point', 'x, y')`

## defaultdict

q: get a dict, which which counts distinct elements in a list --- a: `collections.Counter(list)`
q: get a dict with default value `'foo'` --- a: `collections.defaultdict(lambda: 'foo')`
q: get a dict with default value `0` --- a: `collections.defaultdict(int)`
q: get a dict with default value `[]` --- a: `collections.defaultdict(list)`
q: `dict` vs `collections.defaultdict` --- a: `d['non-existent key']` raises `KeyError`, `defaultdict` adds and returns a default value

## OrderedDict

<https://www.reddit.com/r/Python/comments/7jyluw/dict_knownordered_versus_ordereddict_an/>

- q: `dict` vs `collections.OrderedDict`? --- a: 
q: get a dictionary, which preserves the order in which its elements are added --- a: `od = collections.OrderedDict(); od['a'] = 1; od['b'] = 2`
q: how to initialize a `collections.OrderedDict()` with some content --- a: `OrderedDict( [('a', 1), ('b', 2), ...] )` is the right way, while `OrderedDict({'a': 1, 'b': 2, ...})` and `OrderedDict(a=1, b=2, ...)` are not (`kwargs` is a dict)
- q: What is `.popitem()` method of `OrderedDict` for? --- a: `.popitem(last=True)` behaves like a stack operation.

# sets

- q: Create a set of elements `1, 2, 3`. --- a: `st = {1, 2, 3}`
- q: Create an empty set. --- a: `st = set()`, not `{}`, because the latter is an empty dict.
- q: Create a set from a given list. --- a: `st = set([1, 2, 3])`
- q: Check if an element is in the set, and vice versa. --- a: `elt in st` and `elt not in st`
- q: Get number of elements in a set. --- a: `len(st)`
- q: Get min in a set. --- a: `min(st)`
- q: Get max in a set. --- a: `max(st)`
- q: What if we do `min()` or `max()` on empty set? ---a: Raises `ValueError`.
- q: Get an index of an element in a set. --- a: Sets do not support indexing, slicing, or other sequence-like behaviour.
- q: Get a slice of a set. --- a: Sets do not support indexing, slicing, or other sequence-like behaviour.
- q: Add an element to a set. --- a: `st.add(el)`
- q: Given a set, add elements from another set to it. --- a: `st |= another_set` or `st.update(another_set)`
- q: Given a set, add elements from a list to it. --- a: `st.update(lst)`, it accepts iterables; but not the `|=` operator, it accepts sets only.
- q: Given a set, leave only elements which are also in a given list. --- a: `a_set.intersection_update(lst)`, but not `&=`, it accepts sets only.
- q: `&=` is for `.intersection_update()`. What is `|=` for? --- a: Just `.update()`, there is no `.union_update()`.
- q: `a_set.add()` vs `a_set.update()`? --- a: `a_set.add(el)` adds one element, `a_set.update(another_set)` adds multiple elements from an iterable.
- q: Remove an element from a set. --- a: `st.remove(el)` or `a_set.discard(el)`. The former raises `KeyError` when the element doesn't exist, the latter just silently discards it.
- q: `a_set.remove(el)` vs `a_set.discard(el)`? --- a: `a_set.remove(el)` raises `KeyError` when the element doesn't exist, `a_set.discard(el)` just silently discards it.
- q: Remove all elements from a set. --- a: `st.clear()`
- q: What are set theory functions on sets? --- a: `a_set.union(b_set)` or `|`; `a_set.intersection(b_set)` or `&`; `a_set.difference(b_set)` or `-`; `a_set.symmetric_difference(b_set)` or `^` --- all of them are non-destructive.
- q: What does `a_set & b_set` do? --- a: Set intersection.
- q: What does `a_set | b_set` do? --- a: Set union.
- q: What does `a_set - b_set` do? --- a: Set difference.
- q: What does `a_set ^ b_set` do? --- a: Set symmetric difference.
- q: What operator is for set intersection? --- a: `a_set & b_set`
- q: What operator is for set union? --- a: `a_set | b_set`
- q: What operator is for set difference? --- a: `a_set - b_set`
- q: What operator is for set symmetric difference? --- a: `a_set ^ b_set`
- q: Are set theory operators or corresponding functions on sets destructive? --- a: Operators and functions like `&` and `.intersection()` are non-destructive; `&=` and `.intersection_update()` are destructive.
- q: What happens here? `set('abc') & 'bcd'`? --- a: Set theory operators require their arguments to be sets, `TypeError` is raised.
- q: What happens here? `set('abc').intersection(bcd')`? --- a: Set theory functions (but not operators) accept any iterable as argument.
- q: Do set theory operators and corresponding functions require their arguments to be sets? --- a: Set theory operators require their arguments to be sets, `TypeError` is raised. Set theory functions accept any iterable as argument.
- q: Check if a set is a subset or superset of another set. --- a: `a_set.issubset(another_set)` and `a_set.issuperset(another_set)`; `<`, `<=` and `>`, `>=` respectively.
- q: Check if two sets intersect. --- a: `a_set.isdisjoint(another_set)`
- q: Iterate over elements of a set. --- a: `for x in a_set: ...`; note, sets don't preserve order.
- q: In which order is a set is iterated here? `for x in a_set: ...`. --- a: The order is arbitraty, sets don't preserve order.
- q: `frozenset` vs `set`? --- a: The `frozenset` is an immutable set, it's hashable, so it can be a key in a `dict` and it can be an element of another `set`. It doesn't support operations like `.add`, `.remove`, `&=`, etc.
- q: What if we do `frozenset('abc') | set('bcd')`? --- a: Binary operations that mix `set` instances with `frozenset` return the type of the first operand.
- q: Can `set` and `frozenset` be compared? --- a: Yes, instances of `set` and `frozenset` are compared based on their members.


TODO: why do does `a_set.pop()` even exist? - q: What does `a_set.pop()` do? --- a: it pops an arbitrary element, pretty useless function.

TODO: a good question about `.update()`, `.intersection_update()`, `.difference_update()`, etc --- I don't like existing ones

TODO:
> Note, the elem argument to the __contains__(), remove(), and discard() methods may be a set. To support searching for an equivalent frozenset, the elem set is temporarily mutated during the search and then restored. During the search, the elem set should not be read or mutated since it does not have a meaningful value.


# strings

TODO: f-strings, new in 3.6

Strings `.join()` vs `+=` in a loop: <http://stackoverflow.com/questions/1349311/python-string-join-is-faster-than-but-whats-wrong-here/21964653#21964653>

TODO: unicode
TODO: a question on string immutability, can't use <https://docs.python.org/3/library/stdtypes.html#typesseq-mutable>
TODO: slice

misc:
- q: How are string literals written in python? --- a: `'Single'` or `"double"` or `'''three single'''` or `"""three double"""` quotes. Triple quoted strings may span multiple lines.
- q: What does this return if there is no character type in python: `s[0]`? --- a: Returns a string of length 1, `s[0]` is equivalent to `s[0:1]`.
- q: Get length of a string. --- a: `len(s)`
- q: What if `s = 'abc'` and we try to get `s[3]`? --- a: Raises `IndexError`.
- q: We can't do `a_string[::n] = a_char`, so how to write an equivalent? -- a: `''.join(a_char if i % n == 0 else c for i, c in enumerate(string))`
- q: What are `str.maketrans()` and `str.translate` for? --- a: For character substitution. `l->1, e->3, t->7` is done like this: `'leet'.translate(str.maketrans('let', '137')) == '1337'`

concatenation:
- q: Strings `.join()` vs `+=`. --- a: When you do not join strings in a loop, then pretty much the same. If you do, then this is `O(n)` vs `O(n^2)`. 
- q: Strings `.join()` vs `+=` in a loop. -- a:  `O(n)` vs `O(n^2)`. And although the `+=` is optimized in some cases, it's better to just never use it in loops, because in (pretty unpredictable) cases when it doesn't get optimized, we are going to have quadratic slowdowns. 
q: concatenate a list of strings --- a: `''.join( lst ) `
q: concatenate a list of strings and numbers into comma-separated string --- a: `', '.join( map(str, ['a', 1, 'b', 2]) ) == 'a, 1, b, 2'`
q: get a string of `n` minuses `-` --- a: `'-'*n`

substrings:
- q: `substr in a_string` vs `a_string.find(substr)` vs `a_string.index(substr)` --- a: `in` returns a boolean, `find()` returns index or `-1`, `index()` is quite like find, but raises `ValueError` when not found.
- q: check if a substring is in a string: --- a: `substring in a_string`, which is fastest, or `a_string.find(substring) != -1` or `a_string.index(substring)` and catch `ValueError`
- q: find index of a substring in a string --- a: `a_string[n:m].find(substring)` or `a_string.find(substring, n, m)`, which is faster; same with `.index()` with its `ValueError`
- q: Get a number of non-overlapping occurrences of a substring in a string. -- a: `str.count(sub)`, can also pass start and end positions.
- q: Replace all occurrences of a substring in a string. --- a: `'ababa'.replace('aba', '1') == '1ba'`
- q: Replace two first occurrences of a substring in a string. --- a: `'ababab'.replace('ab', '1', 2) == '11ab'`
- q: replace a character in string at given position --- a: `l = list('hello'); l[4]='!'; ''.join(l) == 'hell!'` or `s = '2+2'; s2 = s[:1] + '**' + s[2:]; s2 == '2**2'` --- the latter is faster
- q: Check if a string starts with `abc`. --- a: `'abcdefgh'.startswith('abc')`
- q: Check if a substring of a string from index `2` starts with `abc`. --- a: `'00abcdefgh'.startswith('abc', 2)`
- q: Check if a string ends with `fgh`. --- a: `'abcdefgh'.endswith('fgh')`
- q: Check if a substring of a string up to index `8` non-inclusive ends with `fgh`. --- a: `'abcdefgh00'.endswith('fgh', None, 8)`


reverse:
- q: reverse a string --- a: `a_string[::-1]`; the `reversed(s)` returns an iterator, so if you really want to use it despite the performance penalty, do `''.join(reversed(s))`.
- q: Why there is no `str.reverse()`? --- a: Because strings are immutable in python, we can't modify them, we can only construct new strings. Use the `s[::1]` or `''.join(reversed(s))`.
- q: What does `reversed(a_string)` return? --- a: An iterator object of type `reversed object`, not a string, so if you really want to use it despite the performance penalty, do `''.join(reversed(s))`. Otherwise, use `s[::-1]`.

adjustments:
- q: Get a string centered within width `w` with a minus `-` as padding char --- a: `'asdf'.center(w, '-')`
- q: Get a string left justified in a string of length `w`. --- a: `'abc'.ljust(4) == 'abc '`
- q: Get a string right justified in a string of length `w`. --- a: `'abc'.rjust(4) == ' abc'`
- q: `str.zfill()` vs `str.ljust()` --- a: The former correctly adds a sign before zeroes: `-00123` vs `00-123`.

strip:
- What is a function to trim a string? --- a: `a_str.strip()`, it also accepts multiple characters to strip: `title.rstrip(',.-')`.
- How to remove leading/trailing whitespaces from a string in Python? --- a: `a_str.rstrip()`, `lstrip()`
- Remove all trailing commas, periods and hyphens from a string. --- a: `title.rstrip(',.-')`

split:
- q: `partition` vs `split` --- a: The former returns a 3-tuple no matter what. Examples: `'a-b-c'.partition('-') == ('a', '-', 'b-c')` and `'a+b+c'.partition('-') == ('a+b+c', '', '')`.
- q: What does `''.partition('-')` return? --- a: `('', '', '')`
q: Split a string by whitespaces and trim results. --- a: `a_str.split()` --- when the `sep` argument is not specified or `None`, runs of consecutive whitespace are regarded as a single separator, so it splits and trims separated pieces.
q: Split a string into two pieces by whitespaces and trim results. --- a: Be careful, the following is not enough: `'  1   2   3  '.split(None, 1) == ['1', '2   3  ']`.
q: Split a string by comma and trim results. --- a: `[x.strip() for x in s.split(',')]` or `list(map(str.strip, s.split(',')))`
q: Split a string by comma without trimming. --- a: `'1,   2,   3'.split(',') == ['1', '   2', '   3']`
q: Split a `'1<>2<>3'` string using `<>` as a separator. --- a: `'1<>2<>3'.split('<>')`
q: Split a string into two pieces by comma without trimming. --- a: `'a, b, c, d'.split(',', maxsplit=1) == ['a', ' b, c, d']` or `'a, b, c, d'.partition(',') == ('a', ',', ' b, c, d')`.
q: Split a string from the end into two pieces by comma without trimming. --- a: `'a, b, c, d'.rsplit(',', maxsplit=1) == ['a, b, c', ' d']` or `rpartition`.
q: Split a multiline string into a list of lines. --- a: `s.splitlines()`, if the `keepends` arg is true, it keeps line breaks.
q: Split a multiline string into a list of lines, keeping line breaks. --- a: `s.splitlines(keepends=True)`
q: What do string split methods return when the string is empty? --- a: If a `sep` arg is not specified or `None`, an empty string is split into an empty list: `''.split() == []`; otherwise: `''.split(',') ==['']`.
q: What do string split methods return when the string is actually not split by given separator? --- a: An empty list containing the string. `'  a  '.split(',') == ['  a  ']`. If a `sep` arg is not specified or `None`, it also trims it: `'  a  '.split() == ['a']`


TODO: `str(bytes, encoding, errors)` is equivalent to `bytes.decode(encoding, errors)`
TODO: `str.encode(encoding="utf-8", errors="strict")`
TODO: `io.StringIO`, `io.BytesIO`, `tempfile.SpooledTemporaryFile`

{: .centered}
![python strings methods](./images/python.strings.001.svg)


## format

<https://docs.python.org/3/library/string.html#format-specification-mini-language>

``` Text
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  integer
grouping_option ::=  "_" | ","
precision       ::=  integer
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

``` python
'hello, {}'.format(username)

'{0} is better than {1}'.format('emacs', 'vim')
'{1} is better than {0}'.format('emacs', 'vim')
'{0} {2} {1} {2}'.format(*tpl)

'{0!s}'.format(an_obj)   # calls str() on the argument
'{0!r}'.format(an_obj)   # calls repr() on the argument
'{0!a}'.format(an_obj)   # calls ascii() on the argument
'repr() shows quotes: {0!r}; str() doesn't: {0!s}'.format('test')

'{first} {last}'.format(first='John', last='Smith')
'{first} {last}'.format(**{'first': 'John', 'last': 'Smith'})

'{0.real}, {0.imag}'.format(1-1j)

coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)


'{:f}'.format(1) == '1.000000'
'{:.1f} {}'.format(698.243, 'GB') == '698.2 GB'
'{0} {0:g}'.format(1.0)

'{:+f}; {:+f}'.format(3.14, -3.14) == '+3.140000; -3.140000'   # always show sign
'{: f}; {: f}'.format(3.14, -3.14) == ' 3.140000; -3.140000'

'{:-f}; {:-f}'.format(3.14, -3.14)    # default, same as just {:f}

'{:#5x}'.format(15) == '  0xf'
'{:#5X}'.format(15) == '  0XF'

map('%Y-%m-%d'.format, lst)
```

``` python
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'

import locale
locale.setlocale(locale.LC_ALL, 'en_US')   ## in this example we set a locale to see the difference:
'{:n}'.format(10**6) == '1,000,000'
locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())

'{:.1%}'.format(0.33) == '33.0%'
'{:.3}'.format('xylophone') == 'xyl'

'{:{fill}{align}{width}}'.format('hello', fill='*', align='^', width=11) == '***hello***'
```

for formatting dates see the dates section

not covered: besides `<`, `>`, and `^` alignment options there is another one, `=`, for putting the sign before fill chars: `'{:0=5}'.format(-1) == '-0001'`
not covered: printing binary and octal
Note, we don't have questions for formatting floats with reserved space for sign, we only have question about meaning of those options: `'{:+f} {: f} {:-f}'`.

TODO: `print(..., sep=', ')`
TODO: `print(..., end=' ')`

basics:
- q: `s.format()` vs `%`-interpolation --- a: Just use the `.format()`, the `%`-style formatting is left in the language for backward compatibility.
- q: TODO: Explicit and implicit positional arguments. --- a: Implicit: `'hello, {}'.format(username)`; explicit: `'{1} is cooler than {0}'.format('vim', 'emacs')`.
- q: What happens when we mix replacement fields like this: `'{} {1}'.format(1, 2)`? --- a: `ValueError: cannot switch from automatic field numbering to manual field specification`
- q: How to `str.format()` curly braces? --- a: Just double them: `'left curly brace:\{\{, and the right one: \}\}'.format()`
- q: named arguments --- a: `'{first} {last}'.format(first='John', last='Smith')` and `'{first} {last}'.format( **{'first': 'John', 'last': 'Smith'} )`
- q: accessing argument's attributes --- a: `'{0.real}, {0.imag}'.format(1-1j) == '1.0, -1.0'`
- q: accessing argument's items --- a: `'X: {0[0]};  Y: {0[1]}'.format( (2, 3) ) == 'X: 2;  Y: 3'`
- q: How to format arguments out of order they come? --- a: `'{1} is cooler than {0}'.format('vim', 'emacs')`
- q: How precision affects formatting of strings? `'{:.3}'.format('xylophone')` --- a: `'{:.3}'.format('xylophone') == 'xyl'`
- q: How to format only the first n chars of a string usign `str.format()`? --- a: `'{:.3}'.format('xylophone') == 'xyl'`

numbers:
- q: `str.format()`: `'{}'` vs `'{:s}'` for strings? --- a: These are equivalent.
- q: `str.format()`: `'{}'` vs `'{:d}'` for integers? --- a: These are equivalent.

- q: `'{}'` vs `'{:f}'` vs `'{:g}'` for floats? --- a: They are similar, except that with the former the fixed-point notation, when used, has at least one digit past the decimal point. The default precision is as high as needed to represent the particular value. The overall effect is to match the output of str() as altered by the other format modifiers.
- q: `'{}'` vs `'{:f}'` vs `'{:g}'` (and vs `'{:n}'`) for formatting floating point numbers? --- TODO, `'{0} {0:g}'.format(1.0) == '1.0 1'`

- q: How to `str.format()` a number with comma as thousands separator? --- a: `'{:,}'.format(10**6)`
- q: How to `str.format()` a number usign current locale to insert number separator characters? --- a: `'{:n}'.format(10**6)`
- q: What is `'{:e}'` for? --- a: Exponent notation. For example: `'{:e}'.format(0.12345) == '1.234500e-01'`

- q: `'{:.3f}'` vs `'{:.3g}'` --- a: `'{:.3f}'` indicates number of digits after the decimal point, `'{:.3g}'` indicates number of digits overall, before and after the decimal point.
- q: How to print a float with precision? --- a: TODO

- q: What is this shit? `'{:%}'` --- a: Percentage. Multiplies the number by 100 and displays in fixed (`'f'`) format, followed by a percent sign: `'{:%}'.format(0.42) == '42.000000%'` --- you probably want to use precision, `'{:.1%}'`
- q: How to format a float as percents when it represents a ratio? --- a: `'{:.1%}'.format(1/3) == '33.3%'` --- you probably want to use precision, because it displays floats in fixed (`f`) format with default precision 6.

- q: What do these mean? `'{:+f} {: f} {:-f}'` --- a: `'{:-f}'` is same as `'{:f}'`, `'{:+f}'` is for always showing the sign, `'{: f}'` preserves space: `'{: f}; {: f}'.format(3.14, -3.14) == ' 3.140000; -3.140000'`.

- q: How to print a hex number with and without `0x` prefix? --- a: `'with: {0:#x}; without: {0:x}'.format(15) == 'with: 0xf; without: f'` --- the octothorp `#` does alternate behaviour.
- q: What does `'{:#x}'` mean? --- a: Hexadecimal with the `0x` prefix.
- q: What if we use capital letters for presentation types? `'{:F}'`, `'{:G}'`, `'{:E}'`, `'{:#X}'`? --- It formats `nan`, `inf`, `e`, etc, in uppercase; for hexadecimals it also formats the prefix `'0X'` uppercase.

alignment:
- q: How to align a string to the left when using `str.format()`? --- a: `'{:<3}'.format('l') == 'l  '`
- q: How to align a string to the right when using `str.format()`? --- a: `'{:>3}'.format('r') =='  r'`
- q: How to align a string at the center when using `str.format()`? --- a: `'{:^5}'.format('c') == '  c  '`
- q: How to use a fill character when aligning a string using `str.format()`? --- a: `'{:*^5}'.format('c') == '**c**'`



misc:
- q: `str()` vs `repr()` --- a: `repr()` is meant to generate representations which can be read by the interpreter, `str()` is for end-users.
- q: What are outputs of `str('hello')` and `repr('hello')`? --- a: `'hello'` and `"'hello'"`
- q: What is `ascii()` for? --- It's the `repr()` with escaped non-ASCII characters.
- q: What is conversion flag to call `repr()` on an argument of `str.format()`? --- a: `'{!r}'.format('hello') == "'hello'"`
- q: What is conversion flag to call `str()` on an argument of `str.format()`? --- a: `'{!s}'.format('hello') == 'hello'`
- q: What does this mean? `{!r}.format(whatever)` --- a: Calls `repr()` on the argument.
- q: What does this mean? `{!s}.format(whatever)` --- a: Calls `str()` on the argument.
- q: `str.format(**dct)` vs `str.format_map(defaultdct)`? --- a: Unpacking produces a `dict`, so this fails if it doesn't contain a needed key. But with `.format_map()` we can use `defaultdict`.
TODO: `str.format_map` example
- q: Nested replacement fields. --- a: `'{:{fill}{align}{width}}'.format('hello', fill='*', align='^', width=11) == '***hello***'`





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
q: `zip()` two sequences until the longest one is exhauseted, with a given value for missing bits --- a: `itertools.zip_longest(lst1, lst2, fillvalue=None)`
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


