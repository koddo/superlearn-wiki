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



- q: How to align a string to the left when using `str.format()`? --- a: `'{:<3}'.format('l') == 'l  '`
- q: How to align a string to the right when using `str.format()`? --- a: `'{:>3}'.format('r') =='  r'`
- q: How to align a string at the center when using `str.format()`? --- a: `'{:^5}'.format('c') == '  c  '`
- q: How to use a fill character when aligning a string using `str.format()`? --- a: `'{:*^5}'.format('c') == '**c**'`

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings adjustments">
    <p>Your browser does not support iframes.</p>
</iframe>


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

<https://docs.python.org/3/reference/lexical_analysis.html#f-strings>

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings f-strings">
    <p>Your browser does not support iframes.</p>
</iframe>


# format

<iframe class="autoresize" src="http://superlearn.it/ht/asdf2?deckname=python -- strings format">
    <p>Your browser does not support iframes.</p>
</iframe>



