---
title:   "Git"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# tutorials and cheatsheets

Interactive tutorials:
<https://onlywei.github.io/explain-git-with-d3/#commit>
<https://learngitbranching.js.org/>
<https://veerasundar.com/blog/2018/03/gitflow-animated/>

Interactive cheatsheet: <https://ndpsoftware.com/git-cheatsheet.html#loc=stash;>
Fixing a mess cheatsheet: <http://justinhileman.info/article/git-pretty/git-pretty.png>
<https://www.quora.com/What-is-the-best-Git-cheat-sheet>

<https://www.atlassian.com/git/tutorials/syncing>
<https://marklodato.github.io/visual-git-guide/index-en.html>

<https://maryrosecook.com/blog/post/git-from-the-inside-out>, <http://gitlet.maryrosecook.com/docs/gitlet.html>

<http://think-like-a-git.net/tldr.html>
<http://ftp.newartisans.com/pub/git.from.bottom.up.pdf>

# undo

<https://stackoverflow.com/questions/8358035/whats-the-difference-between-git-revert-checkout-and-reset#8358039>
<https://www.atlassian.com/git/tutorials/undoing-changes>

TODO: `git reset` is a _dangerous_ method, for local use only, never reset snapshots that have been shared already

- q: `revert` vs `checkout` vs `reset` for undo?
- q: `revert` vs `reset` for undoing an old commit? --- a: `revert` can undo a single arbitraty commit, but adds a new undoing commit; `reset` can only remove a commit from history with all commits that occur after it.
- q: Which of `revert` and `reset` is for undoing local changes, and which is for undoing a published commit?

- q: Unmodify a modified file? -- a: `git checkout -- <file>`

- q: How to unstage a staged file? -- a: `git reset <file>`
- q: How to unstage everything? -- a: `git reset`
- q: How to say fuck it and revert everything (branch tip, working dir content, etc)? -- a: `git reset --hard [<commit>]`
TODO: `git reset <commit>`, actually try it
- q: Is it ok to `git reset` a public commits? -- a: No.

- q: How to remove untracked files and directories? -- a: `git clean -fd`, be cautios. Without `--force` it refuses to clean (unless configured otherwise).
- q: What is `git clean` for? -- a: To remove untracked files, be cautios.
- q: How to dry run `git clean`? -- a: `git clean -n`

- q: How to change a most recent commit message? -- a: `git commit --amend`; don't amend public commits.
- q: How to add a file to a most recent local commit? -- a: `git add file && git commit --amend`
- q: Is it ok to change commit message of public commits? -- a: No.

`git checkout` does check out files, or commits, or branches
`git revert` 
`git reset`

TODO: Consequences of `git push --force`? <https://stackoverflow.com/questions/21259585/other-consequences-of-git-push-force>

- q: Is it ok to rebase public commits? -- a: No.

# misc

<http://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/>

- q: What is a bare repository? --- a: To have central repository the only way it is to have a bare repository. It has no working tree, i.e., your project files. It only contains revision history, the contents of `.git/`



<https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git>
<http://think-like-a-git.net/sections/graphs-and-git/visualizing-your-git-repository.html>

- q: What happens if you checkout something without committing changes? --- a? It doesn't allow you to checkout without committing or stashing.
- q: What are the working dir, the index?
- q: How to move head to a branch or a commit or a tag? --- a: `git checkout <ref>`

- q: How to create a branch? --- a: `git branch [name]` creates a branch at the head.
- q: How to create and switch to a branch with a single command? --- a: `git checkout -b [name]`
- q: How to list branches? --- a: `--list <pattern>` or empty argument list for local branches, `-r` for remote ones, `-a` for both local and remote ones.

- q: How to reassign a branch ref to another commit? --- a: `git branch --force [name] [commit]`
- q: What is `git branch --force [name] [commit]` for? --- a: ask community, learngitbranching-rampup3, <https://stackoverflow.com/questions/28149804/difference-between-git-branch-f-branch-name-hash-and-git-checkout-branc/28150031>


- q: `git revert`vs `git reset` --- a: learngitbranching-rampup4

- q: What is `git cherry-pick` for? --- a: learngitbranching-move1, `git cherry-pick` copies a commit from anywhere in the tree onto the head (except ancestors).
- q: What is rebase? --- a: it's like a massive cherry-picking from one branch to another --- a: <http://think-like-a-git.net/sections/rebase-from-the-ground-up/using-git-cherry-pick-to-simulate-git-rebase.html>, <http://think-like-a-git.net/sections/rebase-from-the-ground-up/a-helpful-mnemonic-for-git-rebase-arguments.html>

`git rebase` won't do anything if you try to rebase to it's ancestor, but `git rebase -i` will be equivalent to cherry-picking

- q: What if you want to merge branches after cherry-picking? --- a: Avoid duplicating by using rebase:
<https://stackoverflow.com/questions/14486122/how-does-git-merge-after-cherry-pick-work/44966513#44966513>
<https://stackoverflow.com/questions/20380013/git-merge-strategies-spaces-make-default-shows-no-conflict-and-bring-unexpected>

<https://gcbenison.wordpress.com/2012/01/17/git-bugfix-branches-choose-the-root-wisely/>
<https://medium.com/@porteneuve/getting-solid-at-git-rebase-vs-merge-4fa1a48c53aa>
<https://stackoverflow.com/questions/34504807/git-flow-vs-cherry-picks>

- q: What is `git fetch` for? --- a: It makes our local graph synched to the remote one. And updates remote branches, like `origin/master`. It doesn't touch anything local: working dir, index, branches, etc.
- q: What is `git pull` for? --- a: It's essantially a shorthand for `git fetch; git merge`.
- q: What is `git pull --rebase` for? --- a: It's essantially a shorthand for `git fetch; git rebase`.
- q: `push.default`?

- q: What is `git branch -u origin/master foo` or `git checkout --track origin/serverfix` for? --- a: To set the `foo` to track the `origin/master`.
- q: How to create a remove branch? --- a: checkout a branch and then `git puth --set-upstream origin branch-name` or `git branch --set-upstream-to=origin/foo foo`

- q: What is `git reflog` for?

- q: `git fetch origin :bar` creates a local branch, `git push origin :foo` removes a remote one

when rebasing, as long as you don't force push you can't mess anything, just reset to origin/master
maybe also `git tag pre-rebase-x; do the rebase;`


First I try to rebase, but I have any conflicts, I abort the rebase and do merge instead.

A dog: `git log --all --decorate --oneline --graph` --- <https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs/35075021#35075021>

{: .centered}
![python deques](./images/git.graph.001.svg)

- q: How to see changes? --- a: `git diff` or `git diff --cached`
- q: How write a commit message? --- a: `git commit -m '...'` --- a short summary followed by a blank line and a thorough description

```
git add
git add --all
git commit -a

git merge bname

git branch [name]
git checkout [ref]
git checkout -b [name]

git branch --force <name> [commit]
git branch -d crazy-idea
-d = --delete
-D = --delete --force

git revert
git reset

git rebase <dest> <commit>
git rebase -i
git cherry-pick

git tag [tag] [commit]
git describe <ref>

HEAD~^2~

git diff
git diff --cache
git status

gitk HEAD...FETCH_HEAD
git show <commit>

git stash??
```











