---
title:   "Strings and format"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}




# strings

TODO: unicode
TODO: `str(bytes, encoding, errors)` is equivalent to `bytes.decode(encoding, errors)`
TODO: `str.encode(encoding="utf-8", errors="strict")`
TODO: `io.StringIO`, `io.BytesIO`, `tempfile.SpooledTemporaryFile`

TODO: `.casefold()`, `lower()`, `.upper()`, `.swapcase()`, `.capitalize()`, etc
- q: `a_str.capitalize()` vs `a_str.title()` vs `string.capswords(s, sep=None)` class method. --- a: There's no simple solution to make words in a string capitalized: `.capitalize()` only does capitalize the very first character of the string (if it's a space, it does nothing); `.title()` makes all consequtive letters in a string capitalized `"they're bill's friends from the UK".title() == "They'Re Bill'S Friends From The Uk"`; <https://docs.python.org/3/library/string.html#string.capwords>

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

TODO: `expandtabs`


Strings `.join()` vs `+=` in a loop: <http://stackoverflow.com/questions/1349311/python-string-join-is-faster-than-but-whats-wrong-here/21964653#21964653>

Strings are immutable, we can't use these operations on them: <https://docs.python.org/3/library/stdtypes.html#typesseq-mutable>

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings concatenation">
    <p>Your browser does not support iframes.</p>
</iframe>


<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings substrings">
    <p>Your browser does not support iframes.</p>
</iframe>


<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings reverse">
    <p>Your browser does not support iframes.</p>
</iframe>

Be careful with the `sep` argument of `a_str.split()`: if a `sep` arg is not specified or `None`, an empty string is split into an empty list: `''.split() == []`; otherwise: `''.split(',') ==['']`.
When it's not actually split: returns a list containing the string. `'  a  '.split(',') == ['  a  ']`; if a `sep` arg is not specified or `None`, it also trims it: `'  a  '.split() == ['a']`

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings split and trim">
    <p>Your browser does not support iframes.</p>
</iframe>


<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings adjustments">
    <p>Your browser does not support iframes.</p>
</iframe>


misc:
- q: How are string literals written in python? --- a: `'Single'` or `"double"` or `'''three single'''` or `"""three double"""` quotes. Triple quoted strings may span multiple lines.
- q: Is there a character type in python? --- a: No, only strings. `s[0]` is equivalent to `s[0:1]` substring.
- q: What does this return as there is no character type in python: `s[0]`? --- a: Returns a string of length 1, `s[0]` is equivalent to `s[0:1]` substring.
- q: Get length of a string. --- a: `len(s)`
- q: What if `s = 'abc'` and we try to get `s[3]`? --- a: Raises `IndexError`.
- q: We can't do `a_string[::n] = a_char`, so how to write an equivalent? -- a: `''.join(a_char if i % n == 0 else c for i, c in enumerate(a_string))`
- q: What are `str.maketrans()` and `str.translate` for? --- a: For character substitution. `l->1, e->3, t->7` is done like this: `'leet'.translate(str.maketrans('let', '137')) == '1337'`
- q: Can we mutate strings? What operations are supported? --- a: No, strings are immutable. `s[i] = l`, `s.append(l)`, `s.insert(i, l)`, `s.reverse()`, `s.remove(l)`, etc are not supported.

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings">
    <p>Your browser does not support iframes.</p>
</iframe>



{: .centered}
![python strings methods](./images/python.strings.001.svg)

# f-strings

<https://www.python.org/dev/peps/pep-0498/#expression-evaluation>:

> The expressions that are extracted from the string are evaluated in the context where the f-string appeared. This means the expression has full access to local and global variables. Any valid Python expression can be used, including function and method calls.

Gotcha: we can't have `'\n'` in a expression part of an f-string, e.g.: `f"{'\n'.join(l)}"` won't work.

Our choises are:

- have it joined outside: `s = '\n'.join(l); f"{s}"`
- `newline = '\n'; f'{newline.join(l)}'`
- `'{}'.format('\n'.join(l))`
- `print(*l, sep='\n')`

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings f-strings">
    <p>Your browser does not support iframes.</p>
</iframe>
