import sqlite3
from contextlib import closing
import datetime

with closing(sqlite3.connect(":memory:",
                             detect_types=sqlite3.PARSE_DECLTYPES)) as conn:
    conn.row_factory = sqlite3.Row     # access fields by name
    with closing(conn.cursor()) as cur:
        with conn:    # auto-commit or -rollback
            cur.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
            purchases = [
                ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
            cur.executemany('insert into stocks values (?,?,?,?,?)', purchases)
            rows = cur.execute('select * from stocks order by price')
            print(rows)
            for r in rows:
                print(r)
                
            cur.execute('select * from stocks where symbol=?', ('RHAT',))
            print(cur.fetchone())
            cur.execute('select * from stocks where symbol=?', ('IBM',))
            r = cur.fetchone()
            print(type(r))
            
            cur.execute("create table test(d date, ts timestamp)")

            today = datetime.date.today()
            now = datetime.datetime.now()

            cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
            cur.execute("select d, ts from test")
            row = cur.fetchone()
            print(today, "=>", row['d'], type(row['d']))
            print(now, "=>", row['ts'], type(row['ts']))

            
            cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
            row = cur.fetchone()
            print("current_date", row['d'], type(row['d']))
            print("current_timestamp", row['ts'], type(row['ts']))
            
