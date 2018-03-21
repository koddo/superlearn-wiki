---
title:   "Drafts"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}

# ignore indentation and blank lines when seeing diffs

<https://coderwall.com/p/crj69a/from-a-useless-git-diff-to-a-useful-one>

$ git diff --ignore-space-at-eol -b -w --ignore-blank-lines [commit] ...

--ignore-space-at-eol
-b = --ignore-space-change
-w = --ignore-all-space
--ignore-blank-lines

# misc

Эффективное использование Github: <https://habrahabr.ru/company/2gis/blog/306166/>

- q: quickly see an old version of a file --- a: $ git show REVISION:path/to/file

git annex for archiving
