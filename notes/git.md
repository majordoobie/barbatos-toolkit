# Git Notes

[Git Basics](#1)
[More on remote](#2)  
[Git Branches](#3)  
[Merge with master](#4)  
[.gitignore](#5)
[Force pull](#6)

---

## Git basic

| Command | Description |
| ----------- | ----------- |
| `git init` | Initializes the current local folder with the .git files to begin tracking changes |
| `git status` | Shows you the status of files from unstages, to uncommitted, to status of remote head |
| `git remote add <remote_alias> <url>` | Link local repo with a remote repo |
| `git add <files>` | Add files in your current directory to the staging area |
| `git commit -m <msg>` | Commit **STAGED** changes to the local repo |
| `git push <remote> <branch>` | Push **COMMITED** changes to the remote repo |

---

## More on remote

| Command | Description |
| ----------- | ----------- |
| `git remote -v` | List remote links with their alias that the local git is tracking |
| `git remote add <remote_alias> <utl>` | Link remote repo with an alias for the local repo to use |
| `git push -f <remote_alias> <branch>` | If you rebase or either the remote or local heads are too off sync you will have to force the push, reset, or manually fix the changes. `-f` forces the push.

---

## Branches

| Command | Description |
| ----------- | ----------- |
| `git branch` | List branches |
| `git branch <branch>` | Create a new branch |  
| `git status` | Tells you what branch you are in and status of files |
| `git checkout <branch>` | Checks out a branch you have already created |

---

## Merge with master

| Command | Description |
| ----------- | ----------- |
| `git checkout master` | Check out the branch you want to merge into |
| `git merge <branch>` | Merges branch specified with the branch you are currently on |

---

## .gitignore

Not all files belong to the remote repo such as a db or credentials file. You can use the `.gitignore` to create a \n seperated regex values for git to ignore.

| Command | Description |
| ----------- | ----------- |
| `git rm` | Removes a file from disc and from being tracked |
| `git rm --cached <file>` | Removes file from being tracked but keeps it on disc |
| `git fetch <remote_alias>` | Pulls the most recent information from the remote |
| `git checkout FETCH_HEAD -- <file>` | Pulls a single file from remote and overwrite what is on disc |
---

## Force git pull

[Source](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)

```md
git fetch --all
git reset --hard <remote>/<branch>
```

  

