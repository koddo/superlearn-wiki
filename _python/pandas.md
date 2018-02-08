---
title:   "Pandas"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}

# helloworld

```
len(df)
df.head(), df.tail()
df['column'], df.column

s + value
s1 + s2
s.notnull(), s.isnull()

df.sort_values(ascending=False)
s.sort_values(by='col')

df[ df.col == value ]
df[ (v1 < df.c) & (df.c < v2) ]

df[ ~df['type'].isin(['actor', 'actress']) ]   # plain not in doesn't work
df = df[ df['title'].str.startswith('Hamlet') ]

df[ ['col1', 'col2'] ]

s.value_counts().sort_index()   # dropna=True by default
# it's like s.groupby('col').size()

s.str.len()
s.str.contains()
s.str.startswith()

s = s.unique()
s = s.sort_values(by=['year', 'name'])


df.plot()
s.plot(kind='bar')
titles.year.value_count().sort_index().plot()

%%time df[ df.title == 'Hamlet' ]
c = cast.set_index(['title']).sort_index()
c.loc('Hamlet')
c = cast.set_index(['title', 'year']).sort_index()
c.loc['Hamlet'].loc['1972']
c.loc[('Hamlet', '1972')]
reset_index

df.groupby('col')
df.groupby(['col1', 'col2])
.size(), .min(), .max(), .mean(), .agg(['min', 'max'])


???:
df.unstack()
df.stack()

df.fillna()
```



```
  len(df)       series + value    df[df.c == value]
  df.head()     series + series2  df[(df.c >= value) & (df.d < value)]
  df.tail()     series.notnull()  df[(df.c < value) | (df.d != value)]
  df.COLUMN     series.isnull()   df.sort_values('column')
  df['COLUMN']  series.order()    df.sort_values(['column1', 'column2'])

  s.str.len()        s.value_counts()
  s.str.contains()   s.sort_index()    df[['column1', 'column2']]
  s.str.startswith() s.plot(...)       df.plot(x='a', y='b', kind='bar')

  df.set_index('a').sort_index()        df.loc['value']
  df.set_index(['a', 'b']).sort_index() df.loc[('v','u')]
  df.groupby('column')                  .size() .mean() .min() .max()
  df.groupby(['column1', 'column2'])    .agg(['min', 'max'])

  df.unstack()      s.dt.year       df.merge(df2, how='outer', ...)
  df.stack()        s.dt.month      df.rename(columns={'a': 'y', 'b': 'z'})
  df.fillna(value)  s.dt.day        pd.concat([df1, df2])
  s.fillna(value)   s.dt.dayofweek
```
