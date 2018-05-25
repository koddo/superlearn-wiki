---
title:   "Misc"
layout:  collection_page

---

# inkscape

## grid

![asdf](./images/Screenshot 2016-08-28 14.53.08.png)

<div class="ryctoic-questions" markdown="1">
- q: create a grid 6x6 --- a: create a rectangle 120x120, then `extensions -> render -> grids -> grid`, set `spacing=20`
</div>


# command line

less:
`p` --- beginning of file
`G` --- end of file
`/` --- search, `n` and `N` are next and prev

# licenses

<https://www.reddit.com/r/Python/comments/2z4k2q/which_license_you_would_choose_when_you_opensouce/>

# erlang

TODO: Erlang Types Book --- <http://erlang-types-book.com/> --- doesn't work
TODO: <https://github.com/zkessin/testing-erlang-book>
TODO: <https://medium.com/@jlouis666/breaking-erlang-maps-1-31952b8729e6>, <https://medium.com/@jlouis666/breaking-erlang-maps-2-362730a91400>
TODO: <http://blog.listincomprehension.com/2010/03/spoofing-erlang-distribution-protocol.html>
TODO: buy <https://ninenines.eu/articles/erlanger-playbook/>

<https://www.reddit.com/r/erlang/comments/6417tj/thebeambook_a_description_of_the_erlang_runtime/>
<https://github.com/happi/theBeamBook>

demo of search engine in erlang -- <https://www.reddit.com/r/erlang/comments/2nalrb/erlang_search_engine_demo_of_the_wand_max_score/>
Testing Poolboy, Concuerror basics -- http://concuerror.com/tutorials/poolboy-example/

<http://videlalvaro.github.io/2013/09/rabbitmq-internals-credit-flow-for-erlang-processes.html>

<https://github.com/0xAX/erlang-bookmarks/blob/master/ErlangBookmarks.md>

<http://marcelog.github.io/articles/erlang_link_vs_monitor_difference.html>

<https://stackoverflow.com/questions/600642/how-do-i-concatenate-two-binaries-in-erlang>

erlang battleground
https://medium.com/erlang-battleground/call-me-maybe-28671e6b92f4
https://medium.com/erlang-battleground/advanced-list-incomprehensions-6957863dfb4f

# garbage collector

<https://spin.atomicobject.com/2014/09/03/visualizing-garbage-collection-algorithms/>, <https://github.com/kenfox/gc-viz>


# docker

<https://sysdig.com/blog/7-docker-security-vulnerabilities/>

there are container vulnerability scanners

# ansible

Run a single task:

```
ansible-playbook playbook-configure-debian.yml -i '1.1.1.1,' --step --start-at-task='build dockerfiles'
```


# functional programming


Löb and möb: strange loops in Haskell -- <https://github.com/quchen/articles/blob/master/loeb-moeb.md>

Списки из lambda-функций -- <https://habrahabr.ru/post/176233/>

# bash

<https://en.wikibooks.org/wiki/Bash_Shell_Scripting#Subshells.2C_environment_variables.2C_and_scope>





# regular expressions

<http://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html>
# first aid

# http

<https://www.quora.com/Why-are-PUT-and-DELETE-no-longer-supported-in-HTML5-forms>

https://stackoverflow.com/questions/283752/refresh-http-header, http://www.securiteam.com/securityreviews/6Z00320HFQ.html
https://stackoverflow.com/questions/4584728/redirecting-with-a-201-created
browsers do not redirect to the location from 201 response, it has to have a link to new resource or to redirect there
201 created with a `Refresh: 0;url=/whatever/etc` header works, but 303 see other should be used instead, because refresh breaks back button
i.e., for forms 303 = 201+refresh, https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.5


http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
