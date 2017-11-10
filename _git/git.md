---
title:   "Git"
layout:  collection_page

---

* this line gets replaced with the generated table of contents
{:toc}


# tutorials and cheatsheets

<https://ndpsoftware.com/git-cheatsheet.html#loc=stash;>
<http://justinhileman.info/article/git-pretty/git-pretty.png>

<https://www.atlassian.com/git/tutorials/undoing-changes>
<https://www.atlassian.com/git/tutorials/syncing>

TODO: create a repo for excersises

# undo

<https://stackoverflow.com/questions/8358035/whats-the-difference-between-git-revert-checkout-and-reset#8358039>

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


