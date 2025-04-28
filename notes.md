# The Guts of Git

## Agenda

Commands:

- git restore
- git reset
- git log
- git diff

Concepts:

- HEAD
- Commit hashes & Refs
- "The Three Trees"
- Force-pushing

Scenarios:

- "I staged (added) code I don't want to commit, but I didn't commit it yet." --> git restore --staged

- "I just committed code I don't want, but didn't push it yet." --> git reset --soft

- "I just committed and pushed code I don't want" --> git reset --hard plus a force push.

## The .git dir

- This is what makes a normal dir into a git repo
- Almost all git info (commits, remote urls, etc) is stored in the .git directory
- You should NEVER delete the .git directory

## Git Commits

### Git Commit Hashes

- A hash uniquely identifies a commit
- Every commit has a hash

### Git Commit Refs

- A ref is like a variable name for a commit
- Not every commit has a ref
- A commit can have more than one ref
- HEAD is a ref pointing to the most recent commit on a branch

## The Three Trees 

### Working Tree

### Index

### Commit History, or, HEAD


## git-revert

- For making a new commit that reverts the changes made by other commits.

## git-restore

- For restoring files in the working tree from either the index or another commit.

## git-reset

- For updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history.

- git reset can also be used to restore the index, overlapping with git restore.
