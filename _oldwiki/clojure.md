---
title:   "Clojure"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}



# hara.zip

hara.zip vs clojure.zip <https://www.reddit.com/r/Clojure/comments/55t3lg/why_clojurezip_sucks/>

# misc

`PersistentQueue`

<https://lambdaisland.com/blog/11-02-2017-re-frame-form-1-subscriptions> --- cooler looking subscriptions: `:checked (<sub [:todos/all-complete?])`

<http://stackoverflow.com/questions/3008411/clojure-consseq-vs-conjlist>

<https://stuartsierra.com/tag/dos-and-donts>

<http://stackoverflow.com/questions/26050540/what-is-the-difference-between-the-hash-map-and-array-map-in-clojure>

The best way to handle nil: <https://bsima.me/clog/robust-clojure-nil.html>

- q: how to flatten one level of seqs `((...) (...) (...))`? -- a: `(apply concat ...)`


<http://mishadoff.com/blog/clojure-design-patterns/>
<https://github.com/bbatsov/clojure-style-guide>

# re-frame

better re-frame subscriptions:
https://github.com/Day8/re-frame/issues/170#issuecomment-240940371

http://grokbase.com/t/gg/clojure/149520vdab/statechart-hierarchical-fsm-implementation
https://github.com/Day8/re-frame/tree/develop/docs


https://github.com/yelouafi/redux-saga/issues/5
https://github.com/yelouafi/redux-saga/issues/8
https://github.com/yelouafi/redux-saga/issues/22









# clojurescript, re-frame

``` Shell
$ [[ ! -f download ]] && wget https://gist.github.com/koddo/c5f2b74d9f33e023f02cf735b66a4127/download && unzip -j download && rm download
$ docker-compose --project-name theproject run --rm --no-deps figwheel lein new re-frame theproject --to-dir . -- +cider +routes +re-frisk
$ docker-compose --project-name theproject run --rm --no-deps figwheel lein deps
$ docker-compose --project-name theproject run --rm --no-deps gulp npm install
$ mkdir less && mkdir resources/public/css && cat <<EOF > less/site.less
body {
    color:red;
}
EOF
```

top figwheel conf: `:repl false :nrepl-port 7888`
figwheel section of dev build configuration in project.clj: `:websocket-host :js-client-host`
head of `index.html`: `<link href="css/site.css" rel="stylesheet" type="text/css">`

</ssh:alex@debian.local:~/>
if you want polling instead of fsevents, add this to the top figwheel conf: `:hawk-options {:watcher :polling}`

``` Shell
docker-compose --project-name theproject up
```

<http://theproject_figwheel.dev.dnsdock:3449/>

## notes

Sticking to safe options and using gulp to generate `css` from `less`, `lein-less` has to be run separately anyway.

TODO: re-frame template `+test`, usage
TODO: nginx https termination, nginx static files





# another way: clojurescript, re-frame

see changes
<https://github.com/Day8/re-frame-template/search?q=lein-template>
<https://clojars.org/re-frame/lein-template>
<https://github.com/Day8/re-frame-template/releases>
<https://github.com/Day8/re-frame-template/compare/v0.2.2-7...v0.2.4>

<http://www.inoreader.com/folder/updates%20--%20cljs>


``` Shell
$ git clone --origin boilerplate repo.git
$ git remote add origin ssh://git@github.com/user/new_proj.git
```



# misc

<https://www.reddit.com/r/Clojure/comments/73tpoe/clojure_gotchas_contains_and_associative/>
<https://lambdaisland.com/blog/02-10-2017-clojure-gotchas-associative-contains>
