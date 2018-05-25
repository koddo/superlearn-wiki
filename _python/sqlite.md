---
title:   "Sqlite"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}

# sqlite3

<https://www.pythoncentral.io/introduction-to-sqlite-in-python/>

``` Python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(path_to_file)) as conn:
    with closing(conn.cursor()) as cur:
        with conn: # auto-commits
            cur.execute(statement)
```

``` Python
c.execute('select * from stocks where symbol=?', t)
```

TODO: importing csv into sqlite using `.separator` and `.import` sqlite special functions: <https://cs.stanford.edu/people/widom/cs145/sqlite/SQLiteLoad.html>
TODO: read <http://charlesleifer.com/blog/going-fast-with-sqlite-and-python/>
TODO: types adapters and converters
TODO: difference between `PARSE_COLNAMES` and `PARSE_DECLTYPES`


How to use sqlite with context managers?


<iframe class="autoresize" src="{{ site.superlearn_url }}/ht/asdf2?deckname=python -- sqlite">
    <p>Your browser does not support iframes.</p>
</iframe>



{% include source_code.html path='src/sqlite.py' lang='Python' %}



