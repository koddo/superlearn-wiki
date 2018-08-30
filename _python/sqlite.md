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

```
conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('file:path/to/database?mode=ro', uri=True)
```

```
# to access fields by name instead of by index
conn.row_factory = sqlite3.Row
```

```
# to have a timestamp type corresponding to datetime
sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
...
cur.execute('create table test(d date, ts timestamp)')
cur.execute('insert into test(d, ts) values (?, ?)', (today, now))
cur.execute('select d, ts from test')
cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
```

```
## https://stackoverflow.com/questions/16936608/storing-bools-in-sqlite-database

sqlite3.register_adapter(bool, int)
sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))

## or

sqlite3.register_converter("BOOLEAN", lambda v: v != '0')
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



