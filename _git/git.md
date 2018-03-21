---
title:   "Git"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# tutorials and cheatsheets

Interactive tutorials:
<https://onlywei.github.io/explain-git-with-d3/#commit>
<https://marklodato.github.io/visual-git-guide/index-en.html>

Interactive cheatsheet: <https://ndpsoftware.com/git-cheatsheet.html#loc=stash;>
Fixing a mess cheatsheet: <http://justinhileman.info/article/git-pretty/git-pretty.png>
<https://www.quora.com/What-is-the-best-Git-cheat-sheet>

<https://www.atlassian.com/git/tutorials/syncing>

<https://maryrosecook.com/blog/post/git-from-the-inside-out>, <http://gitlet.maryrosecook.com/docs/gitlet.html>

<http://think-like-a-git.net/tldr.html>

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

- q: What happens if you checkout a branch without committing changes? --- a? It doesn't allow you to checkout without committing or stashing.
- q: What is the index?


- q: How to create a branch? --- a: `git branch [name]`
- q: How to switch to a branch? --- a: `git checkout [name]`
- q: How to create and switch to a branch with a single command? --- a: `git checkout -b [name]`
- q: What is `git branch -f [name] [commit]` for? --- a: ask community, learngitbranching-rampup3, <https://stackoverflow.com/questions/28149804/difference-between-git-branch-f-branch-name-hash-and-git-checkout-branc/28150031>

- q: `git revert`vs `git reset` --- a: learngitbranching-rampup4

- q: What is `git cherry-pick` for? --- a: learngitbranching-move1
- q: What is rebase? --- a: it's like a massive cherry-picking from one branch to another --- a: <http://think-like-a-git.net/sections/rebase-from-the-ground-up/using-git-cherry-pick-to-simulate-git-rebase.html>, <http://think-like-a-git.net/sections/rebase-from-the-ground-up/a-helpful-mnemonic-for-git-rebase-arguments.html>


- q: What if you want to merge branches after cherry-picking? --- a: Avoid duplicating by using rebase:
<https://stackoverflow.com/questions/14486122/how-does-git-merge-after-cherry-pick-work/44966513#44966513>
<https://stackoverflow.com/questions/20380013/git-merge-strategies-spaces-make-default-shows-no-conflict-and-bring-unexpected>

{: .centered}
![python deques](./images/git.graph.001.svg)
