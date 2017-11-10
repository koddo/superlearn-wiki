---
title:   "Github"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}



# github

<https://opensource.guide>

<https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project>
<https://stackoverflow.com/questions/14680711/how-to-do-a-github-pull-request>

Эффективное использование Github -- <https://habrahabr.ru/company/2gis/blog/306166/>

## pull requests

origin vs upstream: <https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github>
forks are clones on the server side of github, which you interact with: <https://stackoverflow.com/questions/6286571/are-git-forks-actually-git-clones>

from <https://stackoverflow.com/questions/3611256/forking-vs-branching-in-github/3611349#comment13305892_3611349>:

> Honestly, even if you don't have to, it is always a good idea to have a sacred repo that is writable only for senior developers, team leads or other "trusted" people. All other team members should work in their forks (~sandboxes) and contribute their changes in the form of pull request. Since DVCS makes it possible, we adapted it as a "best practice" and successfully use this even in the smallest projects.

TODO: automate creating of pull requests via api: <https://developer.github.com/v3/pulls/#create-a-pull-request>

- q: Origin vs upstream?
- q: Forks vs clones?
- q: Why it's better to isolate modifications in a branch instead of creating a pull request from master?
- q: After you fork, how to create a topic branch? -- a: `git checkout -b <branch-name>`
- q: How to push the topic branch to your fork? -- a: `git push origin <branch-name>`
TODO: Centralized workflow vs integration-manager workflow: <https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#_integration_manager>; what happens behind the scenes when you accept the pr? The upstream adds the fork as a remote and then fetches and merges the commit from there.
- q: Github pull request workflow? -- a: fork and create a branch, edit, commit and push the branch to origin, open a pull request

## workflow

fork and create a topic branch
edit
commit and push the branch to origin
open a pull request, discuss, continue committing until it's merged or closed

